#include<iostream>
#include<string>

using namespace std;
int main(){
	int small=0, caps=0, num=0, sp_char=0, i;
	string pswd;
	getline(cin, pswd);
	for(i=0; pswd[i] !='\0'; i++){
		if(pswd[i]>=65 && pswd[i]<=90)
			caps=1;
		if(pswd[i]>=97 && pswd[i]<=122)
			small=1;
		if(pswd[i]>=48 && pswd[i]<=57)
			num=1;
		if(pswd[i]>=65 && pswd[i]<=90)
			caps=1;
		if(pswd[i]=='$' || pswd[i]== '#' || pswd[i]== '@')
			sp_char=1;

	}
	if(i< 6 || i> 12)
		cout<<"INVALID";
	else if ((caps && small && num && sp_char))
	{
		cout<<"VALID";
	}
	else
		cout<<"INVALID";
	
}
