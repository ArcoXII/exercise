import random

grid_size = 5

player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
# print(player_position)

treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

not_same_position = True

while not_same_position:
    if player_position == treasure_position:
        treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)] #Same logic as above
    else:
        not_same_position = False
# print(treasure_position)

paired_list = list(zip(player_position, treasure_position))

tamp_distance = 0
distance = 0

for player, treasure in paired_list:
    tamp_distance = abs(player - treasure)
    distance = tamp_distance + distance

# print(distance)



line_count = 0

sample_line = ['·','·','·','·','·']
sample_line_copy = ['·','·','·','·','·']

f1 = True
f2 = True
f3 = False
f4 = True
f5 = False

life_count = 10

direction = ''

while f1:

    if life_count == 0:
        if treasure_position[0] == player_position[0]:
            if treasure_position[1] < player_position[1]:
                if line_count < grid_size:
                    if line_count == treasure_position[0]:
                        sample_line.insert(treasure_position[1], 'T')
                        del sample_line[-1]
                        sample_line.insert(player_position[1], 'P')
                        del sample_line[-1]
                        print(' '.join(sample_line))
                        sample_line = ['·','·','·','·','·']
                        line_count += 1
                        continue
                    else:
                        print(' '.join(sample_line_copy))
                        line_count += 1
                        continue
                elif line_count == grid_size:
                    print("You did not find the treasure, see you next time! ")
                    f1 = False
                    break
            else:
                if line_count < grid_size:
                    if line_count == player_position[0]:
                        sample_line.insert(player_position[1], 'P')
                        del sample_line[-1]
                        sample_line.insert(treasure_position[1], 'T')
                        del sample_line[-1]
                        print(' '.join(sample_line))
                        sample_line = ['·','·','·','·','·']
                        line_count += 1
                        continue
                    else:
                        print(' '.join(sample_line_copy))
                        line_count += 1
                        continue
                elif line_count == grid_size:
                    print("You did not find the treasure, see you next time! ")
                    f1 = False
                    break
        else:
            if line_count < grid_size:
                if line_count == player_position[0]:
                    sample_line.insert(player_position[1], 'P')
                    del sample_line[-1]
                    sample_line.insert(treasure_position[1], 'T')
                    del sample_line[-1]
                    print(' '.join(sample_line))
                    sample_line = ['·','·','·','·','·']
                    line_count += 1
                    continue
                else:
                    print(' '.join(sample_line_copy))
                    line_count += 1
                    continue
            elif line_count == grid_size:
                print("You did not find the treasure, see you next time! ")
                f1 = False
                break
    else:
        if line_count < grid_size:
            if line_count == player_position[0]:
                sample_line.insert(player_position[1],'P')
                del sample_line[-1]
                print(' '.join(sample_line))
                sample_line = ['·','·','·','·','·']
                line_count += 1
                continue
            else:
                print(' '.join(sample_line_copy))
                line_count += 1
                continue


    while f3:
        paired_list = list(zip(player_position, treasure_position))
        last_distance = distance
        tamp_distance = 0
        distance = 0
        for player, treasure in paired_list:
            tamp_distance = abs(player - treasure)
            distance = tamp_distance + distance
        print(treasure_position)
        print(player_position)
        print(distance)
        while f4:
            if distance != 0:
                if last_distance > distance:
                    print("You are getting close to the treasure! ")
                    f3 = False
                    f4 = False
                    continue
                elif last_distance < distance:
                    print("You are getting far from the treasure! ")
                    f3 = False
                    f4 = False
                    continue
            elif distance == 0:
                print("Congratulations! You get the treasure! ")
                f1 = False
                f2 = False
                f3 = False
                f4 = False
                break
            else:
                print(last_distance, distance)   
                f3 = False
                f4 = False
                break  

    while f2:
        direction = input(f"Moves left: {life_count}""\nEnter a direction to move(N, S, W, E): ")
        life_count -= 1
        line_count = 0
        f3 = True
        f4 = True
        if direction == 'N':
            if player_position[0] - 1 > -1:
                player_position[0] = player_position[0] - 1
                break
        elif direction == 'S':
            if player_position[0] + 1 < 5:
                player_position[0] = player_position[0] + 1
                break
        elif direction == 'W':
            if player_position[1] - 1 > -1:
                player_position[1] = player_position[1] - 1
                break
        elif direction == 'E':
            if player_position[1] + 1 < 5:
                player_position[1] = player_position[1] + 1
                break
        else:
            print('Invalid input, please try again (N, S, W, E)')
            life_count += 1
            continue
        life_count += 1
        print('You reached edge, please try again (N, S, W, E)')
    continue

    
