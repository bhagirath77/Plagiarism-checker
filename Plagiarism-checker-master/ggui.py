import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
canvas = tk.Canvas(root, height=500, width=350, bg="#263D42")
canvas.pack()

if os.path.isfile('save1.txt'):
    with open('save1.txt', 'r') as f:
        tempApps = f.read()
        temApps = tempApps.split(',')
        apps = [x for x in temApps if x.strip()]
        print(apps)


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"),
                                                     ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.56, relheight=0.8, relx=0.22, rely=0.08)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runFile = tk.Button(root, text="Run File", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)
runFile.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save1.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
