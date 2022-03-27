import streamlit as st
import numpy as np
import pandas as pd

class Process():
	def __init__(self,wt=0,bt=0,at=0,pid=0):
		self.bt=bt
		self.wt=wt 
		self.at=at 
		self.pid=pid

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
	Process(bt=3,at=0,pid=1),
	Process(bt=8,at=1,pid=2),
	Process(bt=6,at=2,pid=3),
	Process(bt=4,at=4,pid=4),
	Process(bt=2,at=5,pid=5),
]

data=[]

for i in range(len(p)):
	data.append([p[i].pid,p[i].bt,p[i].at])

df=pd.DataFrame(data,columns=["Process",'Burst Time',"Arrival Time"])

st.dataframe(df)

but=st.button("Calculate Waiting Time")

if but:
	calc_waiting_time()
	data=[]
	del df
	for i in range(len(p)):
		data.append([p[i].pid,p[i].wt])

	df2=pd.DataFrame(data,columns=["Process","Waiting Time"])
	st.dataframe(df2)

	st.header("Average waiting time")

	s=""
	av=0
	for i in p:
		av+=i.wt
		s+=str(i.wt)
		if i.pid<len(p):
			s+="+"
	av=av/len(p)
	st.latex(r"=\frac{"+s+"}{"+str(len(p))+"}="+str(av))

