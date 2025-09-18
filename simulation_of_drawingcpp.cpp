#include <iostream>
#include <random>
#include <iomanip>

using namespace std;

int single_trial(mt19937 &gen, uniform_real_distribution<> &dist){ //mt19937 is the random number engine thing
    double x_prev = dist(gen);
    int draws = 1;

    while (true) {
        double x_next = dist(gen);
        ++draws;

        if (x_prev < x_next) return draws;

        x_prev = x_next;
    }
   
}

double simulate(int n_trials = 100000) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dist(0.0, 1.0);

    long long total = 0;
    for (int i = 0; i < n_trials; ++i){
        total += single_trial(gen, dist);
    }

    return static_cast<double>(total) / n_trials;
}

int main(){
    int n_trials = 100000;
    double estimate = simulate(n_trials);

    cout << fixed << setprecision(4) << estimate << endl;
}