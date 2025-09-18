#include <iostream>
#include <random>

using namespace std;

int main(){
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<> dist(0.0, 1.0); //this is to represent a mean of 0 and a std of 1

    for (int i = 0; i < 10; ++i){
        cout << dist(gen) << endl;
    }
}