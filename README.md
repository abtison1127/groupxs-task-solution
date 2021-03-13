# groupxs-task-solution
bug: it seems that the any() statement was not accurate(line:14), thus the while loop becomes infinite
(suggestions are encouraged)

# psuedo code:

	input number of copies of books into array1

	while array1 has values more than 0   

		declare empty array2 //clears array to give way for more sets if there are any//
		subtract 1 from every index more than 0 in old array
		add 1 value for every index taken from old array to array2 //new array to determine number of books in a set//
		take array2, add all indexes for price, then apply discount based on length of array2
	
	output price

