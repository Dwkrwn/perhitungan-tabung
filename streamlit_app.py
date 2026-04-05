import streamlit as st

st.title("Menghitung Volume :blue[Tabung] :sunglasses:")

r = st.number_input("Masukan Jari-Jari (cm):",0)
t = st.number_input("Masukan Tinggi (cm)", 0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi(r**2)*t
  st.success(f"Volume Tabung adalah {v:.2f}")
