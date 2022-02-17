# Armin Darabi Mahboub

# inputs:
how_many_data = int(input())
list_of_data = [None] * how_many_data

for i in range(how_many_data):
    list_of_data[i] = list(map(int, input().strip().split()))[:2]

# calculation:
irsa_mood = False
for each in list_of_data:
    for others in range(how_many_data):
        if each[0] < list_of_data[others][0] and each[1] > list_of_data[others][1]:
            irsa_mood = True
            break

# output:
if (irsa_mood):
    print("happy irsa")
else:
    print("poor irsa")