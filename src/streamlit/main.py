import numpy as np
import pandas as pd
import streamlit as st

from helper import find_distance
from database import find_hawker

st.title('Hawker Center finder')

st.write("Where are you in singapore?")


# Default: (Macritchie reservoir 1.341896, 103.817418)
lat = st.number_input("latitude", min_value=1.0, max_value=2.0, value=1.340, step=0.005, format="%.3f", key=None, help='Input location in singapore', on_change=None)
lon = st.number_input("longitude", min_value=103.0, max_value=105.0, value=103.800, step=0.005, format="%.3f", key=None, help='Input location in singapore', on_change=None)

for _ in range(5):
    st.text("")

hawkers = list(find_hawker(lat, lon)[:5])

df = pd.DataFrame(
     [[hawker["loc"]["coordinates"][1],hawker["loc"]["coordinates"][0]] for hawker in hawkers],
     columns=['lat', 'lon'])
st.map(df)

for _ in range(5):
    st.text("")

for hawker in hawkers:
    col1, mid, col2 = st.columns([8,2,20])
    with col1:
        st.image(hawker["photourl"], use_column_width='auto')
    with col2:
        st.write(hawker["name"])
        dist = find_distance([lat,lon],[hawker["loc"]["coordinates"][1],hawker["loc"]["coordinates"][0]])
        st.write(f'{dist:.1f} metres')




