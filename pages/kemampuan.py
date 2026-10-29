import streamlit as st

st.set_page_config(
    page_title="syauqie.skills | Portfolio",
    page_icon="⚡",
    layout="wide"
)

st.title("📊 Kemampuan")
st.write("Kemampuan yang terus saya kembangkan.")

for skill, value in [
    ("Adaptability", 80),
    ("Python", 40),
    ("Discipline", 75),
    ("Streamlit", 30),
    ("Responsibility",75)
]:
    st.write(skill)
    st.progress(value)
    st.caption(f"{value}%")

# ---------- NAVIGASI ANTAR HALAMAN ----------
st.divider()
kiri_nav, kosong, kanan_nav = st.columns([1.2, 5, 1.8])

with kiri_nav:
    if st.button("← Sosial Media", key="kemampuan_prev", use_container_width=True):
        st.switch_page("pages/sosial_media.py")

with kanan_nav:
    if st.button("⌂ Home", key="kemampuan_home", use_container_width=True):
        st.switch_page(st.session_state["home_page"])
