#include<iostream>
#define SIZE 5

using namespace std;

class Queue{

    private:
        int line[SIZE], front=-1, rear=-1;

    public:

        void enqueue(int value){
            
            if(this->rear >= SIZE-1){
                cout<<"Queue Overflow"<<endl;
                return ;
            }
            else{
                this->rear = (this->rear+1)%SIZE;
                this->line[this->rear]=value;
                if(this->front == -1){
                    front=0;
                }
                // cout<<"success"<<endl;
            }
            // cout<<"value of rear upon inserting "<<value<<": "<<this->rear<<endl;
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
            // cout<<"front: "<<this->front<<endl;
            // cout<<"rear: "<<this->rear<<endl;
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
    // queue.dequeue();
    // queue.dequeue();
    queue.enqueue(6);
    // queue.enqueue(7);

    queue.print();
    return 0;
}