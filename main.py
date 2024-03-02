import tkinter as tk
import ctypes
import os

window = tk.Tk()
window.title("Planner")
window.state("zoomed")
frameList = tk.Frame(window, background="red")
frameList.pack(side=tk.BOTTOM, fill = tk.BOTH, expand=True)
frameOther = tk.Frame(window, background="blue")
frameOther.pack(side=tk.TOP, fill=tk.X, expand=False)

path = "C:\\Users\\timur\\PycharmProjects\\NotesAppStorage"
os.chdir(path)

def read_notes(file_path):
    with open(file_path, "r") as f:
        print(f.read())

def open_notes(noteName):
    newWindow = tk.Toplevel(window)
    newWindow.title(noteName)
    newWindow.state("zoomed")
    file_path = f"{path}\\{noteName}"

    def saveNote():
        newText = notesText.get("1.0", "end-1c")
        with open(file_path, "w") as f:
            f.write(newText)
            f.close()

    notesText = tk.Text(newWindow, background="red",height=20, width=40)
    notesText.pack()
    saveButton = tk.Button(newWindow, text="Save", background="blue", width=10, height=5,
                    command= saveNote,
                    font=("Comic Sans", 10),
                    fg="#EEF5FF", bg="#B4D4FF",
                    activeforeground="#EEF5FF", activebackground="#B4D4FF",padx=4).pack()

    with open(file_path, "r") as f:
        notesText.insert(tk.END, f.read())




def addNote():
    if(nameEntry.get() != ""):
        notesList.insert(tk.END, nameEntry.get())
        notesList.itemconfig(tk.END, {'bg': '#285d69'})

def onselect(evt):
    w = evt.widget
    if(len(w.curselection()) != 0):
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))
        open_notes(value)

noteButton = tk.Button(frameOther, text="New Note", background="blue", width=10, height=5,
                    command= addNote,
                    font=("Comic Sans", 10),
                    fg="#EEF5FF", bg="#B4D4FF",
                    activeforeground="#EEF5FF", activebackground="#B4D4FF",padx=4)
noteButton.grid(row=0, column=0, sticky = tk.W)


nameEntry = tk.Entry(frameOther, font=("Ariel",35))
nameEntry.grid(row=0, column=1, sticky = tk.W)


scroller = tk.Scrollbar(frameList, width=60, background="red", activebackground="red", bg="red")
scroller.pack(side=tk.RIGHT,fill=tk.Y )

notesList = tk.Listbox(frameList, yscrollcommand = scroller.set, font=("Comic Sans", 20), bg="#55adad", fg="white")
notesList.pack(side=tk.TOP, fill = tk.BOTH, expand=True )
notesList.bind("<Double-Button>", onselect)

scroller.config( command = notesList.yview )

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\\{file}"
        notesList.insert(tk.END, file)
        with open(file_path, "r") as f:
            print(f.read())
        print(file)


ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()