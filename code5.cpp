#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void display(vector<vector<int>> &array){
    for (size_t i = 0; i < 3; i++){
        for (size_t j = 0; j < 3; j++){
            cout<<array[i][j]<<" ";
        }
        cout<<endl;
    }
}
auto comp = [](vector<int> &a,vector<int> &b){
        return a[0] - b[0];
};
int main(){
    
    vector<vector<int>> array = {
        {2,3,5},//entiity 1
        {1,3,4},//entity 2
        {0,5,6}//entity 3
    };
    
    display(array);
    sort(array.begin(),array.end(),comp);
    cout<<endl;
    display(array);
    return 0;
}