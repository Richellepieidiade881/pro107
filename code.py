import pandas as pd 
import csv
from pandas.io.parsers import read_csv 
import plotly.express as ps
df=read_csv("data.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=pd.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
fig.show()
