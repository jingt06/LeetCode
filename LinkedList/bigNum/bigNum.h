class  node {
public:
	node * next;
	int val;
	node(int, node*);
};



class bigNum
{
	node* first;
	bool sign;
	void _reverse();
public:
	bigNum(int);
	bigNum();
	~bigNum();
	void print() const;
	friend bigNum* operator+(bigNum &, bigNum &);
};

bigNum* operator+(bigNum &, bigNum &);