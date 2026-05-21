import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

st.title("📊 HR Data Cleaning & Attrition Dashboard")
st.write("Welcome to my portfolio project! This interactive dashboard explores employee data and attrition trends.")

@st.cache_data
def load_data():
    return pd.read_csv("hr_cleaned_dataset.csv")

try:
    df = load_data()
    
    if st.checkbox("Show Raw Data Overview"):
        st.write(df.head())
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 Key Metrics")
        st.metric("Total Employees", len(df))
        if 'attrition' in df.columns:
            attrition_rate = (df['attrition'].value_counts(normalize=True).get('Yes', 0)) * 100
            st.metric("Attrition Rate", f"{attrition_rate:.1f}%")

    with col2:
        st.subheader("📈 Monthly Income by Department & Attrition")
        if {"department", "monthlyincome", "attrition"}.issubset(df.columns):
            fig, ax = plt.subplots(figsize=(10, 5))
            
            sns.barplot(data=df, x='department', y='monthlyincome', hue='attrition', palette='Set2', ax=ax)
            
            plt.title('Monthly Income by Department and Attrition', fontsize=12, pad=10)
            plt.xlabel('Department', fontsize=10)
            plt.ylabel('Monthly Income', fontsize=10)
            
            plt.legend(title='Attrition', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            
            st.pyplot(fig)

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Please make sure 'hr_cleaned_dataset.csv' is in the same folder.")