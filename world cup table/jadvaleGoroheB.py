# Armin Darabi Mahboub

# Global variables
win = [0] * 4
lose = [0] * 4
draw  = [0] * 4
goal_difference = [0] * 4
points = [0] * 4
name = ["Iran", "Spain", "Portugal", "Morocco"]
# 0 = iran
# 1 = spain
# 2 = portugal
# 3 = morocco

def main():

    """INPUT"""
    # iran-spain
    # iran-portugal
    # iran-morocoo
    # spain-portugal
    # spain-morocoo
    # portugal-morocoo

    result = [None] * 6
    for i in range(6):
        result[i] = input()
    
    """calculation"""
    # making our data clear
    data = clear_data(result)
    # getting all of the required information from data(win,lose,draw,difference,points) using GLOBAL VARIABLES 
    calculation(data) 
    # setting output into required order (1-points 2-wins 3-alphabet)
    ordered_list = order()

    """"print"""
    printing(ordered_list)


# count wins, draws, loses, points and goal differences for each team
def calculation(data):
    # data: iran - spain - portugal - morocoo
    """counting"""
    for team in range(4):
        for game in range(3):
            team1_score = int(data[team][game].split("-")[0])
            team2_score = int(data[team][game].split("-")[1])
            
            # winning
            if team1_score - team2_score > 0:
                win[team] += 1
            
            # draw
            elif team1_score - team2_score == 0:
                draw[team] += 1
            
            # lose
            else:
                lose[team] += 1

            # goal difference
            goal_difference[team] += team1_score - team2_score
    
    # points
    for team in range(4):
        points[team] = 3 * win[team] + draw[team]

# making data table clear and ready for each team
def clear_data(result):
    records = [None] * 4
    # iran games
    records[0] = [result[0], result[1], result[2]]
    
    # spain games
    spain, iran = result[0].split("-")[1], result[0].split("-")[0] 
    records[1] = [f"{spain}-{iran}", result[3], result[4]]

    # portugal games
    portugal1, iran = result[1].split("-")[1], result[1].split("-")[0]
    portugal2, spain = result[3].split("-")[1], result[3].split("-")[0]
    records[2] = [f"{portugal1}-{iran}", f"{portugal2}-{spain}", result[5]]

    # morocoo
    morocoo1, iran = result[2].split("-")[1], result[2].split("-")[0]
    morocoo2, spain = result[4].split("-")[1], result[4].split("-")[0]
    morocoo3, portugal = result[5].split("-")[1], result[5].split("-")[0]
    records[3] = [f"{morocoo1}-{iran}", f"{morocoo2}-{spain}", f"{morocoo3}-{portugal}"]

    return records

# setting output into required order
def order():
    temp = [None] * 4
    for team in range(4):
        temp[team] = [f"{points[team]}", f"{win[team]}", f"{name[team]}", f"{lose[team]}", f"{goal_difference[team]}", f"{draw[team]}"]
    ordered = sorted(temp, key=lambda x: (-int(x[0]), int(x[1]), x[2]))
    return ordered

# printing the final result in ordered place
def printing(list):
    for team in range(4):
        print(f"{list[team][2]} wins:{list[team][1]} , loses:{list[team][3]} , draws:{list[team][5]} , goal difference:{list[team][4]} , points:{list[team][0]}")

if __name__ == "__main__":
    main()