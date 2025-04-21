# Friday Project 9 – AI Prompt Completion GUI

This project is a simple Python GUI application that allows users to enter a prompt, submit it to OpenAI's API, and receive an AI-generated completion. The interface also includes prompt history, a clear button, and saves all output to a local text file.

---

## 🚀 Features

- Input prompt field
- Submit and clear buttons
- AI-generated response display
- Prompt history log
- Automatically saves completions to `completions.txt`
- Uses `.env` file for secure API key storage

---

## 📁 Files

- `FridayProject9.py` – Main GUI application
- `.env` – Stores your OpenAI API key (not shared publicly)
- `completions.txt` – Output file where all prompt/response pairs are saved
- `README.md` – Instructions and overview (this file)

---

## 🧪 How to Test It Using Your Own API Key

### 1. **Install Required Libraries**
Make sure you have the correct packages installed:

```bash
pip install openai python-dotenv
