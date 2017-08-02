#include <bits/stdc++.h>

using namespace std;

string timeConversion(string s) {
    string ans;
    char hd, hu;
    if(s[8]=='P'){
		hd = s[0];
        hu = s[1];
		if(s[1]=='8'||s[1]=='9'){
			hu -= 8;
			hd += 2;  
		}else if(!(hd == '1' && hu == '2')){
            hd+=1;
            hu+=2;
        }
    }else{
        if(s[0]=='1' && s[1]=='2'){
            hd = '0';
            hu = '0';
        }else{
            hd = s[0];
            hu = s[1];
        }
    }
    ans.push_back(hd);
    ans.push_back(hu);
    for(int i = 2; i < 8; i++)
           ans.push_back(s[i]);
    return ans;
}

int main() {
    string s;
    cin >> s;
    string result = timeConversion(s);
    cout << result << endl;
    return 0;
}
