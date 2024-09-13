import streamlit as st

st.write(os.getcwd())  # Cek direktori kerja saat ini
st.write(sys.path)

from var import *

new_x = x
new_y = y

total = new_x + new_y
st.write("Hello world!")
st.write(total)
