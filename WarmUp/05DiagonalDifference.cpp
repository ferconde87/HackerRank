#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    int diag1 = 0;
    for(int i = 0; i < n; i++)
        diag1 += a[i][i];
    int diag2 = 0;
    for(int i = 0; i < n; i++)
        diag2 += a[n-1-i][i];
    cout << abs(diag1-diag2) << endl;
    return 0;
}
