import streamlit as st

# =========================================
# KONFIGURASI
# =========================================
st.set_page_config(
    page_title="syauqie.home | Portfolio",
    page_icon="🏠",
    layout="wide"
)


# =========================================
# STYLE / BACKGROUND (berlaku untuk semua halaman)
# =========================================
st.markdown(
    """
<style>
.stApp {
    background:
        radial-gradient(ellipse 70% 50% at 10% 0%, rgba(94,165,255,0.20), transparent 60%),
        radial-gradient(ellipse 60% 45% at 95% 15%, rgba(130,100,255,0.16), transparent 60%),
        radial-gradient(ellipse 70% 50% at 50% 100%, rgba(40,200,200,0.10), transparent 60%),
        linear-gradient(180deg, #0a1224 0%, #070d1a 100%);
    background-attachment: fixed;
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
    background: rgba(16, 32, 61, 0.55);
    border: 1px solid rgba(120, 160, 220, 0.18);
}
.stButton > button, .stLinkButton > a {
    border-radius: 12px;
    border: 1px solid rgba(120, 160, 220, 0.25);
    background: rgba(16, 32, 61, 0.65);
    transition: all 0.2s ease;
}
.stButton > button:hover, .stLinkButton > a:hover {
    border-color: #5ea5ff;
    box-shadow: 0 0 14px rgba(94, 165, 255, 0.35);
    transform: translateY(-1px);
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #3f8cff, #6a6bff);
    border: none;
}
hr { border-color: rgba(120, 160, 220, 0.18) !important; }
</style>
    """,
    unsafe_allow_html=True
)


# =========================================
# HALAMAN HOME
# =========================================
def home():
    # ---------- HERO ----------
    st.markdown(
        """
<div style="background: linear-gradient(135deg, #10203d 0%, #0a1224 100%);
            border: 1px solid rgba(120,160,220,0.15);
            border-radius: 22px; padding: 3.2rem 3rem; margin-bottom: 2.5rem;">
<div style="color:#6fb1ff; font-size:0.85rem; font-weight:800;
            letter-spacing:0.25em; margin-bottom:1.6rem;">PORTOFOLIO PRIBADI</div>
<div style="color:#f1f6ff; font-size:3.6rem; font-weight:800;
            line-height:1.15; letter-spacing:-0.02em; margin-bottom:2rem;">
Halo, saya <span style="color:#5ea5ff;">Muhammad Syauqie Alfa Iliyyin.</span></div>
<div style="color:#ffffff; font-size:1.15rem; margin-bottom:1rem;">
Mahasiswa yang tertarik pada teknologi, pemrograman, dan pengembangan diri.</div>
<div style="color:#8fa3c4; font-size:1.1rem; line-height:1.9; max-width:900px;">
Selamat datang di website portofolio saya. Di sini kamu bisa mengenal profil,
melihat media sosial, dan mengetahui kemampuan yang sedang saya kembangkan.</div>
</div>
        """,
        unsafe_allow_html=True
    )

    # ---------- JELAJAHI PORTOFOLIO ----------
    st.header("Jelajahi Portofolio")
    st.write("Pilih halaman yang ingin kamu lihat.")

    menu_home = [
        ("👤", "Profil",
         "Kenali saya lebih dekat, mulai dari program studi hingga minat keilmuan.",
         profil_page),
        ("🌐", "Sosial Media",
         "Temukan cara menghubungi dan mengikuti aktivitas saya secara online.",
         sosial_page),
        ("⚡", "Kemampuan",
         "Lihat kemampuan yang saya miliki dan yang sedang saya pelajari.",
         kemampuan_page),
    ]

    cols = st.columns(3, gap="medium")

    for col, (ikon, judul, deskripsi, tujuan) in zip(cols, menu_home):
        with col:
            with st.container(border=True):
                st.markdown(
                    f"<div style='font-size:2.2rem; margin:0.6rem 0 0.8rem;'>{ikon}</div>",
                    unsafe_allow_html=True
                )
                st.subheader(judul)
                st.write(deskripsi)

            if st.button(f"Lihat {judul} →", key=f"home_{judul}", use_container_width=True):
                st.switch_page(tujuan)


# =========================================
# DAFTAR HALAMAN
# =========================================
home_page = st.Page(home, title="Home", default=True)
profil_page = st.Page("pages/profil.py", title="Profil")
sosial_page = st.Page("pages/sosial_media.py", title="Sosial Media")
kemampuan_page = st.Page("pages/kemampuan.py", title="Kemampuan")

# Disimpan agar halaman di folder pages bisa kembali ke Home
st.session_state["home_page"] = home_page

page = st.navigation(
    [home_page, profil_page, sosial_page, kemampuan_page],
    position="hidden"
)


# =========================================
# HEADER WEBSITE
# =========================================
logo, menu, action = st.columns(
    [1.2, 3.5, 1.2],
    vertical_alignment="center"
)

with logo:
    st.subheader("◈ Syauqie")
    st.caption("DIGITAL PORTFOLIO")

with menu:
    home_col, profil_col, sosial_col, kemampuan_col = st.columns(4)

    with home_col:
        if st.button("⌂ Home", key="nav_home", use_container_width=True):
            st.switch_page(home_page)

    with profil_col:
        if st.button("Profil", key="nav_profil", use_container_width=True):
            st.switch_page(profil_page)

    with sosial_col:
        if st.button("✉ Sosial Media", key="nav_sosial", use_container_width=True):
            st.switch_page(sosial_page)

    with kemampuan_col:
        if st.button("▦ Kemampuan", key="nav_kemampuan", use_container_width=True):
            st.switch_page(kemampuan_page)

with action:
    if st.button(
        "Let's Talk ↗",
        key="nav_talk",
        type="primary",
        use_container_width=True
    ):
        st.switch_page(sosial_page)

st.divider()


# =========================================
# TAMPILKAN HALAMAN
# =========================================
page.run()
