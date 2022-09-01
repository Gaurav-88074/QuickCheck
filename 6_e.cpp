#include<iostream>
using namespace std;

class A{
    public:
        static int count;

        A(){
            count+=1;
        }
        int getCount(){
            return count;
        }
};
int A::count = 0;

int main(){

    A object1;
    cout<<"total objects : "<<object1.count<<endl;

    A object2;
    cout<<"total objects : "<<object1.count<<endl;

    return 0;
}