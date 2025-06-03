import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EV Dataset Explorer", layout="wide")
st.title("🔌 Electric Vehicle Dataset Explorer")

# Load the dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO/main/ElectricCarData_Clean.csv"
    df = pd.read_csv(url)
    df['FastCharge_KmH'] = pd.to_numeric(df['FastCharge_KmH'].replace('—', None), errors='coerce')
    return df

df = load_data()

# Sidebar - Variable selection
st.sidebar.header("Select Options")
selected_variable = st.sidebar.selectbox("Select a numeric variable to visualize", 
    ['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'FastCharge_KmH', 'Seats', 'PriceEuro'])

# Dataset Overview
st.subheader("Dataset Overview")
st.write("Shape of the dataset:", df.shape)
st.dataframe(df.head())

# Variable Distributions
st.subheader(f"Distribution of {selected_variable}")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.histplot(df[selected_variable], kde=True, ax=ax1, color="skyblue")
ax1.set_title(f"Distribution of {selected_variable}")
st.pyplot(fig1)

# Range vs. Price Scatterplot
st.subheader("Range vs. Price")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x='Range_Km', y='PriceEuro', hue='Brand', ax=ax2)
ax2.set_title("Range (Km) vs Price (Euro)")
st.pyplot(fig2)

# Efficiency by Segment
st.subheader("Efficiency (Wh/Km) by Segment")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x='Segment', y='Efficiency_WhKm', ax=ax3)
ax3.set_title("Efficiency by Segment")
st.pyplot(fig3)

# Acceleration vs Price
st.subheader("Acceleration Time vs. Price")
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x='AccelSec', y='PriceEuro', hue='PowerTrain', ax=ax4)
ax4.set_title("Acceleration Time vs Price")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name] | Data Source: ElectricCarData_Clean.csv")
