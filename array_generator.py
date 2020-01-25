import random
import pickle
import os

def generate_arrays(dim):
	try:
		os.mkdir("db")
	except FileExistsError:
		print("Directory already exist")
		pass	
	file_name = "db/ascending_ordered_array.txt"
	file = open(file_name, 'wb+')
	for i in range (0, dim):
		pickle.dump(i, file)
	file.close()

	file_name = "db/random_array.txt"
	file = open(file_name, 'wb+')
	for i in range (0, dim):
		pickle.dump(random.randrange(0, 10000), file)
	file.close()

	file_name = "db/descending_ordered_array.txt"
	file = open(file_name, 'wb+')
	for i in range(0, dim):
		pickle.dump(dim-i, file)
	file.close()