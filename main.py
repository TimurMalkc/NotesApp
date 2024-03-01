import tkinter as tk
import ctypes

window = tk.Tk()
window.title("Planner")
window.state("zoomed")
frameList = tk.Frame(window, background="red")
frameList.pack(side=tk.BOTTOM, fill = tk.BOTH, expand=True)
frameOther = tk.Frame(window, background="blue")
frameOther.pack(side=tk.TOP, fill=tk.X, expand=False)

def openWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Not1")
    newWindow.state("zoomed")
    tk.Label(newWindow, text="aa", background="red",height=100, width=40).pack()

def addNote():
    if(nameEntry.get() != ""):
        notesList.insert(tk.END, nameEntry.get())
        notesList.itemconfig(tk.END, {'bg': '#285d69'})

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

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
notesList.bind("<<ListboxSelect>>", onselect)

scroller.config( command = notesList.yview )

ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()