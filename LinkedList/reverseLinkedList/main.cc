#include "reverseLinkedList.h"
#include <stdlib.h>
#include <iostream>

int main() {
	llist* ll = new llist();
	ll->first = new node(1, new node(2, new node(3, NULL)));
	ll->Print();
	ll->Reverse();
	std::cout<<std::endl<<"reverse"<<std::endl;
	ll->Print();
}