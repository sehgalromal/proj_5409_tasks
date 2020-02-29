import random 
import time 

def generate_random_integers(N):
    with open("input_numbers.txt", "w") as gen_integer_file:
        fact_numbers = [] 
        for number in range(1, N):
            fact_numbers.append(number)
            random.shuffle(fact_numbers)
           
        for num in fact_numbers:
            gen_integer_file.write(str(num))
            gen_integer_file.write("\n")

N = 100
generate_random_integers(N)

def calculate_factorial(num):
    counter = num
    fact = 1
    while counter !=0 :
        fact = fact*counter
        time.sleep(0.002)
        counter -= 1
    return fact

def read_numbers(file_name):
    with open(file_name, "r", ) as input_file:
        read_lines = input_file.read().splitlines()
        rId = 1
        for i in read_lines:
            start = time.time()
            f = open("factorial_logs.txt", "a")
            number = int(i)
            result = calculate_factorial(number)
            end = time.time()
            total_time = (end - start) * 1000
            f.write(str(rId) + " " + str(i) + " " + str(result) + " " + str(round(total_time,2)) + "s")
            f.write("\n")
            rId += 1

inputFile = "input_numbers.txt"
input_numbers = read_numbers(inputFile)


        
        


