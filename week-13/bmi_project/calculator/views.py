from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == 'POST':
        height = float(request.POST['height']) # height in cm
        weight = float(request.POST['weight']) # weight in kg

        # formula: BMI = weight (kg) / [height (m)] x [height (m)]
        height_in_meters = height / 100
        bmi = weight / (height_in_meters * height_in_meters)

        # BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
    
    return render(request, 'bmi.html', {'bmi': bmi, 'category': category})