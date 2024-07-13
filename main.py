from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import time

from ping import *
from config import Config, RouteProfile
from log import Log
from utils import Utils
from tel import Tel

config = Config()
log = Log('main')
tel = Tel(config.switch_ip, config.switch_usr, config.switch_pass, config.user_prompt, config.pass_prompt, timeout=2)

root = Tk()
root.geometry("400x200")
root.title('Grants Route Switcher')

x_col = 20
y_start = 80
y_inc = 40
n_buttons = 0

for route in config.routes:
    print(route.validation_list)
    ttk.Button(text=route.name, command=lambda route=route: tel.send_command(route.command_list, route.validation_list)).place(x=x_col, y=(y_start + (y_inc * n_buttons)))
    n_buttons += 1


ttk.Button(text="Quit", command=lambda: root.destroy()).place(x=x_col, y=20)
ttk.Button(text="Config", command=lambda: root.destroy()).place(x=x_col + 100, y=20)

def update_loop():
    Label(root, text='doop').place(x=x_col+320, y=20)
    #color

root.after(2, update_loop)

root.mainloop()