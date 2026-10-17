# 💊 Pharmacy AI Chatbot (Google Gemini)

A command-line pharmacy assistant built on **Google Gemini**. It answers general questions about medicines and pharmacy topics in **Arabic or English**, with **safety guardrails** so it never acts like a doctor.

## 📌 Overview
| | |
|---|---|
| **Model** | Google Gemini (via the `google-genai` SDK) |
| **Tools** | Python, google-genai, python-dotenv |
| **Languages** | Replies in the same language as the user (Arabic / English) |

## 🛡️ Safety Design
Health is a sensitive domain, so the chatbot is built with three layers of protection:

1. **System prompt rules:** the model is instructed to give only simple, general information and to:
   - **not** diagnose diseases
   - **not** prescribe medicines or recommend dangerous ones
   - **not** give exact personalized doses
   - tell the user when to see a doctor or pharmacist
2. **Danger-word filter (before the AI is called):** if a question mentions a high-risk topic such as chest pain, pregnancy, allergy, babies, or overdose (in **English or Arabic**: ألم الصدر، حامل، حساسية، رضيع، جرعة زائدة), the bot does **not** send it to the model. It immediately tells the user to contact a doctor or pharmacist.
3. **Disclaimer on every answer:** each reply ends with a reminder that the information does not replace professional advice.

It also handles empty input, `exit` / `quit`, and API errors without crashing.

## 💬 Example
```
Pharmacy Chatbot
Type exit or quit to stop.

User: What is paracetamol used for?
Bot: <general information from Gemini>

Important: This information is general and does not replace consulting a doctor or pharmacist.

User: I took an overdose of my pills
Bot: Warning: This situation may require immediate professional medical advice.
Please contact a doctor or pharmacist immediately.
```

## ▶️ How to Run
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and put your key in it:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run:
   ```bash
   python pharmacy_chatbot.py
   ```

> 🔒 The API key is read from the `.env` file, which is listed in `.gitignore`, so it is never uploaded to GitHub.

## 📁 Project Structure
```
├── pharmacy_chatbot.py   # The chatbot
├── requirements.txt
├── .env.example          # Template for your API key
└── .gitignore            # Keeps .env private
```

## ⚠️ Disclaimer
This is a learning project. It provides general information only and is **not** a substitute for professional medical advice.

## 👤 Author
**Waseem Mahmoud** · [LinkedIn](https://www.linkedin.com/in/waseem-mahmoud-a34154213) · [GitHub](https://github.com/waseemalali)
