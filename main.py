import test
import array_generator
import psutil

def main():
	print("Start program\nMemory info: " , psutil.virtual_memory(), "\n")
	array_generator.generate_arrays(50000) #50000 elements
	test.test_all()


main()