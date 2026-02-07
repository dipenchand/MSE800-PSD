import os
import json
import urllib.request
import urllib.error
import pdfplumber
import docx

def _get_google_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        return api_key

    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(dotenv_path):
        return None

    with open(dotenv_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if k == "GOOGLE_API_KEY" and v:
                return v
    return None


GOOGLE_API_KEY = _get_google_api_key()
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Set it in your environment or in a .env file.")

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file_path):
    """Extracts text from a DOCX file."""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def analyze_cv(cv_text):
    """Sends CV text to Gemini for analysis."""
    prompt = f"""
    POSITIVE PROMPT

    - Instructions
      1. Identify and categorize the candidate's experience into software-relevant areas (Backend, Frontend, Full-Stack, Mobile, DevOps/Cloud, Data/ML, QA/Automation, Leadership).
      2. Suggest the candidate's top two strengths and the most relevant software developer job roles based on their experience and tech stack.
      3. Provide three CV improvement recommendations in bullet points (focus on measurable impact, clarity of projects/ownership, and relevant keywords/tools).

    - Context
      You are an expert AI recruiter and senior Software Developer reviewing a candidate's Software Developer CV.

    - Input data
      CV_TEXT:
      ```
      {cv_text}
      ```

    - Output Indicator
      Return your answer in Markdown with exactly these sections:
      1) Experience Categories (bullets per category)
      2) Top Strengths (exactly 2 bullets)
      3) Best-Fit Roles (3-5 role titles)
      4) CV Improvement Recommendations (exactly 3 bullets)

    NEGATIVE PROMPT

    - Instructions
      1. Do not invent experience, education, employers, dates, certifications, or technologies not present in CV_TEXT.
      2. Do not include personal data not already in CV_TEXT.
      3. Do not output the full CV or large excerpts; summarize only.
      4. Do not add disclaimers or policy text.

    - Context
      If CV_TEXT is missing key details, state what is missing as short bullets under the most relevant section.

    - Input data
      CV_TEXT:
      ```
      {cv_text}
      ```

    - Output Indicator
      If CV_TEXT is empty or unreadable, output:
      "CV_TEXT_EMPTY" and one bullet describing the likely cause (e.g., scanned PDF, extraction failure).
    """

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    req = urllib.request.Request(
        url=url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-goog-api-key": GOOGLE_API_KEY,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            resp_json = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini API HTTP error {e.code}: {body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Gemini API request failed: {e}") from e

    try:
        return resp_json["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        raise RuntimeError(f"Unexpected Gemini response format: {resp_json}")

if __name__ == "__main__":
    file_path = input("Enter CV file path (PDF/DOCX): ").strip()

    if not os.path.exists(file_path):
        print("File not found!")
        exit()

    # Extract text based on file type
    if file_path.endswith(".pdf"):
        cv_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        cv_text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format!")
        exit()

    print("\nAnalyzing CV with Gemini...\n\n ", cv_text,"\n\n")
    analysis_result = analyze_cv(cv_text)
    
    print("\n--- CV Analysis Results ---\n")
    print(analysis_result)
