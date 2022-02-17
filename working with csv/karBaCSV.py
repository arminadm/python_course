import csv
# For the average
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    o = open(output_file_name, "w")
    file = csv.reader(f)
    output = csv.writer(o)
    for i in file:
        list_of_numbers = []
        name = i[0]
        for each in i[1:]:
            list_of_numbers += [int(each)]
        avr = mean(list_of_numbers)
        output.writerow([name, avr])
    f.close()
    o.close()

def calculate_sorted_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    o = open(output_file_name, "w")
    file = csv.reader(f)
    output = csv.writer(o)
    list_of_scores = dict()
    for i in file:
        list_of_numbers = []
        name = i[0]
        for each in i[1:]:
            list_of_numbers += [int(each)]
        avr = mean(list_of_numbers)
        list_of_scores[name] = avr

    items = list_of_scores.items()
    print(items)
    sorted_list = sorted(items)
    for any in sorted_list:
        output.writerow(any)
    f.close()
    o.close()


# def calculate_three_best(input_file_name, output_file_name):
    


# def calculate_three_worst(input_file_name, output_file_name):
    


# def calculate_average_of_averages(input_file_name, output_file_name):
    
if __name__ == "__main__":
    calculate_averages("task1.csv", "output.csv")