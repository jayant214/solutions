

class special_interator:
	"""Iterates the numbers, which are divisible by 7. Both 0 and n are included for iteration."""
	def __init__(self, n):
		self.start = 0
		self.end = n

	def generate(self):
		while(self.end >= self.start):
			yield self.start
			self.start = self.start +7


def main():
	input_string = int(raw_input('Enter your input number. '))
	obj1 = special_interator(input_string)
	for i in obj1.generate():
		print i

if __name__ == '__main__':
	main()

		