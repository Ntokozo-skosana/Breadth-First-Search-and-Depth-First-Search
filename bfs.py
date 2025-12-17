from collections import deque

def all_moves(state):
    possible_moves = []
    position_of_blank = state.index('#')
    state_list = list(state)

    moves = {}
    if position_of_blank >= 3:
       moves["UP"] = -3
    else:
       moves["UP"] = None

    if position_of_blank <= 5:
       moves["DOWN"] = 3
    else:
       moves["DOWN"] = None

    if position_of_blank % 3 != 0:
       moves["LEFT"] = -1
    else:
       moves["LEFT"] = None

    if position_of_blank % 3 != 2:
       moves["RIGHT"] = 1
    else:
       moves["RIGHT"] = None

    for move, movement in moves.items():
        if movement is not None:
            position = position_of_blank + movement
            new_state = state_list[:]
            new_state[position_of_blank], new_state[position] = ( 
               new_state[position], 
               new_state[position_of_blank],
            )
            possible_moves.append("".join(new_state))

    return possible_moves


def breath_first_search(initial_state, goal_state):
    if initial_state == goal_state:
        return 0

    track_state = set([initial_state])
    state_and_moves = deque([(initial_state, 0)]) 

    while state_and_moves:
        state, cost = state_and_moves.popleft()

        for next_state in all_moves(state):
            if next_state not in track_state:
                if next_state == goal_state:
                    return cost + 1
                track_state.add(next_state)
                state_and_moves.append((next_state, cost + 1))

    return -1  

initial_state = input()
goal_state = "12345678#"

cost = breath_first_search(initial_state, goal_state)
print(cost)
