import pywhatkit

import pyspark as py
import numpy as np
import pandas as pd
#import streamlit as st

df = pd.read_csv('dataset/data.csv')


groupby_sales = df.groupby("sl").agg({"file":"count"})
#aggregated = df.groupby('Category').agg({'Value': ['mean', 'sum', 'count']})

#st.dataframe(groupby_sales.head(5))

df_text = groupby_sales.head(5).to_string(index=True)
phone_number = "+917200348426"
message = df_text


#pywhatkit.sendwhatmsg(phone_number, message)
pywhatkit.sendwhatmsg_instantly(phone_number, message)