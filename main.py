import test
import array_generator

def main():
	array_generator.generate_arrays(25000) #25000 elements
	test.test_all()


main()