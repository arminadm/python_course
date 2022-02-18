#Armin Darabi Mahboub
import csv
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    f = open(input_file_name, "r")
    o = open(output_file_name, "w", newline='')
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
    f = open(input_file_name, "r")
    o = open(output_file_name, "w", newline='')
    file = csv.reader(f)
    output = csv.writer(o)
    dict_of_scores = dict()
    for i in file:
        list_of_numbers = []
        name = i[0]
        for each in i[1:]:
            list_of_numbers += [int(each)]
        avr = mean(list_of_numbers)
        dict_of_scores[name] = avr
    sorted_scores = sorted(dict_of_scores.items(), key=lambda x: x[1], reverse=False)
    for each in sorted_scores:
        output.writerow(each)
    f.close()
    o.close()


def calculate_top_three(input_file_name, output_file_name):
    f = open(input_file_name, "r")
    o = open(output_file_name, "w", newline='')
    file = csv.reader(f)
    output = csv.writer(o)
    dict_of_scores = {}
    for i in file:
        dict_of_scores[i[0]] = float(i[1])
    top_three = sorted(dict_of_scores.items(), key= lambda x: x[1], reverse=True)
    for each in top_three[0:3]:
        output.writerow(each)
    f.close()
    o.close()

def calculate_last_three(input_file_name, output_file_name):
    f = open(input_file_name, "r")
    o = open(output_file_name, "w", newline='')
    file = csv.reader(f)
    output = csv.writer(o)
    counter = 0
    for each in file:
        if (counter < 3):
            counter += 1
            output.writerow([each[1]])
        else:
            return
    f.close()
    o.close()

def calculate_average_of_averages(input_file_name, output_file_name):
    f = open(input_file_name, "r")
    o = open(output_file_name, "w")
    file = csv.reader(f)
    output = csv.writer(o)
    list_of_numbers = []
    for i in file:
        list_of_numbers += [float(i[1])]
    output.writerow([mean(list_of_numbers)])
    f.close()
    o.close()
    
if __name__ == "__main__":
    calculate_averages("input.csv", "averages.csv")
    calculate_sorted_averages("input.csv", "sorted_averages.csv")
    calculate_top_three("sorted_averages.csv", "top_three.csv")
    calculate_last_three("sorted_averages.csv", "last_three.csv")
    calculate_average_of_averages("sorted_averages.csv", "average_of_averages.csv")
