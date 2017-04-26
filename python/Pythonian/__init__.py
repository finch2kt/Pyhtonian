class Calculate:
	
	counter = 0
	size = int( input("Please enter size of the list"))
	list1 = []
	print("you printed " + str(size))
	while counter < size:
		value = input("Please enter the values you would like to be added")
		list1.append(value)
		counter += 1
		
def addArray(a):
		add = 0
		if len(a) > 0:
			for integers in range(len(a)):
				add += int(a[integers])
				
		string = "The total is %.2f" % (add)
		return string
	      
first = Calculate()
print(addArray(first.list1))
print(first.list1)