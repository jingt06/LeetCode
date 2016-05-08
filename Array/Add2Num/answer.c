#include <stdlib.h>

struct node {
	int val;
	struct node* next;
	struct node* pre;
};

struct node* add2Num(struct node* num1, struct node* num2){
	struct node* l1 = num1;
	struct node* l2 = num2;
	int val = 0;
	int carry = 0;
	struct node* previous = NULL;
	for(struct node* iterator = num1; iterator!= NULL; iterator = iterator->next){
		l1 = iterator;
	}
	for(struct node* iterator = num2; iterator!= NULL; iterator = iterator->next){
		l2 = iterator;
	}
	while ( l1 != NULL || l2 != NULL ) {
		int v1 = l1? l1->val : 0;
		int v2 = l2? l2->val : 0;
		val = (v1 + v2 + carry) % 10;
		carry = (v1 + v2 + carry) / 10;
		struct node* new = malloc(sizeof(struct node));
		new->val = val;
		new->next = previous;
		previous = new;
	}
	return previous;
}

int main(){
}