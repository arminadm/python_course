# Armin Darabi Mahboub

from math import sqrt

def main():
    # INPUT:
    userInputs = [None] * 10
    for i in range(10):
        userInputs[i] = int(input())

    # Counting each number's prime factors and save them into dictionary
    records = dict()
    for i in range(10):
        records[userInputs[i]] = primeFactors(userInputs[i])

    # OUTPUT:
    greatast = greatestFinder(records)
    print(f"{greatast[0]} {greatast[1]}")

# returns the counts of prime numbers for each given number
def primeFactors(number):
    primeFactorCounter = 0
    # first we get all of the possible twos to make the number odd
    while(number % 2 == 0):
        primeFactorCounter += 1
        number /= 2
    
    # going 2 step throw all of the factors that can be number's prime
    """
    the point is, when we are going throw numbers and check each one
    to see if it has zero remainder, the smallest number which fits
    the situation is prime for sure(only if you're divid numbers in sorted
    from low to great)
    """
    for factor in range(3, int(sqrt(number)) + 1, 2):
        while(number % factor == 0):
            primeFactorCounter += 1
            number /= factor

    # remainder is it's own prime factor
    if (number > 2):
        primeFactorCounter += 1

    return primeFactorCounter

# returns the number which has the most prime factors and is bigger than others
def greatestFinder(records):
    temp_list = sorted(((value, key) for (key, value) in records.items()), reverse=True)
    print(temp_list)
    most_factor = (max(sorted(((value, key) for (key, value) in records.items()), reverse=True)))[0]
    
    candidates = {}
    for tops in temp_list:
        if(tops[0] == most_factor):
            candidates[tops[1]] = tops[0]
    
    return max(sorted((key, value) for (key, value) in candidates.items()))

if __name__ == "__main__":
    main()