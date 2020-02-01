#include<iostream>
using namespace std;
#define size 5


class Stack{

    private:
        int stack[size];

    public:
        int top;

        Stack(){
            this->top = -1;            
        }

        void push(int data){
            if(this->top < size){
                this->top += 1;
                this->stack[this->top] = data;
            }
            else{
                cout<<"Stack Overflow"<<endl;
            }
            
        }

        int peek(){
            if(this->top == -1)
                cout<<"Stack empty"<<endl;
            else{
                cout<<stack[this->top]<<endl;
                return this->stack[this->top];
            }
        }

        int pop(){            
            if(this->top == -1)
                cout<<"Stack empty"<<endl;
            else {
                this->top--;
                cout<<"Popped: "<<this->stack[this->top+1]<<endl;
                return this->stack[this->top+1];
            }
        }

        bool isFull(){
            if(this->top >= size)
                return true;
            else 
                return false;
        }

        bool isEmpty(){
            if(this->top == -1)
                return true;
            else 
                return false;

        }

};



int main(){
    Stack stck;

    stck.push(1);
    // stck.push(3);
    // stck.push(10);
    stck.pop();
    stck.peek();
    // stck.push(12);
    // stck.push(2);
    // stck.pop();
    // stck.peek();
    cout<<"isEmpty: "<<stck.isEmpty()<<endl;
    cout<<"isFull: "<<stck.isFull()<<endl;
    

    return 0;
}