#include<iostream>
#include<vector>
using namespace std;

int main(){
    
    vector<int> adj[3];
    // adj[0] =4;
    adj[1].push_back(4);
    adj[2].push_back(4);
    adj[3].push_back(4);
    cout<<adj[1][0]<<endl;
    return 0;
}