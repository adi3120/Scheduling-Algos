#include<iostream>
using namespace std;

struct Process{
	int id;
	int wt=0;
	int at=0;
	int tot=0;
	int bt=0;
	int st=0;
};
int Time=0;
void make_same(Process source,Process &dest){
	dest.wt=source.wt;
	dest.at=source.at;
	dest.tot=source.tot;
	dest.bt=source.bt;
	dest.id=source.id;
}
void swap_processes(Process & p1,Process & p2){
	Process p3;
	make_same(p1,p3);
	make_same(p2,p1);
	make_same(p3,p2);
}
void sort_accto_arr_time(Process p[],int size){
	for(int i=0;i<size-1;i++){
		for(int j=0;j<size-1;j++){
			if(p[j].at>p[j+1].at){
				swap_processes(p[j],p[j+1]);
			}
		}
	}
}
void Draw_all_process_table(Process p[],int size){
	cout<<"\n\n";
	cout<<"+---------+"<<"------------+"<<"--------------+"<<"--------------+";
	cout<<endl;
	cout<<"| Process"<<" | "<<"Burst Time"<<" | "<<"Arrival Time"<<" | "<<"Waiting Time"<<" | "<<endl;
	cout<<"+---------+"<<"------------+"<<"--------------+"<<"--------------+";
	cout<<endl;

	for(int i=0;i<size;i++){
		cout<<"| P"<<p[i].id<<"      |";
		cout<<p[i].bt<<"           |";
		cout<<p[i].at<<"             |";
		cout<<p[i].wt<<"             |";
		cout<<endl;
	}
	cout<<"+---------+"<<"------------+"<<"--------------+"<<"--------------+";
	cout<<endl;
	cout<<"\n";
	
}
void draw_spaces(int bt){
	for(int i=0;i<bt;i++){
		cout<<" ";
	}
}
void draw_dashes(int bt){

	for(int j=0;j<bt;j++){
		cout<<"--";
	}
	cout<<" ";
	
}
void Draw_Gantt_Chart(Process p[],int size)
{
	cout<<"\n\nGantt Chart"<<endl;
	cout<<" ";
	for(int i=0;i<size;i++){
		draw_dashes(p[i].bt);
	}
	cout<<endl<<"|";

	for(int i=0;i<size;i++){
		draw_spaces(p[i].bt-1);
		cout<<"P"<<p[i].id;
		draw_spaces(p[i].bt-1);	
		cout<<"|";
	}

	cout<<endl;
	cout<<" ";
	for(int i=0;i<size;i++){
		draw_dashes(p[i].bt);
	}
	cout<<endl;

	for(int i=0;i<size;i++){

		cout<<Time;
		int offset=0;
		if(Time>9){
			offset=-1;
		
		}
		for(int j=0;j<p[i].bt+offset;j++){
			cout<<"  ";
		}
		Time+=p[i].bt;

	}
	cout<<Time<<"\n\n";
}
void calc_waiting_time(Process p[],int size){
	int t=0;
	for(int i=1;i<size;i++){
		p[i].wt=(p[i-1].wt+p[i-1].bt);
	}
	for(int i=0;i<size;i++){
		p[i].wt-=p[i].at;
	}
}

float calc_av_wt(Process p[],int size){
	float av_wt=0;
	for(int i=0;i<size;i++){
		av_wt+=p[i].wt;
	}
	return av_wt/size;
}
int main()
{
	Process p[5];


	p[0].at=2;
	p[1].at=5;
	p[2].at=1;
	p[3].at=0;
	p[4].at=4;

	p[0].bt=6;
	p[1].bt=2;
	p[2].bt=8;
	p[3].bt=3;
	p[4].bt=4;

	p[0].id=1;
	p[1].id=2;
	p[2].id=3;
	p[3].id=4;
	p[4].id=5;

	sort_accto_arr_time(p,5);
	p[0].wt=0;
	calc_waiting_time(p,5);

	cout<<"\n\nFirst Come First Serve (FCFS) Scheduling"<<endl;

	Draw_all_process_table(p,5);

	Draw_Gantt_Chart(p,5);

	cout<<"Average Waiting Time : "<<calc_av_wt(p,5)<<endl;

	


}