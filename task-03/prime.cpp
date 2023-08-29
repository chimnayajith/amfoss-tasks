#include <iostream>
using namespace std;

bool isPrime(int num){
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    int i = 5;
    while (i * i <= num) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
}

int main(){
    int n;
    cin >> n; //input stream object for input from keyboard => cin >>   

    for (int i =2;i<=n;i++){
        if(isPrime(i)){
            cout << i << " "; //output stream cout <<
        }
    }

    return 0;
}


//run : g++ -o prime prime.cpp
// then run ./prime