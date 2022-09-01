#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> v;
    v.push_back(5);
    v.push_back(1);
    v.push_back(3);
    sort(v.begin(),v.end(),[](int a,int b){
        return a-b;
    });
    for(auto &x: v){
        x*=10;
    }
    for(auto &x: v){
        cout<<x<<" ";
    }
    return 0;
}