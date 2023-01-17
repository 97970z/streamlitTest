import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import clipboard
import streamlit as st
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def mac_ranked_name_exploit():
    if not any(i.name() == 'LeagueClient' for i in u.process_iter()):
        st.error("롤 클라이언트가 실행되어 있지 않습니다.", icon="❌")
        return "e"
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient'  and 'LeagueClientUx' not in i.cmdline()]
    e=list(r.get(url=f'https://localhost:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

def windows_ranked_name_exploit():
    if not any(i.name() == 'LeagueClient.exe' for i in u.process_iter()):
        st.error("롤 클라이언트가 실행되어 있지 않습니다.", icon="❌")
        return
    [x]=[[i.cmdline()[1].split('=')[1],i.cmdline()[2].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient.exe' not in i.cmdline()]
    e=list(r.get(url=f'https://localhost:{x[1]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[0]}'.encode()).decode()}",'Accept': 'application/json'},verify=False).json()['participants'])
    return e

if __name__ == '__main__':
    st.title("Ranked Name Exploit")
    tab3, tab1, tab2 = st.tabs(["사용방법", "Windows", "MacOS"])

    if o.name == 'posix':
        with tab2:
            if st.button("Get Ranked Names", key="macos"):
                st.success("클립보드에 복사되었습니다.")
                for i in mac_ranked_name_exploit():
                    if i == "e":
                        break
                    st.subheader(i['name'])
            with tab3:
                st.subheader("사용방법")
                st.markdown("1. 리그오브레전드를 실행합니다.")
                st.markdown("2. 랭크게임 픽 창에 진입합니다.")
                st.markdown("3. 자신의 운영체제에 맞는 탭을 클릭합니다. (Windows/MacOS)")
                st.markdown("4. Get Ranked Names 버튼을 클릭하면 닉네임이 나타납니다.")
                st.markdown("⚠️  닉네임은 픽 순서가 아닙니다 ⚠️")
    elif o.name == 'nt':
        with tab1:
            if st.button("Get Ranked Names", key="windows"):
                st.success("클립보드에 복사되었습니다.")
                for i in windows_ranked_name_exploit():
                    if i == "e":
                        break
                    st.subheader(i['name'])