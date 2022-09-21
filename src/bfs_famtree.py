def bfs(visited, queue, head):
    # This bfs function assumes that head[0]
    # is the root node. The second value of the tuple
    # is a list consisting of the children of the root
    # node, each consisting of itself and their children.
    # This pattern goes on indefinitely, which prompts
    # the requirement for some sort of loop.

    # To start the search, we add the root node to the
    # visited list, as well as its children to the queue.
    visited.append(head[0])
    queue.append(head[1])

    # Use a while loop to continuously loop while queue
    # is not empty. A non-empty queue signifies that there
    # are still children nodes that needs to be visited,
    # while an empty queue signifies that there are no
    # more nodes left in the queue to visit.
    while queue:
        # Get the children, and their subsequent 
        # children, of the previous node.
        children = queue.pop(0)

        for child in children:
            # Don't think they will be visited twice, but just 
            # in case, we will try to go to the next iteration
            # directly since we do not want to re-add visited nodes.
            if child[0] in visited:
                continue

            # The children nodes are visited according to their
            # specified order. After which, the children of the
            # current child node are then added to the queue.
            visited.append(child[0])
            queue.append(child[1])


def get_family_members(head):
    visited = []
    queue = []

    bfs(visited, queue, head)
    return visited


## Testing functions...
def is_correct(expected, actual):
    if len(actual) != len(expected):
        print(f"Expected len {len(expected)} but got len {len(actual)}.")

    counter = 0
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            counter += 1
        else:
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


h1 = ('Mary', [])
h2 = ('Jane', [('Nick', []), ('Wendy', [])])
h3 = ('Frank', [('Mary', []), ('Jane', [('Nick', [])])])
h4 = ('Alan', [('Bob', [('Chris', [])]), ('Eric', [])])
h5 = ('Alan', [('Bob', [('Chris', []), ('Debbie', [('Cindy', [])])]), ('Eric', [('Dan', []), ('Fanny', [('George', [])])]), ('Hannah', [])])

expected_a1 = ['Mary']
expected_a2 = ['Jane', 'Nick', 'Wendy']
expected_a3 = ['Frank', 'Mary', 'Jane', 'Nick']
expected_a4 = ['Alan', 'Bob', 'Eric', 'Chris']
expected_a5 = ['Alan', 'Bob', 'Eric', 'Hannah', 'Chris', 'Debbie', 'Dan', 'Fanny', 'Cindy', 'George']

a1 = get_family_members(h1)
a2 = get_family_members(h2)
a3 = get_family_members(h3)
a4 = get_family_members(h4)
a5 = get_family_members(h5)
expected_answers = [expected_a1, expected_a2, expected_a3, expected_a4, expected_a5]
answers = [a1, a2, a3, a4, a5]
check_results(expected_answers, answers)
