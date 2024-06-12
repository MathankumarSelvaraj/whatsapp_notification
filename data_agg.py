import numpy as np
import pandas as pd
import streamlit as st

df = pd.read_csv('dataset/data.csv')


groupby_sales = df.groupby("sl").agg({"file":"count"})
#aggregated = df.groupby('Category').agg({'Value': ['mean', 'sum', 'count']})
check = df["sl"].unique()
#st.dataframe(groupby_sales.head(5))
st.text(groupby_sales.head(5))

with st.container(height=100):
    for i in check:
        value = st.checkbox(i,True)
        
st.write(value)   

airline_names = ['Delta', 'American Airlines', 'United Airlines', 'Lufthansa', 'Air France', 'British Airways', 'Emirates', 
                 'Qatar Airways', 'Singapore Airlines', 'Cathay Pacific', 'China Southern Airlines', 'ANA', 'Southwest Airlines', 
                 'Ryanair', 'Air Canada', 'Turkish Airlines', 'Korean Air', 'LATAM Airlines', 'JetBlue Airways', 'Qantas', 
                 'Air India', 'Alaska Airlines', 'Etihad Airways', 'IndiGo', 'easyJet', 'EVA Air', 'Aeroflot', 'Virgin Atlantic', 
                 'Spirit Airlines', 'Norwegian Air Shuttle', 'Hainan Airlines', 'SAS', 'Garuda Indonesia', 'Air New Zealand', 
                 'Saudi Arabian Airlines', 'China Eastern Airlines', 'Vueling Airlines', 'Finnair', 'WestJet', 'Jetstar Airways', 
                 'All Nippon Airways', 'AirAsia', 'Allegiant Air', 'Malaysia Airlines', 'Vietnam Airlines', 'Royal Air Maroc', 
                 'SriLankan Airlines', 'Iberia', 'Norwegian', 'Pakistan International Airlines']
volume = np.random.randint(10000, 1000000, size=len(airline_names))

# Create DataFrame
df_airline = pd.DataFrame({'Airline Name': airline_names, 'Volume': volume})

st.dataframe(df_airline)

selected_airlines = []

with st.container(height= 100):
    for airline in airline_names:
        if st.checkbox(airline, True):
            selected_airlines.append(airline)

# Filter the DataFrame based on selected airlines
filtered_df = df_airline[df_airline['Airline Name'].isin(selected_airlines)]

# Display the filtered DataFrame
st.dataframe(filtered_df)
#selected_df  = 