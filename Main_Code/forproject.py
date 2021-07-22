import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=400, bg="#060A04")
canvas.pack()
folders_all = []
files_all = []
show_on_widget=[]

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.85, relx=0.1, rely=0.05)

def select_folder():
    for widget in frame.winfo_children():
        widget.destroy()
    folder_selected = filedialog.askdirectory()
    folders_all.append(folder_selected)
    show_on_widget.append(folder_selected.split('/')[-1]+" folder")
    for app in show_on_widget:
        # for app in files_all:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def select_file():
    for widget in frame.winfo_children():
        widget.destroy()
    # for widget in frame.winfo_children():
    #     widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("text files", "txt"),))
    files_all.append(filename)
    show_on_widget.append(filename.split("/")[-1])
    for app in show_on_widget:
    # for app in files_all:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def start_code():
    from final import plagcheck
    print("yo")

    x = plagcheck(folders_all, files_all)
    x.run()


openFile = tk.Button(root, text="Select folder", padx=15,
                     pady=5, fg="#030600", bg="#C4C8C3", command=select_folder)
# openFile.pack(side = tkinter.BOTTOM)
openFile.place(x=50, y=460)
runFile = tk.Button(root, text="Select file", padx=10,
                    pady=5, fg="#030600", bg="#C4C8C3", command=select_file)
# runFile.pack(side = tkinter.BOTTOM)
runFile.place(x=170, y=460)

startFile = tk.Button(root, text="Start Code", padx=10,
                      pady=5, fg="#030600", bg="#C4C8C3", command=start_code)
# startFile.pack(side = tkinter.BOTTOM)
startFile.place(x=260, y=460)

# tester = tk.Button(frame, text="Ok", padx=10,
#                    pady=5, fg="#C4C8C3", bg="#060A04")
# tester.place(x=50,y=50)
root.mainloop()
