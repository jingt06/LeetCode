#include "bigNum.h"
#include <iostream>
using namespace std;

node:: node(int val, node* ptr):val(val), next(ptr){}

bigNum:: bigNum(int num){
	bool sign = true;
	node* iter = NULL;
	if (num < 0){
		sign = false;
		num = - num;
	}
	if (num == 0) {
		iter = new node(0, NULL);
	}
	while (num != 0) {
		int div = num % 10;
		int rem = num / 10;
		node * tempNode = new node(div, iter);
		iter = tempNode;
		num = rem;
	}
	this->first =  iter;
	this->sign = sign;
}

bigNum:: bigNum(){
	this->first =  NULL;
	this->sign = true;
}

void bigNum:: print() const{
	if(!this->sign) cout<<"-";
	node* iter = this->first;
	while(iter != NULL) {
		cout<< iter->val;
		iter=iter->next;
	}
}

bigNum:: ~bigNum() {
	node * iter = this->first;
	while (iter != NULL){
		node* tmp = iter->next;
		iter = tmp;
	}
}

void bigNum:: _reverse(){
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

bigNum* operator+(bigNum & a, bigNum & b){
	a._reverse();
	b._reverse();
	// reverse all digits
	int carry = 0;
	node * a_iter = a.first;
	node * b_iter = b.first;
	bigNum * result = new bigNum();
	node ** res_iter = &(result->first);
	bool sign = true;
	while(a_iter != NULL || b_iter != NULL) {
		if (a_iter != NULL && b_iter != NULL) {
			if((a.sign && b.sign) || (!a.sign && !b.sign)){ // all positive or all negaative
				sign = a.sign;
				int res = a_iter->val + b_iter->val + carry;
				if (res >= 10) {
					res -= 10;
					carry = 1;
				}else {
					carry = 0;
				}
				*res_iter = new node(res, NULL);
				res_iter = &(*res_iter)->next;
			}
			a_iter = a_iter->next;
			b_iter = b_iter->next;
		} else if (a_iter != NULL) {
			int res = a_iter->val + carry;
			if(res >= 10) {
				res -= 10;
				carry = 1;
			} else {
				carry = 0;
			}
			*res_iter = new node(res, NULL);
			res_iter = &(*res_iter)->next;
			a_iter = a_iter->next;
		} else if (b_iter != NULL) {
			int res = b_iter->val + carry;
			if(res >= 10) {
				res -= 10;
				carry = 1;
			} else {
				carry = 0;
			}
			*res_iter = new node(res, NULL);
			res_iter = &(*res_iter)->next;
			b_iter = b_iter->next;
		}
	}
	if (carry != 0) {
		*res_iter = new node(carry, NULL);
	}
	result->sign = sign;
	result->_reverse();
	return result;
}











