import os
import pyperclip
import openai
import tkinter as tk

# Replace YOUR_API_KEY with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Get the currently copied text
text = pyperclip.paste()

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are an excellent summarizer."},
        {"role": "user", "content": f"Summarize the following: {text}"}
    ]
)

# Create a GUI window and display the result
root = tk.Tk()
root.title("ChatGPT Summary")
root.geometry("400x300")
result_label = tk.Label(root, text=response.choices[0].message.content.strip(), font=("Arial", 16), wraplength=380)
result_label.pack(expand=True, fill="both")
root.mainloop()
