#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main(){
	string temp;
	int up, down, left, right, int_tmp, d;
	for(int i=0; i<4; i++){
	cin>> temp >> int_tmp;
	if(temp == "UP")
		up= int_tmp;
	if(temp == "DOWN")
		down= int_tmp;
	if(temp == "LEFT")
		left= int_tmp;
	if(temp == "RIGHT")
		right= int_tmp;
	}
	d = abs(sqrt((up-down)*(up-down) + (left- right)*(left- right)));
	cout<< d;

}