from openai import OpenAI
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from pathlib import Path
import os

# Load the .env file from the current script directory
load_dotenv(dotenv_path=Path(__file__).resolve().parent / '.env')

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("API key not found. Make sure you have a .env file with OPENAI_API_KEY set.")

# Create OpenAI client using the latest SDK structure
client = OpenAI(api_key=api_key)

# Function to get AI completion
def get_completion():
    prompt = input_box.get()
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        output = response.choices[0].message.content.strip()
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, output)
    except Exception as e:
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, f"Error: {str(e)}")

# GUI setup
window = tk.Tk()
window.title("AI Completion GUI")

tk.Label(window, text="Enter your prompt:").pack(pady=5)
input_box = tk.Entry(window, width=80)
input_box.pack(pady=5)

submit_btn = tk.Button(window, text="Submit", command=get_completion)
submit_btn.pack(pady=5)

output_box = scrolledtext.ScrolledText(window, height=15, width=80)
output_box.pack(pady=10)

window.mainloop()
