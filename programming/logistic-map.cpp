#include <iostream>

using namespace std;

double logistic_map(int index){
	double x_n = 0.3;
	for(int i=1;i<index;i++){
		x_n = 3.99 * x_n * (1 - x_n);
	}
	return x_n;
}

int main(){
	cout << logistic_map(9999)<< endl;
	return 0;
}
