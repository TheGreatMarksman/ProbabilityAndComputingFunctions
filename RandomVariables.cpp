#include <stdio.h>
#include <set>
#include <vector>
#include<iostream>

using namespace std;


// L12-5
// Heads are 0, tails are 1
// Bernoulli and indicator r.v.
int numHeads(vector<bool> event) {
    int num = 0;
    for (bool b : event) {
        if (b == 0)
            num++;
    }
    return 0;
}

// L12-6
// Indicator r.v.
bool bothPrime(vector<int> event) {
    int numPrimes = 0;
    for (int i : event) {
        if (isPrime(i))
            numPrimes++;
    }
    if (numPrimes >= 2)
        return true;
    return false;
}

bool isPrime(int num) {
    for (int i = 2; i < num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

// L12-8


void main(void) {

}
