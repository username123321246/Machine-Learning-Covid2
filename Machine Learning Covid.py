import pandas as pd
import matplotlib as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

asd = pd.read_csv("LESSONS\\covid_data.csv")
print(asd.head())

asd = asd[["Province_State", "Country_Region", "Confirmed", "Recovered", "Deaths", "Active", "Lat", "Long_"]]
asd.columns = ("State", "Country", "Confirmed Cases", "Recovered Cases", "Deaths", "Active Cases", "Latitude", "Longitude")
print(asd.head())

asd["State"] = asd["State"].fillna("")
print(asd.head())

top_ten_countries = pd.DataFrame(asd.groupby("Country") ["Confirmed Cases"].sum().nlargest(10).sort_values(ascending = False))
Fig1 = px.scatter(top_ten_countries, x = top_ten_countries.index, y = "Confirmed Cases", size = "Confirmed Cases", size_max = 200, color = top_ten_countries.index)
Fig1.write_html("Figure.html", auto_open = True)

recovered = pd.DataFrame(asd.groupby("Country") ["Recovered Cases"].sum().nlargest(10).sort_values(ascending = False))
Fig2 = px.bar(recovered, x = "Recovered Cases", y = recovered.index, height = 600, color = recovered.index, orientation = "h")
Fig2.write_html("Figure2.html", auto_open = True)

deaths = pd.DataFrame(asd.groupby("Country") ["Deaths"].sum().nlargest(10).sort_values(ascending = False))
Fig3 = px.bar(deaths, x = deaths.index, y = "Deaths", height = 600, color = deaths.index)
Fig3.write_html("Figure3.html", auto_open = True)

active = pd.DataFrame(asd.groupby("Country") ["Active Cases"].sum().nlargest(10).sort_values(ascending = False))
Fig4 = px.bar(active, x = active.index, y = "Active Cases", height = 600, color = active.index)
Fig4.write_html("Figure4.html", auto_open = True)

usstates = asd["Country"] == "US"
usstates = asd[usstates].nlargest(5, "Confirmed Cases")
Fig5 = go.Figure(data = [
    go.Bar(name = "Confirmed Cases", y = usstates["State"], x = usstates["Confirmed Cases"], orientation = "h"), 
    go.Bar(name = "Recovered Cases", y = usstates["State"], x = usstates["Recovered Cases"], orientation = "h")]) 
Fig5.update_layout(title = "Most affected states in US", height = 600)
Fig5.write_html("Figure5.html", auto_open = True)


