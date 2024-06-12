import pymongo as pym
import os
from dotenv import load_dotenv
import pandas as pd
import isodate
import json
from bson.json_util import dumps
from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime, tzinfo, timezone
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt



load_dotenv(r"key.env")
mongo_url = os.getenv("CONNECTION_STRING")

client = pym.MongoClient(mongo_url)

#db = client['database_name']
dbs = client.list_database_names()

sample_airbnb = client["sample_airbnb"]
sample_airbnb_collections = sample_airbnb.list_collection_names()

listing_reviews = sample_airbnb["listingsAndReviews"]

groupby_property_type = listing_reviews.aggregate([
    {
        '$group': {
            '_id': '$property_type', 
            'count': {
                '$sum': 1
            }
        }
    }
])

json_data=dumps(list(groupby_property_type))

df = pd.json_normalize(json.loads(json_data))

df['_id'] = df['_id'].fillna('Unknown')

# Sort the DataFrame based on the 'count' column in descending order
df = df.sort_values(by='count', ascending=False)
#fig = px.bar(df, x=df['_id'], y=df['count'], title=' Bar Chart')
print(df)
#fig.show()
plt.figure(figsize=(10, 6))
plt.bar(df['_id'], df['count'], color='skyblue')
plt.xlabel('Property Type')
plt.ylabel('Count')
plt.title('Property Type Bar Chart')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Define the file name
current_date = datetime.now().strftime("%Y-%m-%d")
file_name = f"bar_chart_{current_date}.jpeg"

# Save the plot as a JPEG file
plt.savefig(file_name, format='jpeg', dpi=300)

print(f"Bar chart saved as {file_name}")




