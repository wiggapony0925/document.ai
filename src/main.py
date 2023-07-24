import tkinter as tk
from tkinter import ttk, filedialog
import os
import webbrowser
#from summarizer import summarize_text

attached_file = None

def browse_file():
    global attached_file
    file_path = filedialog.askopenfilename(
        initialdir="./data",
        title="Select a file",
        filetypes=(
            ("PDF files", "*.pdf"),
            ("Google Slides", "*.pptx"),
            ("Word Documents", "*.docx"),
            ("Text files", "*.txt"),
        ),
    )
    if file_path:
        attached_file = file_path
        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_path)[1].lstrip(".").upper()
        file_info.config(text=f"File Name: {file_name}\nFile Type: {file_type}")
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, f"File Name: {file_name}\nFile Type: {file_type}\n\n{file_content}")

def open_file():
    if attached_file:
        webbrowser.open(attached_file)

def summarize_button_click():
    # Get user input from text field or other elements
    user_input = input_text.get("1.0", tk.END)
    
    # Here, you can take the selected instruction and style from the dropdowns
    selected_instruction = instruction_combobox.get()
    selected_style = style_combobox.get()
    
    # Process the user input, fetch content from Google Slides/Docs, etc.
    # Perform summarization using the summarize_text function from summarizer.py
    summary = "" # summarize_text(user_input, instruction=selected_instruction, style=selected_style)
    
    # Display the summary in the output text box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

root = tk.Tk()
root.title("Google Slides & Docs Summarizer")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), padding=6)

input_label = ttk.Label(root, text="File Attachment:")
input_label.grid(row=0, column=0, columnspan=2)

attachment_button = ttk.Button(root, text="Attach File", command=browse_file)
attachment_button.grid(row=1, column=0, padx=10, pady=5)

open_file_button = ttk.Button(root, text="Open File", command=open_file)
open_file_button.grid(row=1, column=1, padx=10, pady=5)

file_info = ttk.Label(root, text="")
file_info.grid(row=2, column=0, columnspan=2)

instruction_combobox = ttk.Combobox(root, values=["Respond to email", "Write a letter", "Summarize it"])
instruction_combobox.grid(row=3, column=0, padx=10, pady=5)

style_combobox = ttk.Combobox(root, values=["Professional", "Funny", "Gratitude"])
style_combobox.grid(row=3, column=1, padx=10, pady=5)

summarize_button = ttk.Button(root, text="Summarize", command=summarize_button_click)
summarize_button.grid(row=4, column=0, padx=10, pady=5)

output_label = ttk.Label(root, text="Summary:")
output_label.grid(row=5, column=0, columnspan=2)

input_text = tk.Text(root, width=60, height=10)
input_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

output_text = tk.Text(root, width=60, height=10)
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
