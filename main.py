import os
import git
import threading

import tkinter as tk

from tkinter import *
from tkinter import filedialog as fd

st = Tk()
st.title('Git-Installer v1.0')
st.config()
st.geometry('450x420')
st.configure(bg='#156475')


setting = {'name': "Git-Installer",
           'version': "1.0",
           'author': "NjProVk",
           'web': "https://njprovk.com"}


btn_ins = None
how_to_delete = None
is_create = 0


def get_inst_t(paths):
    try:
        git.Git(paths).clone(entry.get())
    except git.exc.GitCommandError:
        tk.messagebox.showerror(title='Error install', message='Error download files!\nCheck your link or network!')
        btn_ins["state"] = "normal"


def installers(paths):
    global btn_ins

    btn_ins["state"] = "disabled"
    threading.Thread(target=get_inst_t, args=(paths,)).start()


def callback():
    global how_to_delete, is_create, btn_ins

    paths = fd.askdirectory()
    paths = paths if paths else os.getcwd()
    if not is_create:
        paths_label = Label(
            st,
            text=paths,
            font=('Arial', 15),
            bg='#1b4d3e',
            fg='white'
        )

        paths_label.pack(fill=BOTH, expand=True)
        how_to_delete = paths_label
        is_create = 1
    else:
        how_to_delete.config(text=paths)

    btn_ins = tk.Button(text='Install',
                        command=lambda: installers(paths),
                        highlightcolor='red',
                        font=('Arial', 14),
                        bg="black",
                        fg='white')
    btn_ins.pack(pady=20)


Label(
    st,
    text="Step into the past \nor\n step into the future!\nFree soft",
    font=('Times', 20),
    bg='#156475',
    fg='#fff'
).pack(fill=BOTH, expand=True)

Label(
    st,
    text='\n'.join(list(f"{key}: {setting[key]}" for key in setting)),
    font=('Arial', 13),
    bg='#156475',
    fg='black',
    justify=LEFT
).pack(fill=BOTH, expand=True)

entry = tk.Entry(st, font=('Arial', 13), width=40)
entry.pack(pady=20)

tk.Button(text='Choose a path',
          command=callback,
          font=('Arial', 13),
          bg="black",
          fg='white').pack(fill=tk.X)
tk.mainloop()
