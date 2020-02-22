#include<iostream>
#define SIZE 5

using namespace std;

class Queue{

    private:
        int line[SIZE], front=-1, rear=-1;

    public:

        void enqueue(int value){
            
            if((this->front+this->rear)){
                cout<<"Queue Overflow"<<endl;
                return ;
            }
            else{
                this->rear = (this->rear+1)%SIZE;
                this->line[this->rear]=value;
                if(this->front == -1){
                    front=0;
                }                             
            }

        }

        void dequeue(void){
            if(front == -1){
                cout<<"Queue Underflow"<<endl;
            }
            else{
                if(this->front == this->rear){
                    this->front=-1;
                    this->rear = -1;                
                }
                else if(this->front == SIZE-1)
                    this->front = 0;
                else{
                    this->front++;
                }
            }
        }

        void print(void){
    
            if(this->front==-1){
                cout<<"Queue Empty"<<endl;
            }
            else{
                for(int i=this->front; i<=this->rear;i++){
                    cout<<"| "<<this->line[i]<<" | ";
                }
            }
        }
};

int main(){
    
    Queue queue = Queue();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);
    queue.print();
    queue.dequeue();
    queue.enqueue(6);
    queue.print();

    return 0;
}