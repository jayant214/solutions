

def sort_tuples(arr):
	arr.sort(key= lambda tup: (tup[0],tup[1],tup[2]))
	return arr


def main():
	#input_arr will be a list of tuples
	input_arr=[] 
	while(True):
		#Assumption: User will give valid input. A string containing 3 values separated by comma with no space in between. 
		input_string = raw_input('Enter your input. Enter "exit" to finish. ')
		input_string= input_string.strip()
		if (input_string.lower()=='exit'):
			break
		else:
			input_arr.append(tuple(input_string.split(',')))
	
	result_arr= sort_tuples(input_arr)
	for el in result_arr:
		print(el)

if __name__ == '__main__':
	main()