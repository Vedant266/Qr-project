import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title = "Sales Results")
st.header("Sales 2024")

excel_name = "Book1.xlsx"
sheet_name = "DATA"

df = pd.read_excel(excel_name,
                      sheet_name = sheet_name,
                      usecols = "A:C",
                      header = 0)

df_sales = pd.read_excel(excel_name,
                      sheet_name = sheet_name,
                      usecols = "B:C",
                      header = 0)


st.dataframe(df,
             hide_index = True)

pie_chart = px.pie(df_sales,
                   title = "Total Sales",
                   values = "Sales",
                   names = "Department")

st.plotly_chart(pie_chart)


