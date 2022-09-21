
'''
    This file was created with the intention of better understanding how
    DFS works. The DFS was used to tackle one of questions in my school's
    Lab Test.

    In a nutshell, DFS works by traversing through all possible nodes given
    a starting point. Traditionally, when a node has been visited, a corresponding
    attribute will be updated. (eg node.visited = True) In this example, I added
    them to a list instead. At the end of the day, they serve the same purpose.

    For this question, I was required to return a list of all possible stations, 
    or nodes, given the maximum number of steps you can take. For instance, if
    the maximum steps I can take is 2, I need to return all the stations I can
    reach within 2 stops, inclusive of the stations that can be reached in 1 stop. 
'''

def dfs(visited: list, neighbours: dict, node: str, origin: str, steps: int):
    # If the steps are 0, it means that we can't move anymore.
    # If the node is found in the visited list, it means that
    # it has already been visited.

    # These two cases mean that there is no need to evaluate
    # the current node. Hence, the function can return.
    if steps == 0 or node in visited:
        return
    
    # Add the current node to the list. If it reaches this point,
    # it means that the node is new and that there are still steps
    # that need to be taken.
    visited.append(node)

    # Check if it's the starting node. If it is, we do not want to amend
    # the step counter because the search has not began yet, and adjusting
    # the step when the search has not started will mean that we are searching
    # with one less step, returning the answers with missing final stations.

    # If it's not, then we can safely assume that the search has began,
    # and we need to reduce the step to signify that we have moved a station.
    if node != origin:
        steps -= 1
    
    # For each neighbour of the current node,
    # we will run it through the dfs again.
    for neighbour in neighbours[node]:
        dfs(visited, neighbours, neighbour, origin, steps)


def find_stations_within_distance(mrt_map: list, orig: str, dist: int):
    # mrt_map [[...], [...], [...]]
    # mrt_map is a list of lines.
    # line is a list of stations.

    mrt_dict = {}

    # Therefore, we need a nested for-loop to access the station
    # itself. At this step, I'll be adding them to a dictionary.
    # The goal here is to add them to a list in such a way that
    # for each station, represented as a key, it keeps note of
    # the 7neighbours, represented as the value to that key.
    for line in mrt_map:
        for station in line:
            # Getting the index of the station for that
            # specific line, so we can get its neighbours.
            idx = line.index(station)
            # Setting the limits to the corner indexes.
            # This is to prevent a negative index, or
            # an index that is out of range.
            # eg: imagine idx of station is 0.
            # It would not have a left neighbour.
            left = max(0, idx - 1)
            right = min(len(line) - 1, idx + 1)
            # Initialising the key if it does not exist.
            if station not in mrt_dict:
                mrt_dict[station] = []
            
            # Checking the limits. If left is less than the idx,
            # it represents that there is a neighbour on the left.
            if left < idx:
                mrt_dict[station].append(line[left])
            
            # Similarly for the right index. If right is more than the idx,
            # it represents that there is a neighbour on the right.
            if right > idx:
                mrt_dict[station].append(line[right])
    
    # Create a visited list to store all the stations
    # that have been "visited", or accounted for.
    # This list is what we will be returning at the
    # end of the function.
    visited = []

    # Run it through the depth-first search function
    # for it to recursively get all the neighbours
    # based on the number of steps and update the
    # visited list.
    dfs(visited, mrt_dict, orig, orig, dist)

    return [x for x in visited if x != orig]


## Testing...
mrt_map = [
            ['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'],
            ['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'],
            ['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng'],
        ]

def is_correct(expected, actual):
    if len(actual) != len(expected):
        print(f"Expected len {len(expected)} but got len {len(actual)}.")
        return False

    counter = 0
    for x in expected:
        if x in actual:
            counter += 1
        else:
            print(f"{x} not in {actual}")
            return False
    
    return counter == len(expected)


def check_results(expected_answers: list, answers: list):
    num_correct = 0
    max = len(expected_answers)
    if len(expected_answers) != len(answers):
        print("Number of expected answers do not match number of answers.")
        return
    
    for i in range(len(expected_answers)):
        ea = expected_answers[i]
        a = answers[i]
        print(f"CASE {i+1}")
        print(f"Expected answer: {ea}")
        print(f"Actual answer:   {a}")
        correct = is_correct(ea, a)
        if correct:
            num_correct += 1
        print(f"Answer is correct: {correct}\n")
    
    print(f"Total score: {num_correct} out of {max} ({(num_correct/max) * 100}%).")


expected_a1 = ['Stevens', 'Newton']
expected_a2 = ['Farrer Park', 'Newton', 'Rochor', 'Dhoby Ghaut']
expected_a3 = ['Little India', 'Farrer Park', 'Boon Keng', 'Rochor', 'Newton', 'Stevens', 'Novena']
expected_a4 = ['Botanic Gardens', 'Stevens', 'Newton', 'Rochor', 'Novena', 'Toa Payoh', 'Braddell', 'Dhoby Ghaut', 'Farrer Park', 'Boon Keng']

a1 = find_stations_within_distance(mrt_map, 'Botanic Gardens', 2)
a2 = find_stations_within_distance(mrt_map, 'Little India', 1)
a3 = find_stations_within_distance(mrt_map, 'Dhoby Ghaut', 3)
a4 = find_stations_within_distance(mrt_map, 'Little India', 4)
expected_answers = [expected_a1, expected_a2, expected_a3, expected_a4]
answers = [a1, a2, a3, a4]
check_results(expected_answers, answers)