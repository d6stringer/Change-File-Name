import os
import tkinter.messagebox
import tkinter as tk
from tkinter import filedialog, ttk, IntVar

def get_dir():
    global path
    path = filedialog.askdirectory()
    dir_label['text'] = path
    return

def change_name(number):
    # global path
    try:
        for file in os.listdir(path):
            old_fn = path + "/" + file
            new_fn = path + "/" + file[0:18] + ' - ' + str(number) + ".pdf"
            os.rename(old_fn, new_fn)
            number += 1
    except:
        pass
    finally:
        global status
        status = 1
        root.update_idletasks()


path = ''
status = 0
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Change File Names')
    btn1 = tk.Button(root,
                     text='Select Folder',
                     command=get_dir)
    btn1.grid(row=0, column=0, pady=10)
    dir_label = ttk.Label(root,
                          text=path)
    dir_label.grid(row=1, column=0, pady=10)
    start = IntVar()

    l_e1 = tk.Label(root,
                    text="Starting Number")
    l_e1.grid(row=2, column=0)
    e1 = tk.Entry(root)
    e1.grid(row=2, column=1)

    btn2 = tk.Button(root,
                     text='Change',
                     command= lambda: change_name(int(e1.get())))
    btn2.grid(row=3, column=1, pady=10)

    if status:
        done_label = tk.Label(root,
                              text="Done!")
        done_label.grid(row=4, column=0)

    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/