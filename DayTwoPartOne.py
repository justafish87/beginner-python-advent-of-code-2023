import re

count = 1
max_red = 12
max_blue = 14
max_green = 13
red_possible = False
blue_possible = False
green_possible = False
colour_possible = False
possible_games = []


def check_max_colour(pick_colour,game_picks,max_colour):
    round = re.split('; |, ',game_picks)
    
    picks_num_cubes = []
    for pick in round:
        text_position = pick.find(pick_colour)
        if text_position > 0:
            num_cubes = int(pick[0:text_position])
            picks_num_cubes.append(num_cubes)
  
    max_cubes = max(picks_num_cubes)

    global colour_possible
    colour_possible = False
    if max_cubes < max_colour + 1:
        colour_possible = True

with open(
        "/Users/bigbird/Desktop/Python/Advent of Code/Day Two/PuzzleInputD2P1.txt"
    ) as file:
        for line in file:
            game_possible = False

            colon_position = line.find(':')
            game_num = int(line[5:colon_position])
            print(game_num)

            picks = line[(colon_position + 1):]
            print(picks)
            check_max_colour('red',picks, max_red)
            red_possible = colour_possible
            print('red:',red_possible)
            check_max_colour('blue',picks, max_blue)
            blue_possible = colour_possible
            print('blue:',blue_possible)
            check_max_colour('green',picks, max_green)
            green_possible = colour_possible
            print('green:',green_possible)

            if red_possible is True and blue_possible is True and green_possible is True:
                game_possible = True
            if game_possible is True:
                possible_games.append(game_num)
            print('game:',game_possible)


            #count = count + 1
            #if count == 15:
            #    break    

games_total = sum(possible_games)
print(possible_games)
print(games_total)