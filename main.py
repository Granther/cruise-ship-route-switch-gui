from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
import time

from ping import *
from config import Config, RouteProfile
from log import Log
from utils import Utils
from tel import Tel

config = Config()
#utils = Utils(config=config)
log = Log('main')
tel = Tel(config.switch_ip, config.switch_usr, config.switch_pass, config.user_prompt, config.pass_prompt)

root = Tk()
root.geometry("200x200")
root.title('Grants Route Switcher')

x_col = 0
y_start = 80
y_inc = 40
n_buttons = 0

#button_label = Label(root, text='Route S')
#button_label.place(x=x_col, y=2)

for route in config.routes:
    print(route.validation_list)
    ttk.Button(text=route.name, command=lambda route=route: tel.send_command(route.command_list, route.validation_list)).place(x=x_col, y=(y_start + (y_inc * n_buttons)))
    n_buttons += 1


ttk.Button(text="Quit", command=lambda: root.destroy()).place(x=x_col, y=20)
# ttk.Button(text="Starlink", command=lambda: tel.starlink()).place(x=x_col, y=100)
# ttk.Button(text="AT&T", command=lambda: tel.att()).place(x=x_col, y=160)

# status_label = Label(root, text='Status')
# status_label.place(x=450, y=2)

# def ping_loop():
#     tag = ''

#     ping_textbox.config(state=tk.NORMAL)

#     ping_result = 999

#     try:
#         ping_result = ping(config.host_to_ping, timeout=0.1)
#     except PingException:
#         pass
#     except Exception as e:
#         pass

#     if ping_result < config.green_ping_threshold:
#         tag = 'good_lat'
#     elif ping_result < config.yellow_ping_threshold:
#         tag = 'mid_lat'
#     else:
#         tag = 'high_lat'

#     ping_textbox.insert(tk.INSERT, str(ping_result) + ' ms \n', tag)
    
#     if int(ping_textbox.index('end-1c').split('.')[0]) > 20:
#         ping_textbox.delete("1.0", "2.0")

#     ping_textbox.config(state=tk.DISABLED)
#     root.after(config.ping_interval, ping_loop)

# root.after(config.ping_interval, ping_loop)
#root.after(config.periodic_check_interval, periodic_check)

root.mainloop()