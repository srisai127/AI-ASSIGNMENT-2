import heapq

class MissionariesCannibals:

    def __init__(self):
        self.start = (3, 3, 0)
        self.goal = (0, 0, 1)

    def is_valid(self, state):
        m, c, boat = state

        # Check boundaries
        if m < 0 or c < 0 or m > 3 or c > 3:
            return False

        m_right = 3 - m
        c_right = 3 - c

        # Missionaries should not be outnumbered
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
                successors.append((new_state, 1))  # cost = 1 per move

        return successors


def ucs(problem):
    priority_queue = []
    heapq.heappush(priority_queue, (0, [problem.start]))  # (cost, path)

    visited = {}

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        state = path[-1]

        if state == problem.goal:
            return path, cost

        if state not in visited or cost < visited[state]:
            visited[state] = cost

            for next_state, step_cost in problem.get_successors(state):
                heapq.heappush(priority_queue,
                               (cost + step_cost, path + [next_state]))

    return None, None


if __name__ == "__main__":
    problem = MissionariesCannibals()
    solution, total_cost = ucs(problem)

    print("UCS Solution:")
    for step in solution:
        print(step)

    print("Total Cost:", total_cost)
