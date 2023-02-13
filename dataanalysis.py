# Import the necessary libraries
import streamlit as st
import pandas as pd
import pandas_profiling
import plotly.express as px

# Load the data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Create the main app
def main():
    # Load the data
    file_path = st.file_uploader("Upload your data file", type=["csv"])
    if file_path is not None:
        data = load_data(file_path)
        
        # Generate the profile report
        profile = pandas_profiling.ProfileReport(data)
        
        # Display the profile report
        st.write("## Profile Report")
        st.write(profile)
        
        # Display a scatter plot
        st.write("## Scatter Plot")
        st.write(px.scatter(data, x="column1", y="column2"))
        
# Run the app
if __name__ == "__main__":
    main()
