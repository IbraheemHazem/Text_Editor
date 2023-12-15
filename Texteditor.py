import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from tkinter import ttk

root = tk.Tk()

def saveAs(): 
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
    )
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        txt = text.get("1.0", tk.END)
        output_file.write(txt)

def openFile():
    filepaths = askopenfilenames(filetypes=[("All files", "*.*"), ("Text Files", "*.txt")])

    if not filepaths:
        return

    text.delete("1.0", tk.END)  # Clear existing content in the text widget

    for filepath in filepaths:
        with open(filepath, "r") as input_file:
            txt = input_file.read()
            text.insert(tk.END, txt)

root.title("TextEditor")
root.iconbitmap("D:\Icons\\blogging_7795639.ico")

root.rowconfigure(0, minsize=600)
root.columnconfigure(1, minsize=800)

frame = tk.Frame(root, relief=tk.RAISED)

OpenFile = tk.Button(frame, text="Open File", command=openFile)
OpenFile.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

SaveAs = tk.Button(frame, text="Save As", command=saveAs)
SaveAs.grid(column=0, row=1, sticky="ew", padx=5)

frame.grid(column=0, row=0, sticky="nw")

text = tk.Text(root)
text.grid(column=1, row=0, sticky="nsew")

root.mainloop()