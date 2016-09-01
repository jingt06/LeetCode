#include "reverseLinkedList.h"
#include <iostream>
using namespace std;

node:: node(int val, node* ptr):val(val), next(ptr){}

void llist:: Reverse(){
	node* end = NULL;
	node* curr = this->first;
	if(curr == NULL) {
		// no need to reverse
		return;
	}
	node* next = curr->next;
	while(next != NULL) {
		curr->next = end;
		end = curr;
		curr = next;
		next = next->next;
	}
	curr->next = end;
	this->first = curr;
}

void llist:: Print(){
	node* iter = this->first;
	while(iter != NULL) {
		cout<<iter->val<<" ";
		iter = iter->next;
	}
}