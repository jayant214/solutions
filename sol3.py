
import math

def distance(x,y):
	dist= math.sqrt(x*x + y*y)
	#calculate nearest integer
	floor= int(dist)
	ceiling = floor+1
	if((ceiling-dist)> (dist-floor)):
		dist= floor
	else:
		dist = ceiling
	return dist
	

def get_coordinates(arr):
	x=0
	y=0
	for el in arr:
		el= el.strip().lower().split(' ')
		if(el[0]=='up'):
			y= y+int(el[1])
		elif(el[0]=='down'):
			y= y- int(el[1])
		elif(el[0]=='right'):
			x= x+ int(el[1])
		elif(el[0]=='left'):
			x= x- int(el[1])
	return x,y


def main():
	input_arr=[] 
	while(True):
		#Assumption: User will give valid input. A string containing separated by space and a number
		input_string = raw_input('Enter your input. Enter "exit" to finish. ')
		input_string= input_string.strip()
		if (input_string.lower()=='exit'):
			break
		else:
			input_arr.append(input_string)

	x,y= get_coordinates(input_arr)
	dist = distance(x,y)
	print dist
	
	

if __name__ == '__main__':
	main()