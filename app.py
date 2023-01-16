import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import streamlit as st

if __name__ == '__main__':
    if st.button("Get Names"):
        [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient'  and 'LeagueClientUx' not in i.cmdline()]
        print(x)
        e=list(r.get(url=f'https://127.0.0.1:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
        for i in e:
            st.subheader(i['name'])