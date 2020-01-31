#include<iostream>
#include"BST.h"

using namespace std;

BST::BST()
{
	root = NULL;
}

BST::Node* BST::createNode(int data){

	Node * node = new Node;
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return node;
}

