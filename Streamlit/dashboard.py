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
    selected_visualization = st.sidebar.selectbox("Select Visualization", ("Scatter Plot", "Box Plot"))

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

    # Plot heatmap of correlation
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Heatmap of Correlation between Variables in Bike Sharing Dataset (per Day)')
    plt.show()
    #Histogram Distribusi Jumlah Total Rental Sepeda per Hari:
    plt.figure(figsize=(5, 5))
    sns.histplot(day['cnt'], bins=30, kde=True, color='green')
    plt.title('Distribusi Jumlah Total Rental Sepeda per Hari')
    plt.xlabel('Jumlah Total Rental Sepeda')
    plt.ylabel('Frekuensi')
    plt.show()

    #Count Plot Distribusi Jumlah Hari Berdasarkan Musim:
    plt.figure(figsize=(5, 5))
    sns.countplot(x='season', data=day, palette='pastel')
    plt.title('Distribusi Jumlah Hari Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Hari')
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
    plt.show()

    #Box Plot untuk Hubungan antara Hari Libur dan Jumlah Sewa:
    fig = px.box(day, x='holiday', y='cnt', title='Hubungan antara Hari Libur dan Jumlah Sewa')
    fig.update_xaxes(title_text='Hari Libur')
    fig.update_yaxes(title_text='Jumlah Sewa')
    fig.show()

    #Box Plot untuk Hubungan antara Cuaca dan Jumlah Sewa:
    fig = px.box(day, x='weathersit', y='cnt', title='Hubungan antara Cuaca dan Jumlah Sewa')
    fig.update_xaxes(title_text='Cuaca')
    fig.update_yaxes(title_text='Jumlah Sewa')
    fig.show()

    #Scatter Plot antara Suhu dan Jumlah Sewa:
    fig = px.scatter(day, x='temp', y='cnt', title='Scatter Plot antara Suhu dan Jumlah Sewa')
    fig.update_xaxes(title_text='Suhu (Celsius)')
    fig.update_yaxes(title_text='Jumlah Sewa')
    fig.show()


if __name__ == "__main__":
    main()
