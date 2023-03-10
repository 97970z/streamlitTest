import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import streamlit as st
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_process():
    for proc in u.process_iter(['pid', 'name']):
        if proc.info['name'] == 'LeagueClient':
            return True
    return False

def mac_ranked_name_exploit():
    if not check_process():
        st.error("Client not running", icon="❌")
        return "e"
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient'  and 'LeagueClientUx' not in i.cmdline()]
    e=list(r.get(url=f'https://127.0.0.1:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

def windows_ranked_name_exploit():
    if not check_process():
        st.error("Client not running", icon="❌")
        return "e"
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient.exe' not in i.cmdline()]
    e=list(r.get(url=f'https://127.0.0.1:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

if __name__ == '__main__':
    st.title("Ranked Name Exploit")
    tab1, tab2 = st.tabs(["Windows", "MacOS"])

    if o.name == 'posix':
        with tab2:
            if st.button("Get Ranked Names", key="macos"):
                st.success("Successfully got ranked names")
                for i in mac_ranked_name_exploit():
                    if i == "e":
                        break
                    st.subheader(i['name'])
    elif o.name == 'nt':
        with tab1:
            if st.button("Get Ranked Names", key="windows"):
                st.success("Successfully got ranked names")
                for i in windows_ranked_name_exploit():
                    if i == "e":
                        break
                    st.subheader(i['name'])