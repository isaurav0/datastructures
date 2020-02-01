#include<iostream>

using namespace std;


class Node{

	public: 

		int value = NULL;
		Node* left = NULL;
		Node* right = NULL;

		Node(int val){
			this->value = val;
			this->left = NULL;
			this->right = NULL;
		}

		int getValue(){
			return this->value;
		}

		bool addNode(Node* node){
			
			if(node->value < this->value){
				if(this->left != NULL){
					this->left->addNode(node);
				}
				else{
					this->left = node;
					// cout<<"Added to tree: "<<node->value<<endl;
					return true	;
				}
			}
			if(node->value > this->value){
				if(this->right != NULL)
					this->right->addNode(node);
				else{
					this->right = node;
					// cout<<"Added to tree: "<<node->value<<endl;
					return true;
				}
			}
			if(node->value == this->value)
				return false;

		}		
};

class Tree{

	private:
		Node* root = NULL;
	
	public: 

		bool addValue(int val){
			// cout<<this->root->getValue();
			Node* node = new Node(val);
			if(this->root == NULL)			
				this->root = node;
			else
				return this->root->addNode(node);
		}
};


int main(){

	Tree tree;
	tree.addValue(25);
	tree.addValue(3);
	tree.addValue(100);
	tree.addValue(2);
	tree.addValue(110);
	tree.addValue(5);
	tree.addValue(30);
	tree.addValue(57);
	
	return 0;

}
