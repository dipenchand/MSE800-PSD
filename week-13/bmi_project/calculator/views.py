import os
from django.shortcuts import render
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

def bmi_calculator(request):
    bmi = None
    category = None
    height = None
    weight = None
    plan = None
    age = request.POST.get('age')
    gender = request.POST.get('gender')

    if request.method == 'POST':
        height = float(request.POST['height']) # height in cm
        weight = float(request.POST['weight']) # weight in kg

        # formula: BMI = weight (kg) / [height (m)] x [height (m)]
        height_in_meters = height / 100
        bmi = round(weight / (height_in_meters**2), 2)

        # BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        plan = generate_plan_with_llm(age, gender, weight, height, bmi, category)
    
    return render(request, 'bmi.html', {
        'bmi': bmi, 
        'category': category,
        'age': age,
        'gender': gender,
        'plan': plan
        })

def generate_plan_with_llm(age, gender, weight, height, bmi, category):
    api_key = os.environ.get('GEMINI_API_KEY', '')
    if not api_key:
        return "Missing GEMINI_API_KEY. Set it in your environment or in the project's .env file."

    client = genai.Client(api_key=api_key)

    system_prompt = (
        "You are a fitness and nutrition planning assistant. "
        "Provide safe, practical, evidence-based general guidance. "
        "Do not provide medical diagnosis or treatment. "
        "If the user has medical conditions, pregnancy, injury, eating disorder history, or takes medication, "
        "recommend consulting a qualified clinician before starting the plan. "
        "Return ONLY an HTML fragment (no Markdown, no code fences). "
        "Do not include <html>, <head>, or <body> tags."
    )

    stop_token = "<!-- END_OF_PLAN -->"

    positive_prompt = (
        "Create a detailed, structured 4-week diet and exercise plan tailored to the person. "
        "Use metric units. Be specific about portion sizes and daily workouts. "
        "Include progression week-to-week, rest days, warm-up/cool-down, hydration and sleep guidance. "
        "Make it realistic for a typical adult with limited time and budget. "
        "Output must be valid HTML using headings and lists. "
        "Use this structure:\n"
        "<div class='ai-plan'>\n"
        "  <h4>Week 1</h4><h5>Meals</h5><ul>...</ul><h5>Exercise</h5><ul>...</ul>\n"
        "  <h4>Week 2</h4>...\n"
        "  <h4>Week 3</h4>...\n"
        "  <h4>Week 4</h4>...\n"
        "  <h4>Maintenance Tips</h4><ul>...</ul>\n"
        "</div>\n"
        f"End your response with {stop_token}."
    )

    negative_prompt = (
        "Avoid: unsafe or extreme calorie restriction; recommending drugs, steroids, or prescription medications; "
        "dangerous exercises; shaming language; absolute guarantees of results. "
        "Do not output personal data beyond what is provided."
    )

    prompt = f"""
    {positive_prompt}

    Person:
    - Age: {age} years old
    - Gender: {gender}
    - Weight: {weight} kg
    - Height: {height} cm
    - BMI: {bmi}
    - Category: {category}

    {negative_prompt}
    """

    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            max_output_tokens=1400,
            stop_sequences=[stop_token],
        ),
    )

    text = response.text or ""
    return text.replace(stop_token, "").strip()