class  node {
public:
	node * next;
	int val;
	node(int val, node* ptr):val(val), next(ptr){}
};

