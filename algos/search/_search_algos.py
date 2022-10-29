import sys
from ..utils import memoize, PriorityQueue
from .search import Node,deque

def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue."""

    # Check if starting node == goal
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node

    # Add children of initial node to frontier
    frontier = deque([Node(problem.initial)])  # FIFO queue

    # Explore frontier
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None


def depth_first_graph_search(problem):
    """Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue."""

    # Check if starting node == goal
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node

    # Add children of initial node to frontier
    frontier = deque([Node(problem.initial)])  # LIFO queue

    explored = set()
    while frontier:
        node = frontier.pop()
        explored.add(node.state)

        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None


def depth_limited_search(problem, limit=50):

    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search_for_vis(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, limit=depth)
        if result == 'cutoff':
            print("Due to limit=%d, the goal state cannot be reached" % depth)
            continue
        else:
            iterations, all_node_colors, node = depth_limited_search(problem, limit=depth)
            return (iterations, all_node_colors, node)





# Give the cost evaluation method as parameter, then we get UCS
def uniform_cost_search(problem):
    def best_first_graph_search(problem, f):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""

        # we use these two variables at the time of visualisations
        iterations = 0

        f = memoize(f, 'f')
        node = Node(problem.initial)


        iterations += 1


        if problem.goal_test(node.state):
            iterations += 1
            return (iterations, node)

        frontier = PriorityQueue('min', f)
        frontier.append(node)


        iterations += 1

        explored = set()
        while frontier:
            node = frontier.pop()


            iterations += 1

            if problem.goal_test(node.state):
                iterations += 1
                return (iterations, node)

            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                    iterations += 1
                elif child in frontier:
                    incumbent = frontier[child]
                    if f(child) < f(incumbent):
                        del frontier[incumbent]
                        frontier.append(child)
                        iterations += 1

            iterations += 1
        return None
    return best_first_graph_search(problem, lambda node: node.path_cost)