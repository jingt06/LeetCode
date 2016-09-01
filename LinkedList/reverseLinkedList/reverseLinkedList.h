class  node {
public:
	node * next;
	int val;
	node(int, node*);
};

class llist {
public:
	node* first;
	void Reverse();
	void Print();
};