#RemoveElement(List of Integers, Integer)
def RemoveElement(List, element):
	new_List = []
	for x in List:
		if x != element:
			new_List = new_List + element
	return new_List