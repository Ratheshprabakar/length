def check_error(input_number):
	"""
	Check type errors in the input
	"""
	if type(input_number) is str or type(input_number) is float:
		raise Exception("Input must be int")
	try:
		input_number = int(input_number)
	except:
		raise Exception("n must be integer")
def nlength(input_number):
	"""
	To find the digit count of a number
	"""
	check_error(input_number)
	count=0
	while(input_number>0):
    		count=count+1
    		input_number=input_number//10
	return count

