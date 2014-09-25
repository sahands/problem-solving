#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//ifstream fin("n.in");

int main(int argc, char *argv[]){
	while(true){  //do another problem...
		int num; cin>>num; if(num<0) break;
		int sum=1; int nFacs = 1; int fac[1000]; fac[0]=1;
		for(int i=2; i<=num/2; i++) if(num % i == 0){ //if i divides into num
			sum += i;  fac[nFacs++] = i;
		}
		if(sum==num){  //if perfect...
			cout<<num<<" = "<<fac[0];
			for(int i=1;i<nFacs;i++)cout<<" + "<<fac[i];
			cout<<endl;
		}else{
			cout<<num<<" is NOT perfect."<<endl;
		}
	}
}
