import streamlit as st
import numpy as np
import pandas as pd

class Process():
	def __init__(self,wt=0,bt=0,at=0):
		self.bt=bt
		self.wt=wt 
		self.at=at 

	def __str__(self):
		return self.bt

def calc_waiting_time():
	t=0
	for i in range(1,len(p)):
		p[i].wt=p[i-1].wt+p[i-1].bt
	for i in range(0,len(p)):
		p[i].wt-=p[i].at

st.title("FCFS Scheduling")
p=[
	Process(bt=3,at=0),
	Process(bt=8,at=1),
	Process(bt=6,at=2),
	Process(bt=4,at=4),
	Process(bt=2,at=5),
]

data=[]

for i in range(len(p)):
	data.append([p[i].bt,p[i].at,p[i].wt])

df=pd.DataFrame(data,columns=['Burst Time',"Arrival Time","Waiting Time"])

st.dataframe(df)

but=st.button("Calculate Waiting Time")

if but:
	calc_waiting_time()
	data=[]

	for i in range(len(p)):
		data.append([p[i].bt,p[i].at,p[i].wt])

	df=pd.DataFrame(data,columns=['Burst Time',"Arrival Time","Waiting Time"])

	st.dataframe(df)

