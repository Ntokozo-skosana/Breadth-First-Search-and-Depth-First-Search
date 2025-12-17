def all_moves(state):
    """Generate all valid neighboring states from the current state."""
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

    next_states = []
    for move, movement in moves.items():
        if movement is not None:
            pos = position_of_blank + movement
            new_state = state_list[:]
            new_state[position_of_blank], new_state[pos] = (
                new_state[pos],
                new_state[position_of_blank],
            )
            next_states.append((move, "".join(new_state)))
    return next_states

def depth_first_search(initial_state, goal_state):
    """Perform DFS to find a path from initial to goal state."""
    if initial_state == goal_state:
        return 0
    
    # Stack stores tuples of (state, cost)
    stack = [(initial_state, 0)]
    visited = set()
    
    while stack:
        state, cost = stack.pop()
        
        if state in visited:
            continue
            
        visited.add(state)
        
        if state == goal_state:
            return cost
        
        # Generate all neighbors and add to stack
        for move, next_state in all_moves(state):
            if next_state not in visited:
                step_cost = 5 if move == "UP" else 1
                new_cost = cost + step_cost
                stack.append((next_state, new_cost))
    
    # If no solution found
    return -1

# Read input
initial_state = input().strip()
goal_state = input().strip()

# Perform DFS and output the result
result = depth_first_search(initial_state, goal_state)
print(result)