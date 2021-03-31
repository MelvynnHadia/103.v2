import pandas as pd

import plotly.express as px

df = pd.read_csv("csv files/data.csv")

fig = px.scatter(df, x="Date", y="Infected", size = "Infected", color = "Country",title = "Covid Infection Statistics", size_man = 60)

fig.show()