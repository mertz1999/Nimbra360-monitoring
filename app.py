import streamlit as st
from base import Base
import pandas as pd
import numpy as np
import datetime

# Instance of our scrapper system
core = Base()

# Config streamlit window
st.set_page_config(
    page_title="Nimbra Scrapper",
    page_icon="👋",
    layout="wide"
)

# Scrap CallBackfunction
def scrap(today, yesterday, stations):
    prog_bar = st.progress(0)
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    today_date     = f'{today.day} {months[today.month]} {today.year}'
    yesterday_date = f'{yesterday.day} {months[yesterday.month]} {yesterday.year}'
    core.start(today_date=today_date, yesterday_date=yesterday_date, stations=stations, prog_bar=prog_bar)
    prog_bar.empty()


# st.markdown("""
#             # <div align="center">Scrap Nimbra now</div>  
#             """, unsafe_allow_html=True)


# A form on sidebar
with st.sidebar.form("Inputs:"):
    st.markdown("## Inputs:")

    # Get date of today and yesterday
    today = datetime.datetime.today()
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)

    # make time input
    d = st.date_input(
    "Today:",
    datetime.date(today.year, today.month, today.day)
    )
    d2 = st.date_input(
    "Yesterday:",
    datetime.date(yesterday.year, yesterday.month, yesterday.day)
    )

    # Stations
    stations = st.multiselect( 'Select stations:',
                          ('Tabas', 'Ghaen', 'Abiz'),
                          ('Tabas', 'Ghaen', 'Abiz'))
    
    submitted = st.form_submit_button("Start!",on_click=scrap, args=(d,d2,stations))
    if submitted:
        st.session_state['data'] = {
            'today' : d,
            'yesterday' : d2,
            'stations' : stations
        }



# Make container to write information from Nimbra
info_container = st.container()

information_data = np.array(
    [['Tabas', '25 °C', "✅/✅", "✅", "0 4 0 0","0 0 0 0","0 0 0 0","0 0 0 0","0 4 0 0","0 0 0 0"]]
)

data = pd.DataFrame(
    information_data,
    columns=('Station', 
             '🌡️ Temprature', 
             '📡​ DTM(RX/TX)', 
             '🚨 Alarm', 
             '📮 Trunk ES', '📮 Trunk SES', '📮 Trunk UAS', '📮 Trunk SS',
             '🧰​ TS0 (ES SES BBE UAS)',
             '🧰​ TS1 (ES SES BBE UAS)',
            )
)
data.set_index("Station", inplace = True)

st.dataframe(data)
