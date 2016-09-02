#include "bigNum.h"

int main() {
	bigNum* bn = new bigNum(-2147483647);
	bigNum* bn2 = new bigNum(-2147483647);
	bigNum* result = *bn + *bn2;
	result->print();
}