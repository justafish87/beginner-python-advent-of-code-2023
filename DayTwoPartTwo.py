import re

count = 1
max_cubes = 0
games_power = []


def check_max_colour(pick_colour,game_picks):
    round = re.split('; |, ',game_picks)
    
    picks_num_cubes = []
    for pick in round:
        text_position = pick.find(pick_colour)
        if text_position > 0:
            num_cubes = int(pick[0:text_position])
            picks_num_cubes.append(num_cubes)
  
    global max_cubes
    max_cubes = max(picks_num_cubes)




with open(
        "/Users/bigbird/Desktop/Python/Advent of Code/Day Two/PuzzleInputD2P1.txt"
    ) as file:
        for line in file:
            game_power = 0

            colon_position = line.find(':')
            game_num = int(line[5:colon_position])
            print(game_num)

            picks = line[(colon_position + 1):]
            check_max_colour('red',picks)
            red_max = max_cubes
            check_max_colour('blue',picks)
            blue_max = max_cubes
            check_max_colour('green',picks)
            green_max = max_cubes

            game_power = red_max * blue_max * green_max
            games_power.append(game_power)


            #count = count + 1
            #if count == 15:
            #    break    

games_total = sum(games_power)
print(games_power)
print(games_total)