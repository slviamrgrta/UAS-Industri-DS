import streamlit as st
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# CSS styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    .stApp {
        background-color: #f9f9f9;
        font-family: 'Poppins', sans-serif;
    }

    h7, h8, h9, h10, h11 {
        font-family: 'Poppins', sans-serif;
        color: #1E3A8A;
        margin-bottom: 10px; /* Jarak antar judul lebih kecil */
    }
    h12{
        font-family: 'Poppins', sans-serif;
        color: #1E3A8A;
        margin-bottom: 10px; /* Jarak antar judul lebih kecil */
    }

    p1 {
        font-size: 14px; /* Ukuran lebih kecil */
        color: #555555;
        margin: 10px 0; /* Jarak antar paragraf lebih kecil */
    }

    .divider {
        margin: 10px 0; /* Jarak antar bagian lebih kecil */
        border-top: 1px solid #ddd;
    }

    .file-upload-label {
        font-size: 14px;
        color: #1E3A8A;
        font-family: 'Poppins', sans-serif;
    }

    .flex-container {
        display: flex;
    }

    .flex-item {
        flex: 1;
    }

    .center-title {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 40px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 10px;
    }

    .custom-label {
        font-size: 18px !important; /* Ukuran label lebih besar */
        font-weight: 300 !important; /* Tebal */
        color: black; /* Warna biru */
        margin-bottom: 10px; /* Jarak ke input */
        font-family: 'Poppins', sans-serif;
    }

    div.stButton > button {
        background-color: #154673;
        color: white;
        font-size: 14px;
        font-weight: bold !important;
        padding: 8px 16px; /* Tombol lebih kecil */
        border-radius: 4px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #D3D3D3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load model
MODEL_DIR = "model/models"

@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    return model, tokenizer

# Predict sentiment
def predict_sentiment(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    sentiment_mapping = {0: 'Negatif', 1: 'Netral', 2: 'Positif'}
    return sentiment_mapping.get(predicted_label, "Tidak Diketahui")

# Halaman analisis
def main():
    st.markdown("<div class='center-title'>Halaman Analisis Sentimen</div>", unsafe_allow_html=True)
    
    # Custom label sebelum input
    st.markdown("<div class='custom-label'>Masukkan kalimat untuk analisis:</div>", unsafe_allow_html=True)
    user_input = st.text_area("", placeholder="Masukkan kalimat...")
    
    if st.button("Cek Sentimen"):
        if user_input.strip():
            model, tokenizer = load_model()
            result = predict_sentiment(user_input, model, tokenizer)
            st.write(f"**Hasil Sentimen:** {result}")
        else:
            st.warning("Masukkan kalimat untuk dianalisis.")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("<div class='custom-label'>Analisis Sentimen:</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload file CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah!")
        st.dataframe(df, height=300)

        column_name = st.selectbox("Pilih kolom teks:", options=df.columns)
        if st.button("Analisis CSV"):
            model, tokenizer = load_model()
            df["Sentiment"] = df[column_name].apply(lambda x: predict_sentiment(x, model, tokenizer))
            st.success("Analisis selesai!")
            st.dataframe(df, height=300)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Unduh Hasil", data=csv, file_name="hasil_sentimen.csv")

    if st.button("Kembali ke Beranda"):
        st.session_state.current_page = "Home"
