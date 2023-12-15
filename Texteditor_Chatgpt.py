# import tkinter as tk
# from tkinter.filedialog import askopenfilenames, asksaveasfilename

# class TextEditorApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Text Editor")
#         self.master.iconbitmap("D:\Icons\\blogging_7795639.ico")

#         self.create_widgets()

#     def create_widgets(self):
#         # Configure row and column weights
#         self.master.rowconfigure(0, weight=1)
#         self.master.columnconfigure(1, weight=1)

#         # Create a frame
#         self.frame = tk.Frame(self.master, relief=tk.RAISED)
#         self.frame.grid(row=0, column=0, sticky="nw")

#         # Create Open File button
#         self.open_button = tk.Button(self.frame, text="Open File", command=self.open_file)
#         self.open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#         # Create Save As button
#         self.save_button = tk.Button(self.frame, text="Save As", command=self.save_as)
#         self.save_button.grid(row=1, column=0, sticky="ew", padx=5)

#         # Create Text widget
#         self.text = tk.Text(self.master)
#         self.text.grid(row=0, column=1, sticky="nsew")

#     def open_file(self):
#         filepaths = askopenfilenames(filetypes=[("All files", "*.*"), ("Text Files", "*.txt")])

#         if not filepaths:
#             return

#         # Clear existing content in the text widget
#         self.text.delete("1.0", tk.END)

#         # Insert content of each selected file
#         for filepath in filepaths:
#             with open(filepath, "r") as input_file:
#                 txt = input_file.read()
#                 self.text.insert(tk.END, txt)

#     def save_as(self):
#         filepath = asksaveasfilename(
#             defaultextension="txt",
#             filetypes=[('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
#         )

#         if not filepath:
#             return

#         # Write content to the selected file
#         with open(filepath, "w") as output_file:
#             txt = self.text.get("1.0", tk.END)
#             output_file.write(txt)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TextEditorApp(root)
#     root.mainloop()








# import tkinter as tk
# from tkinter import messagebox, filedialog

# class NoteApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Note App")

#         self.notes = []

#         self.create_widgets()

#     def create_widgets(self):
#         self.text_box = tk.Text(self.master, height=15, width=60)  # Adjusted height and width
#         self.text_box.pack(pady=10)

#         self.save_button = tk.Button(self.master, text="Save Note", command=self.save_note)
#         self.save_button.pack(side=tk.LEFT, padx=5)

#         self.save_as_button = tk.Button(self.master, text="Save As", command=self.save_as_note)
#         self.save_as_button.pack(side=tk.LEFT, padx=5)

#         self.open_button = tk.Button(self.master, text="Open File", command=self.open_file)
#         self.open_button.pack(side=tk.LEFT, padx=5)

#         self.view_button = tk.Button(self.master, text="View Notes", command=self.view_notes)
#         self.view_button.pack(side=tk.LEFT, padx=5)

#         self.clear_button = tk.Button(self.master, text="Clear Notes", command=self.clear_notes)
#         self.clear_button.pack(side=tk.LEFT, padx=5)

#     def save_note(self):
#         note_content = self.text_box.get("1.0", tk.END).strip()
#         if note_content:
#             self.notes.append(note_content)
#             messagebox.showinfo("Note Saved", "Your note has been saved successfully.")
#             self.text_box.delete("1.0", tk.END)
#         else:
#             messagebox.showwarning("Empty Note", "Cannot save an empty note.")

#     def save_as_note(self):
#         note_content = self.text_box.get("1.0", tk.END).strip()
#         if note_content:
#             file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#             if file_path:
#                 with open(file_path, "w") as file:
#                     file.write(note_content)
#                 messagebox.showinfo("Note Saved", "Your note has been saved successfully.")
#                 self.text_box.delete("1.0", tk.END)
#         else:
#             messagebox.showwarning("Empty Note", "Cannot save an empty note.")

#     def open_file(self):
#         file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#         if file_path:
#             with open(file_path, "r") as file:
#                 note_content = file.read()
#                 self.text_box.delete("1.0", tk.END)
#                 self.text_box.insert(tk.END, note_content)
#                 messagebox.showinfo("File Opened", "The file has been opened successfully.")

#     def view_notes(self):
#         if not self.notes:
#             messagebox.showinfo("No Notes", "There are no notes to display.")
#         else:
#             notes_text = "\n".join(f"{i + 1}. {note}" for i, note in enumerate(self.notes))
#             messagebox.showinfo("Your Notes", notes_text)

#     def clear_notes(self):
#         confirmation = messagebox.askyesno("Confirm", "Are you sure you want to clear all notes?")
#         if confirmation:
#             self.notes = []
#             messagebox.showinfo("Notes Cleared", "All notes have been cleared.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = NoteApp(root)
#     root.mainloop()












# import tkinter as tk
# from tkinter import messagebox, filedialog

# class NoteApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Note App")

#         self.notes = []

#         self.create_widgets()

#     def create_widgets(self):
#         self.text_box = tk.Text(self.master, height=15, width=60)
#         self.text_box.pack(pady=10)

#         self.save_button = tk.Button(self.master, text="Save Note", command=self.save_note)
#         self.save_button.pack(side=tk.LEFT, padx=5)

#         self.save_as_button = tk.Button(self.master, text="Save As", command=self.save_as_note)
#         self.save_as_button.pack(side=tk.LEFT, padx=5)

#         self.open_button = tk.Button(self.master, text="Open File", command=self.open_file)
#         self.open_button.pack(side=tk.LEFT, padx=5)

#         self.view_button = tk.Button(self.master, text="View Notes", command=self.view_notes)
#         self.view_button.pack(side=tk.LEFT, padx=5)

#         self.clear_button = tk.Button(self.master, text="Clear Notes", command=self.clear_notes)
#         self.clear_button.pack(side=tk.LEFT, padx=5)

#         self.copy_button = tk.Button(self.master, text="Copy Text", command=self.copy_text)
#         self.copy_button.pack(side=tk.LEFT, padx=5)

#         self.cut_button = tk.Button(self.master, text="Cut Text", command=self.cut_text)
#         self.cut_button.pack(side=tk.LEFT, padx=5)

#         self.paste_button = tk.Button(self.master, text="Paste Text", command=self.paste_text)
#         self.paste_button.pack(side=tk.LEFT, padx=5)

#         self.undo_button = tk.Button(self.master, text="Undo", command=self.undo_text)
#         self.undo_button.pack(side=tk.LEFT, padx=5)

#     def save_note(self):
#         note_content = self.text_box.get("1.0", tk.END).strip()
#         if note_content:
#             self.notes.append(note_content)
#             messagebox.showinfo("Note Saved", "Your note has been saved successfully.")
#             self.text_box.delete("1.0", tk.END)
#         else:
#             messagebox.showwarning("Empty Note", "Cannot save an empty note.")

#     def save_as_note(self):
#         note_content = self.text_box.get("1.0", tk.END).strip()
#         if note_content:
#             file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#             if file_path:
#                 with open(file_path, "w") as file:
#                     file.write(note_content)
#                 messagebox.showinfo("Note Saved", "Your note has been saved successfully.")
#                 self.text_box.delete("1.0", tk.END)
#         else:
#             messagebox.showwarning("Empty Note", "Cannot save an empty note.")

#     def open_file(self):
#         file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#         if file_path:
#             with open(file_path, "r") as file:
#                 note_content = file.read()
#                 self.text_box.delete("1.0", tk.END)
#                 self.text_box.insert(tk.END, note_content)
#                 messagebox.showinfo("File Opened", "The file has been opened successfully.")

#     def view_notes(self):
#         if not self.notes:
#             messagebox.showinfo("No Notes", "There are no notes to display.")
#         else:
#             notes_text = "\n".join(f"{i + 1}. {note}" for i, note in enumerate(self.notes))
#             messagebox.showinfo("Your Notes", notes_text)

#     def clear_notes(self):
#         confirmation = messagebox.askyesno("Confirm", "Are you sure you want to clear all notes?")
#         if confirmation:
#             self.notes = []
#             messagebox.showinfo("Notes Cleared", "All notes have been cleared.")

#     def copy_text(self):
#         selected_text = self.text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
#         self.master.clipboard_clear()
#         self.master.clipboard_append(selected_text)

#     def cut_text(self):
#         self.copy_text()
#         self.text_box.delete(tk.SEL_FIRST, tk.SEL_LAST)

#     def paste_text(self):
#         pasted_text = self.master.clipboard_get()
#         self.text_box.insert(tk.SEL_FIRST, pasted_text)

#     def undo_text(self):
#         self.text_box.edit_undo()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = NoteApp(root)
#     root.mainloop()





# import tkinter as tk
# from tkinter.filedialog import askopenfilenames, asksaveasfile 
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# root = tk.Tk()


# def saveAs(): 
#     filepath = asksaveasfile(
#         defaultextension= "txt",
#         filetypes= [('All Files', '*.*'),  ('Python Files', '*.py'), ('Text Document', '*.txt')])
    
#     if not filepath:
#         return

    
#     with open(filepath, "w") as output_file:
#         txt = text.get(1.0 , tk.END)
#         output_file.write(txt)


# def openFile():
#     filepaths = askopenfilenames(filetypes=[("All files", "*.*"), ("Text Files", "*.txt")])

#     if not filepaths:
#         return

#     text.delete("1.0", tk.END)  # Clear existing content in the text widget

#     with open(filepaths, "r") as input_file:
#         txt = input_file.read()
#         text.insert(tk.END, txt)


# root.title("TextEditor")

# root.iconbitmap("D:\Icons\\blogging_7795639.ico") # sets and icon to the program


# root.rowconfigure(0, minsize= 600)
# root.columnconfigure(1, minsize=800)


# frame = tk.Frame(root, relief=tk.RAISED)

# OpenFile = tk.Button(frame, text = "Open File",command=openFile)
# OpenFile.grid(column= 0, row= 0,sticky="ew", padx=5, pady=5)

# SaveAs = tk.Button(frame, text = "Save As",command=saveAs)
# SaveAs.grid(column= 0, row= 1,sticky="ew",padx=5)

# frame.grid(column=0, row=0,sticky="nw")

# text = tk.Text(root)
# text.grid(column=1, row=0,sticky="nsew")


# root.mainloop()






# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# # root window
# root = tk.Tk()
# root.geometry("300x150")
# root.resizable(False, False)
# root.title('Sign In')

# # store email address and password
# email = tk.StringVar()
# password = tk.StringVar()


# def login_clicked():
#     """ callback when the login button clicked
#     """
#     msg = f'You entered email: {email.get()} and password: {password.get()}'
#     showinfo(
#         title='Information',
#         message=msg
#     )


# # Sign in frame
# signin = ttk.Frame(root)
# signin.pack(padx=10, pady=10, fill='x', expand=True)


# # email
# email_label = ttk.Label(signin, text="Email Address:")
# email_label.pack(fill='x', expand=True)

# email_entry = ttk.Entry(signin, textvariable=email)
# email_entry.pack(fill='x', expand=True)
# email_entry.focus()

# # password
# password_label = ttk.Label(signin, text="Password:")
# password_label.pack(fill='x', expand=True)

# password_entry = ttk.Entry(signin, textvariable=password, show="*")
# password_entry.pack(fill='x', expand=True)

# # login button
# login_button = ttk.Button(signin, text="Login", command=login_clicked)
# login_button.pack(fill='x', expand=True, pady=10)


# root.mainloop()





# # Learning GUI
# title = root.title() 
# print(title)  # print the title in the CLI


# root.geometry("800x500+50+50") # Sets the width and height and where the program is going to show
# root.minsize(100, 70) # Sets the minimum size 
# root.maxsize(800, 500) # Sets the Maximum size

# root.resizable(False,False) # Prevents the user from MIN or MAX the program


# root.attributes("-topmost", 1)
# root.attributes("-alpha",0.5) # Modifying the transparency of the program



# label = tk.Label(root, text = "tk themed.").pack()
# label = ttk.Label(root, text = "ttk themed.").pack()



# button = ttk.Button(root, text="Exit" , command=lambda : root.quit())
# button.pack(padx=10,pady=200, expand=True)
# button.state(["disabled"]) # didn't get it. It disable or enable a button but I don't know how?


# def button_clicked():
#     showinfo(title= "Information", message= "Download button clicked successfully!")

# downloadimage = tk.PhotoImage(file="D:\weather app icon/download.png")


# button = ttk.Button(root, image= downloadimage, text= "Download", compound=tk.LEFT, command=button_clicked)
# button.pack(ipadx=30, ipady=5, expand=True)
# email = tk.StringVar()
# password = tk.StringVar()

# passwordlabel = tk.Label(root, text= "Password:", padx= "50",pady= "2")
# passwordlabel.pack()

# textbox = ttk.Entry(root, textvariable=password,show="*")
# textbox.pack()


# label = tk.Label(root, text="This is your TextEditor. Hope you use  it well.")
# label.pack()


