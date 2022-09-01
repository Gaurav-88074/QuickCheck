#include<iostream>
using namespace std;

void replace(int &num){
    int arr[10] = {0};
    
    while (num>0){
        int value = num%10;
        arr[value] +=1;
        num/=10;
    }
    for (int i = 0; i < 10; i++){
        while(arr[i]!=0){
            num+=i;
            num*=10;
            arr[i]--;
        }
    }
    num/=10;
}
int main(){
    int num = 4223;
    cout<<"value of num : "<<num<<endl;

    replace(num);
    cout<<"value of num : "<<num<<endl;
  
    return 0;
}