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
    st.sidebar.header("**Gilang Kurnia Mandari**")
    st.sidebar.title("Bike Sharing Dashboard")
    selected_visualization = st.sidebar.selectbox("Select Visualization", ("Show All Plots", "Scatter Plot", "Box Plot (Weather Situation)", "Box Plot (Holiday)","Box Plot (Season)", "Figure", "Season Counts"))

    # Main content
    st.title("Bike Sharing Dataset Analysis :sparkles: :sparkles:")

    # Show all plots in one page
    if selected_visualization == "Show All Plots":
        st.subheader("All Plots")
        
        # Create a grid layout
        col1, col2 = st.columns(2)

        # Scatter plot: Temperature vs Total Rentals (Weekday)
        with col1:
            st.subheader("Scatter Plot: Temperature vs Total Rentals (Weekday)")
            fig_scatter = px.scatter(data, x='temp', y='cnt', color='weekday', title='Temperature vs Total Rentals (Weekday)')
            st.plotly_chart(fig_scatter)

            # Box plot (Weather Situation)
            st.subheader("Box Plot: Weather Situation vs Total Rentals (Weekday)")
            fig_weather = px.box(data, x='weathersit', y='cnt', color='weekday', title='Weather Situation vs Total Rentals (Weekday)')
            st.plotly_chart(fig_weather)

            # Box plot (Holiday)
            st.subheader("Box Plot: Holiday vs Total Rentals (Weekday)")
            fig_holiday = px.box(data, x='holiday', y='cnt', color='weekday', title='Holiday vs Total Rentals (Weekday)')
            st.plotly_chart(fig_holiday)

        with col2:
            # Box plot (Season)
            st.subheader("Box Plot: Season vs Total Rentals (Weekday)")
            fig_season = px.box(data, x='season', y='cnt', color='weekday', title='Season vs Total Rentals (Weekday)')
            fig_season.update_xaxes(title_text='Musim')
            fig_season.update_yaxes(title_text='Jumlah Sewa')
            st.plotly_chart(fig_season)

            # Figure
            st.subheader("Figure: Distribusi Jumlah Total Rental Sepeda per Hari")
            fig_hist, ax_hist = plt.subplots(figsize=(8, 6))  # Ubah ukuran plot
            sns.histplot(data['cnt'], bins=30, kde=True, color='green', ax=ax_hist)
            ax_hist.set_title('Distribusi Jumlah Total Rental Sepeda per Hari')
            ax_hist.set_xlabel('Jumlah Total Rental Sepeda')
            ax_hist.set_ylabel('Frekuensi')
            st.pyplot(fig_hist)

            # Season Counts
            st.subheader("Season Counts: Distribusi Jumlah Hari Berdasarkan Musim")
            fig_count, ax_count = plt.subplots(figsize=(8, 6))  # Ubah ukuran plot
            sns.countplot(x='season', data=data, palette='pastel', ax=ax_count)
            ax_count.set_title('Distribusi Jumlah Hari Berdasarkan Musim')
            ax_count.set_xlabel('Musim')
            ax_count.set_ylabel('Jumlah Hari')
            ax_count.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
            st.pyplot(fig_count)

    else:
        # Individual plots
        if selected_visualization == "Scatter Plot":
            st.subheader("Scatter Plot: Temperature vs Total Rentals (Weekday)")
            fig = px.scatter(data, x='temp', y='cnt', color='weekday', title='Temperature vs Total Rentals (Weekday)')
            st.plotly_chart(fig)

        elif selected_visualization == "Box Plot (Weather Situation)":
            st.subheader("Box Plot: Weather Situation vs Total Rentals (Weekday)")
            fig = px.box(data, x='weathersit', y='cnt', color='weekday', title='Weather Situation vs Total Rentals (Weekday)')
            st.plotly_chart(fig)

        elif selected_visualization == "Box Plot (Holiday)":
            st.subheader("Box Plot: Holiday vs Total Rentals (Weekday)")
            fig = px.box(data, x='holiday', y='cnt', color='weekday', title='Holiday vs Total Rentals (Weekday)')
            st.plotly_chart(fig)

        elif selected_visualization == "Box Plot (Season)":
            st.subheader("Box Plot: Season vs Total Rentals (Weekday)")
            fig = px.box(data, x='season', y='cnt', color='weekday', title='Season vs Total Rentals (Weekday)')
            fig.update_xaxes(title_text='Musim')
            fig.update_yaxes(title_text='Jumlah Sewa')
            st.plotly_chart(fig)

        elif selected_visualization == "Figure":
            st.subheader("Figure: Distribusi Jumlah Total Rental Sepeda per Hari")

            # Visualisasi histogram
            fig, ax = plt.subplots(figsize=(8, 6))  # Ubah ukuran plot
            sns.histplot(data['cnt'], bins=30, kde=True, color='green', ax=ax)
            ax.set_title('Distribusi Jumlah Total Rental Sepeda per Hari')
            ax.set_xlabel('Jumlah Total Rental Sepeda')
            ax.set_ylabel('Frekuensi')
            st.pyplot(fig)

            # Deskripsi statistik
            cnt_stats = data['cnt'].describe()
            st.write("Deskripsi Statistik untuk Variabel 'cnt':")
            st.write(cnt_stats)

        elif selected_visualization == "Season Counts":
            st.subheader("Season Counts: Distribusi Jumlah Hari Berdasarkan Musim")

            # Hitung frekuensi musim
            season_counts = data['season'].value_counts()

            # Plot countplot musim
            fig, ax = plt.subplots(figsize=(8, 6))  # Ubah ukuran plot
            sns.countplot(x='season', data=data, palette='pastel', ax=ax)
            ax.set_title('Distribusi Jumlah Hari Berdasarkan Musim')
            ax.set_xlabel('Musim')
            ax.set_ylabel('Jumlah Hari')
            ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
            st.pyplot(fig)

            # Tampilkan tabel frekuensi untuk variabel 'season'
            st.write("Tabel Frekuensi untuk Variabel 'season':")
            st.write(season_counts)

if __name__ == "__main__":
    main()
