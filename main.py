"""
Extra Whitespace Remover Script (Powered by Tkinter)
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__license__ = "MIT"
__version__ = "0.1.1"

import tkinter as tk
from tkinter import ttk


def remove_extra_whitespace(event):
    input_text = input_text_widget.get("1.0", tk.END)
    words = input_text.split()
    processed_text = " ".join(words)
    output_text_widget.config(state="normal")
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.insert("1.0", processed_text)
    output_text_widget.config(state="disabled")


def copy_output_text():
    root.clipboard_clear()
    root.clipboard_append(output_text_widget.get("1.0", tk.END))


root = tk.Tk()
root.resizable(False, False)
root.title("Extra Whitespace Remover")


header = ttk.Label(root, text="Extra Whitespace Remover")
header["font"] = "Menlo", 24, "bold"
header.pack(pady=10)

input_text_widget = tk.Text(root, width=80, height=4)
input_text_widget["font"] = "Menlo", 18
input_text_widget["wrap"] = "word"
input_text_widget.pack(padx=10, pady=(0, 10))

output_text_widget = tk.Text(root, width=80, height=4, state="disabled")
output_text_widget["font"] = "Menlo", 18
output_text_widget["wrap"] = "word"
output_text_widget.pack(padx=10, pady=(0, 10))

input_text_widget.bind("<KeyRelease>", remove_extra_whitespace)


copy_button = ttk.Button(root, text="Copy Output", command=copy_output_text)
copy_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))


root.mainloop()
