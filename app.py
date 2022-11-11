import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(
    page_title="Nimbra Scrapper",
    page_icon="👋",
    layout="wide"
)


def scrap(today, yesterdat, stations):
    pass


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
                          ('Tabas', 'Ghaen', 'Sarbishe'),
                          ('Tabas', 'Ghaen', 'Sarbishe'))
    
    submitted = st.form_submit_button("Start!",on_click=)
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
# info_container.markdown("***")
# info_container.markdown('#### <div align="center" style="margin-top: -39px;">😱 Tabas</div>', unsafe_allow_html=True)
# info_container.markdown("##### 🌡️​ Temprature: 25 °C")
# info_container.markdown("##### 🚨​ Alarms:")
# info_container.success("CLEARED 123 opoi ooo opo", icon="✅")


# col1, col2, col3 = st.columns(3)

# with col2:
#    st.button('Start scrapping',type='primary')




# d = st.date_input(
#     "When's your birthday",
#     datetime.date(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day))
# st.write('Your birthday is:', d)



# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

