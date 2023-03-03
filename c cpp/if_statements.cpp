#include<iostream>
#include<cmath>
using namespace std;

int main(){

    int x, y;
    cout << "Enter the first number: ";
    cin >> x;
    cout << "Enter the second number: ";
    cin >> y;
    
    if (x < y){
        cout << "The first number is higher than the second";
    }

    if (x > y){
        cout << "The second number is higher than the first";
    }

    return 0;
}