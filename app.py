import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

st.title("Car Horsepower Viewer by Brand")

# Load the dataset with error handling
try:
    df = pd.read_csv("CARS.csv")
except FileNotFoundError:
    st.error("❌ Error: The file 'Cars.csv' was not found. Please make sure it is in the same folder as this script.")
    st.stop()

brands = sorted(df['Make'].dropna().unique())
selected_brand = st.selectbox("Enter Brand Name:", brands)
filtered_df = df[df['Make'] == selected_brand]

st.write(f"Filtered data for **{selected_brand}**:")
st.write(filtered_df)

fig, ax = plt.subplots(figsize=(8, 5))
sb.barplot(x=filtered_df.Make, y=filtered_df.Horsepower, ax=ax)
plt.xticks(rotation=90)
ax.set_title(f"Horsepower for {selected_brand}")
st.pyplot(fig)
