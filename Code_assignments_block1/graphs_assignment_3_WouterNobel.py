import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Suicides in the World", layout="wide", initial_sidebar_state="expanded")


# Load dataset
df = pd.read_csv("C:/Users/woute/Documents/Minor/Assignments/Assignment_3/Suicide_rates.csv") #load the dataset
print(df.head(13))
print(df.dtypes)

# Sidebar filters
st.sidebar.header("Please filter here:") #Make sidebar header

# Gender Selector
gender_selector = st.sidebar.radio(
    "Select Gender",
    ("Both", "male", "female")
)

# Age Group Selector 
age_selector = st.sidebar.multiselect(
    "Select Age Groups",
    options=df["age"].unique(),  # Use the unique age groups from the dataset
    default=df["age"].unique()    # Default to all age groups selected
)

# Measure Selector 
measure_selector = st.sidebar.radio(
    "Select Measure",
    ("Total Suicides", "Suicides per 100k")
)

# Year Slider to choose the year
selected_year = st.sidebar.slider(
    "Select Year", 
    min_value=df["year"].min(), 
    max_value=df["year"].max(), 
    value=df["year"].min(), 
    step=1
)

# Filter dataset based on the selected year
filtered_data = df[df["year"] == selected_year]

# Filter based on gender selection
if gender_selector != "Both":
    filtered_data = filtered_data[filtered_data["sex"] == gender_selector]

# Filter based on age group selection
filtered_data = filtered_data[filtered_data["age"].isin(age_selector)]

# Choose the column to display based on the measure selector
if measure_selector == "Total Suicides":
    color_column = "suicides_no"
    color_title = "Total Suicides"
else:
    color_column = "suicides/100k pop"
    color_title = "Suicides per 100k"
    
# Checkbox to show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(filtered_data)

# Aggregate suicides per country
agg_data = filtered_data.groupby("country", as_index=False)[color_column].sum()


# Create Choropleth Map
fig = px.choropleth(
    agg_data,
    locations="country",  # Country names
    locationmode="country names",  # Matches country names
    color=color_column,  # Use the selected measure for color intensity
    hover_name="country",  # Display country name on hover
    color_continuous_scale="Viridis",  # Adjust color scale
    title=f"{color_title} in {selected_year}"  # Title reflecting the selected year and measure
)

# Customize the layout
fig.update_layout(
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    margin=dict(l=0, r=0, t=50, b=0), # margins so title shows
    height=400
)

# Display map
st.plotly_chart(fig)

st.markdown("""___""") # make a stripe to seperate the graphs

# Only show the box plot if "Suicides per 100k" is selected
if (gender_selector == "Both"):
    
    # Create Box Plot
    fig_box = px.box(
        filtered_data, 
        x="sex", 
        y=color_column,   # ✅ Use actual column name
        color="sex",
        color_discrete_map={
            "male": "rgb(0,150,255)",   # Male = Blue
            "female": "rgb(255,16,240)" # Female = Pink
        },
        points="all",  # Show all individual points
        title=f"Total {color_title} in {selected_year} comparing gender",
        labels={color_column: color_title, "sex": "Gender"},  
        hover_data=["country"]  # Show country on hover
    )
    # Customize Layout
    fig_box.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=50, b=0), # margins so title shows
        height=400
    )

    # Show Box Plot
    st.plotly_chart(fig_box)
