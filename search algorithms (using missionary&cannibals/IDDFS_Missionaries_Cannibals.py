
class MissionariesCannibals:

    def __init__(self):
        self.start = (3, 3, 0)
        self.goal = (0, 0, 1)

    def is_valid(self, state):
        m, c, boat = state

        if m < 0 or c < 0 or m > 3 or c > 3:
            return False

        m_right = 3 - m
        c_right = 3 - c

        if (m > 0 and m < c):
            return False
        if (m_right > 0 and m_right < c_right):
            return False

        return True

    def get_successors(self, state):
        m, c, boat = state
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        successors = []

        for move in moves:
            if boat == 0:
                new_state = (m - move[0], c - move[1], 1)
            else:
                new_state = (m + move[0], c + move[1], 0)

            if self.is_valid(new_state):
                successors.append(new_state)

        return successors


def depth_limited_search(problem, limit):

    def recursive_dls(path, depth):
        state = path[-1]

        if state == problem.goal:
            return path

        if depth == limit:
            return None

        for child in problem.get_successors(state):
            if child not in path:
                result = recursive_dls(path + [child], depth + 1)
                if result:
                    return result
        return None

    return recursive_dls([problem.start], 0)


def iterative_deepening(problem, max_depth):
    for depth in range(max_depth):
        result = depth_limited_search(problem, depth)
        if result:
            return result
    return None


if __name__ == "__main__":
    problem = MissionariesCannibals()
    solution = iterative_deepening(problem, 20)

    print("Iterative Deepening DFS Solution:")
    for step in solution:
        print(step)
