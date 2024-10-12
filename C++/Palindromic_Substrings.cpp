#include <bits/stdc++.h>
using namespace std;

// Function to count the number of palindromic substrings in a string
int countSubstrings(string s) {
    int n = s.size(), count = 0;
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    for(int len = 1; len <= n; len++) {
        for(int i = 0; i + len <= n; i++) {
            int j = i + len - 1;
            if(len == 1)
                dp[i][j] = true;
            else if(len == 2)
                dp[i][j] = (s[i] == s[j]);
            else
                dp[i][j] = (s[i] == s[j]) && dp[i + 1][j - 1];
            if(dp[i][j]) count++;
        }
    }
    return count;
}

int main(){
    string s;
    cout << "Enter the string: ";
    cin >> s;
    cout << "Number of palindromic substrings: " << countSubstrings(s) << endl;
    return 0;
}
