class Tree{

	private:

	struct Node{
		int data;
		struct Node *left, *right;	
	};
	
	Node* root = NULL;

	Node* addNodePrivate(int data, Node *ptr);
	
	public:

	void BST();
	Node* createNode(int data);
	void addNode(int data);
//	struct Node* getNewNode(int data){
//		Node* node = new Node();
//		node.data = data;
//		node->left = node->right = NULL;
//	}

};
