#include<iostream>
using namespace std;

int main(){
    unsigned long long res  =1;
    unsigned long long mod  =1e8 + 7;
    unsigned long long n;
    cin>>n;

    for(int i=1 ; i<=n ; i++){
        res*=i;
        res%=mod;
    }
    // cout<<res<<endl;
    return 0;
}