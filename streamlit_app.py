import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

response_API = requests.get('https://anss-api.dev.asiagate.com/v1/member-states')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)

print(parse_json)

df = pd.json_normalize(parse_json, record_path=['data'])

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
# print(df)
df["attributes.unsd"] = pd.to_numeric(df["attributes.unsd"])
bardf= df[['attributes.name','attributes.unsd']].copy()
bardf = bardf.set_index('attributes.name')

fig = px.bar(df, y='attributes.name', x='attributes.unsd', orientation='h')
st.write(fig)

# st.bar_chart(bardf)
