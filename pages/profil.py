import streamlit as st

st.set_page_config(
    page_title="syauqie.profil | Portfolio",
    page_icon="👤",
    layout="wide"
)

# =========================================
# DATA PROFIL
# =========================================
nama = "Muhammad Syauqie Alfa Iliyyin"
prodi = "Sistem Informasi"
hobi = ["Mendengarkan musik", "Bermain game"]
motto = "Still growing, never settling."
minat = ["Web Development", "Data Analytics", "Artificial Intelligence"]


# =========================================
# FUNGSI BANTU
# =========================================
def chips(items):
    return "".join(
        f"<span style='display:inline-block; margin:0 0.5rem 0.5rem 0; "
        f"padding:0.35rem 0.9rem; border-radius:999px; font-size:0.95rem; "
        f"background:rgba(94,165,255,0.15); color:#9cc8ff; "
        f"border:1px solid rgba(94,165,255,0.35);'>{item}</span>"
        for item in items
    )


# =========================================
# HALAMAN PROFIL
# =========================================
st.caption("GET TO KNOW ME")
st.title("👤 Profil")

kiri, kanan = st.columns([1, 2], gap="medium")

with kiri:
    st.image("images/1.jpeg", use_container_width=True)

with kanan:
    st.caption("NAMA LENGKAP")
    st.header(nama)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.container(border=True):
            st.caption("🎓 PROGRAM STUDI")
            st.subheader(prodi)

    with col2:
        with st.container(border=True):
            st.caption("🎯 HOBI")
            st.markdown(chips(hobi), unsafe_allow_html=True)

    with st.container(border=True):
        st.caption("💬 MOTTO HIDUP")
        st.subheader(f"“{motto}”")

    with st.container(border=True):
        st.caption("🔬 MINAT KEILMUAN")
        st.markdown(chips(minat), unsafe_allow_html=True)

# ---------- NAVIGASI ANTAR HALAMAN ----------
st.divider()
kiri_nav, kosong, kanan_nav = st.columns([1.2, 5, 1.8])

with kiri_nav:
    if st.button("← Home", key="profil_home", use_container_width=True):
        st.switch_page(st.session_state["home_page"])

with kanan_nav:
    if st.button("Sosial Media →", key="profil_next", use_container_width=True):
        st.switch_page("pages/sosial_media.py")
