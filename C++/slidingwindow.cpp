#include<bits/stdc++.h>
using namespace std;
//calculating sum of given subarray using previous subarray

// max sum of subarray of size k

int max_sum(vector<int>v,int k){
    int sum=0;
    int max_sum=INT_MIN;
    for(int i=0;i<k;i++){
        sum=sum+v[i];
    }
    max_sum=sum;
    for(int i=k;i<v.size();i++){                 //O(n) time complexity
        sum=sum+v[i]-v[i-k];
        max_sum=max(sum,max_sum);
    }
    return max_sum;
}

int main(){
  vector<int>v={1,8,30,-5,20,7};
int t=max_sum(v,3);
cout<<"max sum is:"<<t<<endl;
}