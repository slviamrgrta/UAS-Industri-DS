import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="WebApps", layout="wide")

if "to_analisis" not in st.session_state:
    st.session_state.to_analisis = False
if "about" not in st.session_state:
    st.session_state.about = False

# Tambahkan font Poppins melalui Google Fonts
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    .stApp {
        background: #f9f9f9 !important;
        font-family: 'Poppins', sans-serif;
        font-size: 15px
    }
    .custom-navbar {
        display: flex;
        justify-content: flex-start;
        gap: 90px;
        padding: 10px 20px;
        color:black;
    }
    .navbar-link {
        font-size: 18px;
        font-weight: 400;
        color: black !important;
        text-decoration: underline;
        cursor: pointer;
        font-family: 'Poppins', sans-serif;
    }
    .navbar-link:hover {
        color: #1E3A8A;
        text-decoration: none;
    }
    .custom-navbar {
    display: flex;
    justify-content: flex-start;
    gap: 90px;
    padding: 10px 20px;
    color: black;
    border-bottom: 2px solid #1E90FF; /* Menambahkan garis pembatas di bawah navbar */
    }

    h2 {
        font-size: 65px !important;
        font-weight: bold !important;
        color: #1E3A8A !important;
        margin-bottom: 15px; /* Jarak di bawah judul utama */
    }
    h3 {
        font-size: 30px !important; /* Ukuran subjudul */
        font-family: Poppins;
        font-weight: 400 !important; /* Ketebalan font */
        color: #333333 !important; /* Warna subjudul */
        margin-top: 10px !important; /* Margin atas */
        margin-bottom: 50px !important; /* Margin bawah */
    }
    p{
        font-size: 15px !important;
        font-weight: 300 !important;
    }
    button {
        font-family: 'Poppins', sans-serif;
        font-weight: bold !important;
    }
    .custom-button {
        background-color: #1E3A8A;
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: bold !important;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 20px;
    }
    .custom-button:hover {
        background-color: #fffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def load_beranda():
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)

    # Membuat layout dengan teks di kiri dan gambar di kanan
    col1, spacer, col2 = st.columns([2, 0.001, 1.5])  # Lebih banyak ruang untuk teks (kiri)

    with col1:
        st.markdown("""
            <h2>Transformasikan Data Anda Menjadi Wawasan Berharga</h2>
            <h3>Analisis sentimen data dengan cepat untuk keputusan yang lebih cerdas dan strategis.</h3>
        """, unsafe_allow_html=True)

        # Tombol di tengah teks dengan warna merah menggunakan st.button
        _, button_col, _ = st.columns([2, 3, 1])  # Kolom untuk memusatkan tombol
        with button_col:
            if st.button("Mulai Analisis", key="start_analysis"):
                st.session_state.to_analisis = True
                st.session_state.about = False

    with col2:
        st.image("C:\\Semester 5\\Industri Sains Data\\Project UAS Industri\\3")  # Gambar dipindahkan ke kolom kanan

    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #154673;
            color: white;
            font-size: 16px;
            font-weight: bold !important;
            padding: 10px 12px;
            border-radius: 5px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #D3D3D3;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_analisis_page():
    analisis_path = os.path.join("menus", "analisis.py")  # Lokasi file analisis.py
    if os.path.exists(analisis_path):
        spec = importlib.util.spec_from_file_location("menus.analisis", analisis_path)
        analisis = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(analisis)
        analisis.main()  # Pastikan ada fungsi main() di analisis.py
    else:
        st.error("Halaman analisis tidak ditemukan. Pastikan file analisis.py berada di dalam folder menus.")

# Navbar
def top_navbar():
    st.markdown(
        """
        <style>
        .e1f1d6gn5 {
            position: relative;
            z-index: 10;
        }
        .custom-navbar {
        display: flex;
        justify-content: flex-start;
        gap: 90px;
        padding: 10px 20px;
        color: black;
        border-bottom: 2px solid #1E90FF; /* Garis pembatas di bawah navbar */
        }
        .stTooltipHoverTarget button {
            background-color: transparent;
            border-color: transparent;
            color: black;
        }
        .stTooltipHoverTarget button:hover {
            border-color: transparent;
            background-color: #B17BAC;
            color: white;
        }
        .st-emotion-cache-1jicfl2 {
            width: 100%;
            padding: 2.5rem;
        }
        .e1f1d6gn3 {
            display: block !important;
            position: relative;
            z-index: 10;
            justify-content: center;
        }
        @media (min-width: 576px) {
            .st-emotion-cache-7tauuy {
                padding-left: 5rem;
                padding-right: 5rem;
            }
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # Mengatur proporsi kolom lebih kecil agar tombol lebih rapat
    col1, col2, col3, col4 = st.columns([1, 1, 1.05, 7])  # Kurangi proporsi kolom kanan

    with col1:
        if st.button("🏠 Beranda", key="beranda_btn"):
            st.session_state.to_analisis = False
            st.session_state.about = False

    with col2:
        if st.button("📊 Analisis", key="analisis_btn"):
            st.session_state.to_analisis = True
            st.session_state.about = False
    
    # Menambahkan style untuk navbar
    st.markdown(
        """
        <style>
        div.stButton > custom-button {
            background-color: transparent;
            color: black;
            font-size: 16px;
            font-weight:bold !important;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        div.stButton > custom-button:hover {
            background-color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Fungsi utama
def main():
    top_navbar()

    if st.session_state.to_analisis:
        load_analisis_page()
    else:
        load_beranda()


main()

