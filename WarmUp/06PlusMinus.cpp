#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    double positives = 0;
    double negatives = 0;
    double zeros = 0;
    for(int x : arr){
        if(x > 0) positives++;
        else if(x < 0) negatives++;
             else zeros++; 
    }
    cout << positives / n << endl;
    cout << negatives / n << endl;
    cout << zeros / n << endl;
    return 0;
}
