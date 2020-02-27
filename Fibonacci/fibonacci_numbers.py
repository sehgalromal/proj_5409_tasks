import time 

def calculate_fibonacci(num):
    series = [] 
    first = 0
    second = 1 
    series.append(first)
    series.append(second)
    third = first + second
    for i in range(num-2):
        series.append(third)
        first = second 
        second = third
        third = first + second 
    return series 
    


def read_numbers(file_name):
    with open("input_numbers.txt", "r", ) as input_file:
        read_lines = input_file.read().splitlines()
        rId = 1
        for i in read_lines:
            start = time.time()
            f = open("fibonacci_numbers_logs.txt", "a")
            number = int(i)
            result = calculate_fibonacci(number)
            end = time.time()
            total_time = (end - start) * 1000
            f.write(str(rId) + " " + str(i) + " " + str(result) + " " + str(round(total_time,2)) + " ms")
            f.write("\n")
            rId += 1
            
            
inputFile = "input_numbers.txt"
input_numbers = read_numbers(inputFile)

