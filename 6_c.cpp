#include<iostream>
#include<string>
using namespace std;

void displayAscii(string s){
    for (int i = 0; i < s.length(); i++){
        cout<<"Ascii value of "<<s[i]<<" : "<<(int)s[i]<<endl;
    }
}
int main(){
    
    string s = "hello world";
    cout<<s<<endl;
    for (int  i = 0; i < s.length(); i++){
        if(s[i]=='o'){
            s.insert(i,"offline");
            break;
        }
    }
    cout<<s<<endl;
    displayAscii(s);

    return 0;
}