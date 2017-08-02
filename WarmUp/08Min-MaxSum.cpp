#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> arr(5);
    for(int arr_i = 0; arr_i < 5; arr_i++){
       cin >> arr[arr_i];
    }
    long long int sum = 0;
    for(int x : arr)
       sum += x;
    long long min = *min_element(arr.begin(), arr.end());
    long long max = *max_element(arr.begin(), arr.end());
    cout << sum - max << " " << sum - min << endl;
    return 0;
}
