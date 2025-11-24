1.	CODE untuk di Github.com pada app.py, bisa copy kode warna kuning dibawah ini.
import streamlit as st
import pandas as pd
import plotly.express as px
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key securely
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("🚨 API Key is missing! Set it in Streamlit Secrets or a .env file.")
    st.stop()

# Streamlit App UI
st.set_page_config(page_title="Budget vs. Actuals AI", page_icon="📊", layout="wide")
st.title("📊 Budget vs. Actuals AI – Variance Analysis & Commentary")
st.write("Upload your Budget vs. Actuals file and get AI-driven financial insights!")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your dataset (Excel format)", type=["xlsx"])

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Check for required columns
    required_columns = ["Category", "Budget", "Actual"]
    if not all(col in df.columns for col in required_columns):
        st.error("⚠️ The uploaded file must contain 'Category', 'Budget', and 'Actual' columns!")
        st.stop()

    # Calculate Variance and Variance Percentage
    df["Variance"] = df["Actual"] - df["Budget"]
    df["Variance %"] = (df["Variance"] / df["Budget"]) * 100

    # Display data preview
    st.subheader("📊 Data Preview with Variance Calculation")
    st.dataframe(df)

    # Plot Variance Analysis
    st.subheader("📈 Budget vs. Actual Variance Analysis")
    
    fig_bar = px.bar(
        df,
        x="Category",
        y="Variance",
        color="Variance",
        title="📊 Variance by Category",
        text_auto=".2s",
        color_continuous_scale=["red", "yellow", "green"],
    )
    st.plotly_chart(fig_bar)

    fig_line = px.line(
        df,
        x="Category",
        y=["Budget", "Actual"],
        markers=True,
        title="📉 Budget vs. Actual Performance",
    )
    st.plotly_chart(fig_line)

    # AI Section
    st.subheader("🤖 AI-Powered Variance Analysis")

    # AI Summary of Variance Data
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI financial analyst providing variance analysis insights on budget vs. actuals."},
            {"role": "user", "content": f"Here is the budget vs. actual variance summary:\n{df.to_string()}\nWhat are the key insights and recommendations?"}
        ],
        model="llama-3.1-8b-instant",
    )

    st.write(response.choices[0].message.content)

    # AI Chat - Users Can Ask Questions
    st.subheader("🗣️ Chat with AI About Variance Analysis")

    user_query = st.text_input("🔍 Ask the AI about your variance data:")
    if user_query:
        chat_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an AI financial analyst helping users understand their budget vs. actual variance analysis."},
                {"role": "user", "content": f"Variance Data:\n{df.to_string()}\n{user_query}"}
            ],
            model="llama-3.1-8b-instant",
        )
        st.write(chat_response.choices[0].message.content)

Catatan: untuk mengganti model bisa pilih model di link Supported Models - GroqDocs (https://console.groq.com/docs/models)

Bisa copy di Modeli ID dan copy di atas yang warna hijau kodenya.
 






2.	CODE untuk di Github.com pada requiements.txt, bisa copy kode warna kuning dibawah ini.

streamlit
pandas
plotly
groq
python-dotenv
openpyxl

















PROMPT AI NYA untuk di Chat GPT

Saya ingin Anda membuat aplikasi Streamlit berbasis Python untuk analisis Budget vs. Actual.

Spesifikasi detail:
1. Aplikasi memiliki UI dengan judul *Budget vs. Actuals AI – Variance Analysis & Commentary"*.
2. User dapat mengunggah file Excel (.xlsx) dengan kolom wajib: **Category, Budget, Actual**.
3. Aplikasi harus menghitung:
   - Variance = Actual - Budget
   - Variance % = (Variance / Budget) * 100
4. Aplikasi menampilkan preview dataframe setelah dihitung.
5. Buat dua grafik interaktif menggunakan **Plotly**:
   - Bar chart (Variance by Category, dengan warna merah–kuning–hijau).
   - Line chart (Budget vs Actual, per Category).
6. Tambahkan integrasi **Groq API**:
   - Import: `from groq import Groq`
   - API Key di-load aman lewat `.env` (`dotenv`).
   - Bagian pertama: AI langsung memberi summary insights & rekomendasi atas variance.
   - Bagian kedua: user bisa bertanya (text input) dan AI menjawab berdasarkan data variance.
7. Model yang digunakan: **llama-3.1-8b-instant**.

Buatkan kode Python lengkap (`app.py`) dengan struktur rapi dan komentar penjelasan.









