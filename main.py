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

buttonBG = "#B4D4FF"
buttonFG = "#EEF5FF"
itemBG = "#285d69"
listBG = "#55adad"
listFG = "white"

path = "C:\\Users\\timur\\PycharmProjects\\NotesAppStorage"
os.chdir(path)

def saveNote(text, name):
    newText = text.get("1.0", "end-1c")
    file_path = f"{path}\\{name}.txt"
    with open(file_path, "w") as f:
        f.write(newText)
        f.close()

def open_notes(name):
    newWindow = tk.Toplevel(window)
    newWindow.title(name)
    newWindow.state("zoomed")
    file_path = f"{path}\\{name}.txt"

    notesText = tk.Text(newWindow, background="red",height=20, width=40)
    notesText.pack()
    saveButton = tk.Button(newWindow, command=lambda: saveNote(notesText, name),
                           text="Save", background="blue", width=10, height=5,
                           font=("Comic Sans", 10),
                           fg="#EEF5FF", bg="#B4D4FF",
                           activeforeground="#EEF5FF", activebackground="#B4D4FF", padx=4,)
    saveButton.pack()

    with open(file_path, "r") as f:
        notesText.insert(tk.END, f.read())

def addNote(listbox, entry):
    fileName = entry.get()
    if(fileName != "" and fileName+".txt" not in os.listdir()):
        listbox.insert(tk.END, fileName)
        listbox.itemconfig(tk.END, {'bg': '#285d69'})
        open(fileName+".txt", "x")

def deleteNote(listbox):
    if (len(listbox.curselection()) != 0):
        index = int(listbox.curselection()[0])
        value = listbox.get(index)
        os.remove(value+".txt")
        listbox.delete(listbox.get(0, tk.END).index(value))

def onselect(listbox):
    w = listbox.widget
    if(len(w.curselection()) != 0):
        index = int(w.curselection()[0])
        value = w.get(index)
        open_notes(value)

nameEntry = tk.Entry(frameOther, font=("Ariel",35))
nameEntry.grid(row=0, column=2, sticky = tk.W, padx=4, pady=2)

scroller = tk.Scrollbar(frameList, width=60)
scroller.pack(side=tk.RIGHT,fill=tk.Y )

notesList = tk.Listbox(frameList, yscrollcommand = scroller.set,  font=("Comic Sans", 20), bg=listBG, fg=listFG)
notesList.pack(side=tk.TOP, fill = tk.BOTH, expand=True )
notesList.bind("<Double-Button>", onselect)
notesList.bind("<Delete>", lambda x : deleteNote(notesList))
window.bind("<Return>", lambda x : addNote(notesList, nameEntry))

scroller.config(command = notesList.yview )

addButton = tk.Button(frameOther, text="New Note", width=10, height=5,
                    command= lambda : addNote(notesList, nameEntry),
                    font=("Comic Sans", 10),
                    fg=buttonFG, bg=buttonBG,
                    activeforeground=buttonFG, activebackground=buttonBG)
addButton.grid(row=0, column=0, sticky = tk.W, padx=4, pady=2)

deleteButton = tk.Button(frameOther, text="Delete Note", width=10, height=5,
                    command= lambda : deleteNote(notesList),
                    font=("Comic Sans", 10),
                    fg=buttonFG, bg=buttonBG,
                    activeforeground=buttonFG, activebackground=buttonBG)
deleteButton.grid(row=0, column=1, sticky = tk.W, padx=4, pady=2)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\\{file}"
        notesList.insert(tk.END, file.rstrip(".txt"))
        notesList.itemconfig(tk.END, {"bg": itemBG})
#        with open(file_path, "r") as f:
#            print(f.read())
#       print(file)

ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()