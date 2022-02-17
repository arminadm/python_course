#Armin Darabi Mahboub

def main():
    """Inputs"""
    #Group A
    numberOfA = int(input())
    A_age = list(input().split())
    A_height = list(input().split())
    A_weight = list(input().split())
    #Group B
    numberOfB = int(input())
    B_age = list(input().split())
    B_height = list(input().split())
    B_weight = list(input().split())


    """Classes"""
    class GroupA:
        age_counter = 0.0
        height_counter = 0.0
        weight_counter = 0.0
        def __init__(self, age, height, weight):
            self.age = age
            self.height = height
            self.weight = weight
            GroupA.age_counter += float(self.age)
            GroupA.height_counter += float(self.height)
            GroupA.weight_counter += float(self.weight)
    class GroupB:
        age_counter = 0.0
        height_counter = 0.0
        weight_counter = 0.0
        def __init__(self, age, height, weight):
            self.age = age
            self.height = height
            self.weight = weight
            GroupB.age_counter += float(self.age)
            GroupB.height_counter += float(self.height)
            GroupB.weight_counter += float(self.weight)


    """Calculation"""
    #Making A group data
    person = [None] * numberOfA
    for i in range(numberOfA):
        person[i] = GroupA(A_age[i], A_height[i], A_weight[i])

    #Making B group data
    person = [None] * numberOfB
    for i in range(numberOfB):
        person[i] = GroupB(B_age[i], B_height[i], B_weight[i])
    

    """Output"""
    #Age average for groupA
    print(GroupA.age_counter / numberOfA)
    #Height average for groupA
    print(GroupA.height_counter / numberOfA)
    #Height average for groupA
    print(GroupA.weight_counter / numberOfA)

    #Age average for groupB
    print(GroupB.age_counter / numberOfB)
    #Height average for groupB
    print(GroupB.height_counter / numberOfB)
    #Height average for groupB
    print(GroupB.weight_counter / numberOfB)

    #A or B? (decision by height), if height is same, winner is the group with less weight
    if (GroupA.height_counter > GroupB.height_counter):
        print("A")
    elif (GroupA.height_counter < GroupB.height_counter):
        print("B")
    else:
        if (GroupA.weight_counter < GroupB.weight_counter):
            print("A")
        elif (GroupA.weight_counter > GroupB.weight_counter):
            print("B")
        else:
            print("Same")

    

if __name__ == "__main__":
    main()