import tkinter as tk
from tkinter import messagebox
import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_process():
    for proc in u.process_iter(['pid', 'name']):
        if proc.info['name'] == 'LeagueClient':
            return True
    return False

def mac_ranked_name_exploit():
    if not check_process():
        messagebox.showerror("Error", "Client not running")
        return "e"
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient'  and 'LeagueClientUx' not in i.cmdline()]
    e=list(r.get(url=f'https://127.0.0.1:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

def windows_ranked_name_exploit():
    if not check_process():
        messagebox.showerror("Error", "Client not running")
        return "e"
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient.exe' not in i.cmdline()]
    e=list(r.get(url=f'https://127.0.0.1:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ranked Name Exploit")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.mac_button = tk.Button(self, text="Get Ranked Names (Mac)", command=self.mac_button_clicked)
        self.mac_button.pack()
        self.windows_button = tk.Button(self, text="Get Ranked Names (Windows)", command=self.windows_button_clicked)
        self.windows_button.pack()

    def mac_button_clicked(self):
        ranked_names = mac_ranked_name_exploit()
        if ranked_names == "e":
            return
        for i in ranked_names:
            messagebox.showinfo("Ranked Names", i['name'])
    
    def windows_button_clicked(self):
        ranked_names = windows_ranked_name_exploit()
        if ranked_names == "e":
            return
        for i in ranked_names:
            messagebox.showinfo("Ranked Names", i['name'])

if __name__ == "__main__":
    app = App()
    app.mainloop()