from google import genai
from google.genai import types


import os

from dotenv import load_dotenv

# The API key is read from the GEMINI_API_KEY environment variable
# (put it in a .env file next to this script - never write it in the code)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

client = genai.Client(api_key=api_key)


system_prompt = """
You are a helpful pharmacy assistant chatbot.

Give simple and general pharmacy information.
Do not diagnose diseases.
Do not prescribe medicines.
Do not recommend dangerous medicines.
Do not give exact personalized doses.
Answer in the same language used by the user.
Tell the user when they should ask a doctor or pharmacist.
Keep answers simple and clear.
"""


warning_message = """
Warning: This situation may require immediate professional medical advice.
Please contact a doctor or pharmacist immediately.

Important: This information is general and does not replace consulting
a doctor or pharmacist.
"""


danger_words = [
    "chest pain",
    "pregnancy",
    "pregnant",
    "allergy",
    "baby",
    "overdose",
    "ألم الصدر",
    "حامل",
    "حساسية",
    "رضيع",
    "جرعة زائدة"
]


print("Pharmacy Chatbot")
print("Type exit or quit to stop.\n")


while True:

    question = input("User: ").strip()

    # إغلاق البرنامج
    if question.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    # منع السؤال الفارغ
    if question == "":
        print("Bot: Please enter a question.")
        continue

    # فحص الكلمات الخطرة
    if any(word in question.lower() for word in danger_words):
        print("Bot:", warning_message)
        continue

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )

        print("\nBot:", response.text)

        # التنبيه يضاف دائمًا
        print(
            "\nImportant: This information is general and does not replace "
            "consulting a doctor or pharmacist.\n"
        )

    except Exception as error:
        print("Bot: An error occurred:", error)