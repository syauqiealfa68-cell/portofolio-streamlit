import streamlit as st

st.set_page_config(
    page_title="syauqie.sosmed | Portfolio",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Sosial Media")
st.write("Temukan dan hubungi saya melalui platform berikut.")

sosmed = [
    ("📸 Instagram", "@sawqeee_", "https://www.instagram.com/sawqeee_/", "Kunjungi ↗"),
    ("✉️ Email", "syauqiealfa98@gmail.com", "mailto:syauqiealfa98@gmail.com", "Kirim Email ↗")
]

cols = st.columns(2)
for col, (name, username, link, label) in zip(cols, sosmed):
    with col:
        with st.container(border=True):
            st.subheader(name)
            st.caption(username)
            st.link_button(label, link)

# ---------- NAVIGASI ANTAR HALAMAN ----------
st.divider()
kiri_nav,kosong, tengah_nav,kosong, kanan_nav = st.columns([1.3, 3.5, 1.2, 3, 1.8])

with kiri_nav:
    if st.button("← Profil", key="sosial_prev", use_container_width=True):
        st.switch_page("pages/profil.py")

with tengah_nav:
    if st.button("⌂ Home", key="sosial_home", use_container_width=True):
        st.switch_page(st.session_state["home_page"])

with kanan_nav:
    if st.button("Kemampuan →", key="sosial_next", use_container_width=True):
        st.switch_page("pages/kemampuan.py")