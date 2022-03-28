import streamlit as st
import numpy as np
import pandas as pd

class Process():
	def __init__(self,wt=0,bt=0,at=0,pid=0,tat=0):
		self.bt=bt
		self.wt=wt 
		self.at=at 
		self.pid=pid
		self.tat=tat

	def __str__(self):
		return self.bt

def sort_acc_to_arrival():
	for i in range(0,len(st.session_state.p)-1):
		for j in range(0,len(st.session_state.p)-1-i):
			if st.session_state.p[j].at>st.session_state.p[j+1].at:
				p[j],p[j+1]=p[j+1],p[j]


def calc_waiting_time():
	t=0
	for i in range(1,len(st.session_state.p)):
		st.session_state.p[i].wt=st.session_state.p[i-1].wt+st.session_state.p[i-1].bt
	for i in range(0,len(st.session_state.p)):
		st.session_state.p[i].wt-=st.session_state.p[i].at

def calc_turnaround_time():
	for i in st.session_state.p:
		i.tat=i.wt+i.bt;

def get_dataframe(data,columns):
	return pd.DataFrame(data,columns=columns)

st.title("FCFS Scheduling")

p=[]
data=[]

if 'p' not in st.session_state:
    st.session_state.p = []
if 'data' not in st.session_state:
    st.session_state.data = []


pid=st.number_input("Enter Pid",step=1)
bt=st.number_input("Enter Burst Time",step=1)
at=st.number_input("Enter arrival Time",step=1)

add=st.button("Add process")
clr=st.button("Clear Table")

if clr:
	st.session_state.p = []
	st.session_state.data = []

if add:
	st.session_state.p.append(Process(pid=pid,bt=bt,at=at))


for i in range(len(st.session_state.p)):
	data.append([st.session_state.p[i].pid,st.session_state.p[i].bt,st.session_state.p[i].at])

df=get_dataframe(data,["Process",'Burst Time',"Arrival Time"])

st.header("Process Table")
st.dataframe(df)

if st.session_state.p!=[]:
	but=st.button("Calculate Waiting Time & Turnaround Time")


	if but:
		# sort_acc_to_arrival()
		# st.dataframe(df)

		calc_waiting_time()
		calc_turnaround_time()
		data=[]
		del df
		for i in range(len(st.session_state.p)):
			data.append([st.session_state.p[i].pid,st.session_state.p[i].wt,st.session_state.p[i].tat])

		df2=get_dataframe(data,["Process","Waiting Time","Turnaround Time"])
		st.dataframe(df2)

		st.header("Average waiting time")

		s=""
		av=0
		for i in st.session_state.p:
			av+=i.wt
			s+=str(i.wt)
			if i.pid<len(st.session_state.p):
				s+="+"
		av=av/len(st.session_state.p)
		st.latex(r"=\frac{"+s+"}{"+str(len(st.session_state.p))+"}="+str(av))

		st.header("Average Turnaround time")

		s=""
		av=0
		for i in st.session_state.p:
			av+=i.tat
			s+=str(i.tat)
			if i.pid<len(st.session_state.p):
				s+="+"
		av=av/len(st.session_state.p)
		st.latex(r"=\frac{"+s+"}{"+str(len(st.session_state.p))+"}="+str(av))


footer="""<style>


.footer {
position:fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by Aditya Yadav</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)