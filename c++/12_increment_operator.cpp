#include <iostream>
using namespace std;

int main(){
	int x,y;
	x = 5;
	y = ++x;   // prefix, x=6, y=6
	cout << "for prefix" << endl;
	cout << "x : " << x << endl;
	cout << "y : " << y << endl;
	
	int a,b;
	a = 5;
	b = a++;   // postfix, x=6, y=5
	cout << "for postfix" << endl;
	cout << "x : " << a << endl;
	cout << "y : " << b << endl;
	
	return 0;
}
