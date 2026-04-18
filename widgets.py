import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Interactive App 🚀")

# ---------------- USER INPUT ----------------
st.header("User Input Section")

name = st.text_input("What is your name?")
age = st.slider("What is your age?", 0, 100, 25)

options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Choose your favourite language:", options)

if name:
    st.success(f"Hello {name}!")
    st.write(f"Age: {age}")
    st.write(f"Favourite language: {choice}")

# ---------------- FILE UPLOADER ----------------
st.header("Upload Dataset 📂")

uploaded_file = st.file_uploader("Upload your dataset (CSV only)", type=["csv"])

if uploaded_file is not None:
    try:
        # Read file
        df = pd.read_csv(uploaded_file)

        # Show success
        st.success("File uploaded successfully!")

        # Show dataset
        st.subheader("📊 Dataset Preview")
        st.dataframe(df)

        # Show basic info
        st.subheader("📈 Basic Statistics")
        st.write(df.describe())

        # Show column names
        st.subheader("📌 Columns")
        st.write(list(df.columns))

        # Missing values
        st.subheader("❗ Missing Values")
        st.write(df.isnull().sum())

        # Column selection
        st.subheader("🔍 Column Analysis")
        column = st.selectbox("Select a column", df.columns)

        if column:
            st.write(f"Value Counts for {column}")
            st.write(df[column].value_counts())

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("Please upload a CSV file to proceed.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with Streamlit ❤️")