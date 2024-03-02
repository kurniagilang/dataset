import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import plotly.express as px

sns.set(style='dark')

# Load data
@st.cache
def load_data():
    data = pd.read_csv("./data/day.csv")
    return data

# Main function
def main():
    # Load data
    data = load_data()

    # Sidebar
    st.sidebar.title("Bike Sharing Dashboard")
    selected_visualization = st.sidebar.selectbox("Select Visualization", ("Scatter Plot", "Box Plot", "Figure", "Heatmap", "Season Counts"))

    # Main content
    st.title("Bike Sharing Dataset Analysis")

    # Scatter plot
    if selected_visualization == "Scatter Plot":
        st.subheader("Scatter Plot: Temperature vs Total Rentals")
        fig = px.scatter(data, x='temp', y='cnt', title='Temperature vs Total Rentals')
        st.plotly_chart(fig)

    # Box plot
    elif selected_visualization == "Box Plot":
        st.subheader("Box Plot: Weather Situation vs Total Rentals")
        fig = px.box(data, x='weathersit', y='cnt', title='Weather Situation vs Total Rentals')
        st.plotly_chart(fig)
    
    # Figure
    elif selected_visualization == "Figure":
        st.subheader("Figure: Distribusi Jumlah Total Rental Sepeda per Hari")

        # Visualisasi histogram
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.histplot(data['cnt'], bins=30, kde=True, color='green', ax=ax)
        ax.set_title('Distribusi Jumlah Total Rental Sepeda per Hari')
        ax.set_xlabel('Jumlah Total Rental Sepeda')
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)

        # Deskripsi statistik
        cnt_stats = data['cnt'].describe()
        st.write("Deskripsi Statistik untuk Variabel 'cnt':")
        st.write(cnt_stats)

    # Heatmap
    elif selected_visualization == "Heatmap":
        st.subheader("Heatmap: Korelasi antar Variabel dalam Dataset Penyewaan Sepeda (per Hari)")

        # Handling NaN values
        data_cleaned = data.dropna()

        # Hitung matriks korelasi
        correlation_matrix = data_cleaned.corr()

        # Plot heatmap korelasi
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Heatmap of Correlation between Variables in Bike Sharing Dataset (per Day)')
        st.pyplot()

    # Season Counts
    elif selected_visualization == "Season Counts":
        st.subheader("Season Counts: Distribusi Jumlah Hari Berdasarkan Musim")

        # Hitung frekuensi musim
        season_counts = data['season'].value_counts()

        # Plot countplot musim
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.countplot(x='season', data=data, palette='pastel', ax=ax)
        ax.set_title('Distribusi Jumlah Hari Berdasarkan Musim')
        ax.set_xlabel('Musim')
        ax.set_ylabel('Jumlah Hari')
        ax.set_xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
        st.pyplot(fig)

        # Tampilkan tabel frekuensi untuk variabel 'season'
        st.write("Tabel Frekuensi untuk Variabel 'season':")
        st.write(season_counts)

if __name__ == "__main__":
    main()
