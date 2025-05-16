import tkinter as tk
from tkinter import filedialog, Text, messagebox

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select HTML Document",
        filetypes=[("Text files", "*.html")]
    )
    if file_path:
        messagebox.showinfo("File Selected", f"You selected:\n{file_path}")
        print(f"File path: {file_path}")

def get_input():
    user_input = input_box.get("1.0", tk.END).strip()
    print(f"User input: {user_input}")
    messagebox.showinfo("Input Received", f"You entered:\n{user_input}")

# Create the main window
root = tk.Tk()
root.title("Document Uploader with Input Box")
root.geometry("400x300")

# Upload button
upload_btn = tk.Button(root, text="Upload Document", command=upload_file)
upload_btn.pack(pady=10)

# Text box for user input
input_label = tk.Label(root, text="Enter your input:")
input_label.pack()

input_box = Text(root, height=5, width=40)
input_box.pack(pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit Input", command=get_input)
submit_btn.pack(pady=10)

# Run the application
root.mainloop()
