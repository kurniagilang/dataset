import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache
def load_data():
    data = pd.read_csv("day.csv")
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

if __name__ == "__main__":
    main()
