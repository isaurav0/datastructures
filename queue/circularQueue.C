#include<iostream>
#define SIZE 3

using namespace std;

class Queue{

    private:
        int line[size], front=-1, rear=-1;

    public:

        void enqueue(int value){
            if(this->rear >= size){
                cout<<"Queue Overflow"<<endl;
            }
            this->rear++;
            this->line[this->rear]=value;
            if(this->front == -1){
                front=0;
            }            
        }

        void dequeue(void){


        }

}

int main(){


    return 0;
}