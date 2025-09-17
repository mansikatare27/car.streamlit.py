import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../Datasets/Cars.csv")
    return df

df = load_data()

st.title("Car Brand Horsepower Visualization")

# Show the unique car brands
brands = df['Make'].unique()
selected_brand = st.selectbox("Select a Car Brand", sorted(brands))

# Filter the DataFrame for the selected brand
filtered_df = df[df['Make'] == selected_brand]

# Check if there are any records for the selected brand
if filtered_df.empty:
    st.warning("No data available for the selected brand.")
else:
    # Create a barplot using Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=filtered_df, x="Make", y="Horsepower", ax=ax)
    ax.set_title(f"Horsepower of {selected_brand} Cars")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Horsepower")
    plt.xticks(rotation=90)
    st.pyplot(fig)
