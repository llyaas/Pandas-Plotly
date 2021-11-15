import pandas as pd
import plotly.express as px

df = pd.read_csv('line_chart.csv')
graph = px.line(df,x = "Country",y = "Per capita income")
graph.show()