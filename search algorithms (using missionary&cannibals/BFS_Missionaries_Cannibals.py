
from collections import deque

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


def bfs(problem):
    frontier = deque([[problem.start]])
    explored = set()

    while frontier:
        path = frontier.popleft()
        state = path[-1]

        if state == problem.goal:
            return path

        if state not in explored:
            explored.add(state)
            for child in problem.get_successors(state):
                frontier.append(path + [child])

    return None


if __name__ == "__main__":
    problem = MissionariesCannibals()
    solution = bfs(problem)

    print("BFS Solution:")
    for step in solution:
        print(step)
