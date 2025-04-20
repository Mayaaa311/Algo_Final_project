import random
import time
import math
import sys

def parse_input(file_path):
    with open(file_path, 'r') as f:
        n, m = map(int, f.readline().split())
        subsets = []
        for _ in range(m):
            parts = list(map(int, f.readline().split()))
            subsets.append(set(parts[1:]))
    return n, subsets

def is_valid(solution, subsets, universe):
    covered = set()
    for idx in solution:
        covered |= subsets[idx]
    return covered == universe

def get_initial_solution(subsets, universe):
    uncovered = set(universe)
    solution = []
    while uncovered:
        best_i = max(range(len(subsets)), key=lambda i: len(subsets[i] & uncovered))
        solution.append(best_i)
        uncovered -= subsets[best_i]
    return solution

def get_neighbors(solution, subsets, universe):
    neighbors = []
    for i in range(len(solution)):
        for j in range(len(subsets)):
            if j not in solution:
                new_solution = solution[:i] + [j] + solution[i+1:]
                if is_valid(new_solution, subsets, universe):
                    neighbors.append(new_solution)
    return neighbors

def objective(sol):
    return len(set(sol))

def local_search_1(U, subsets, cutoff, seed):
    import time, random, math
    random.seed(seed)
    start_time = time.time()
    universe = set(U)

    curr_sol = get_initial_solution(subsets, universe)
    best_sol = curr_sol[:]
    best_val = len(set(best_sol))

    trace = [(0.0, best_val)]
    temp = 100.0
    alpha = 0.95

    while time.time() - start_time < cutoff and temp > 1e-3:
        neighbors = get_neighbors(curr_sol, subsets, universe)
        if not neighbors:
            break
        next_sol = random.choice(neighbors)
        delta = len(next_sol) - len(curr_sol)

        if delta < 0 or random.random() < math.exp(-delta / temp):
            curr_sol = next_sol
            if len(curr_sol) < best_val:
                best_val = len(curr_sol)
                best_sol = curr_sol[:]
                trace.append((round(time.time() - start_time, 6), best_val))

        temp *= alpha

    return list(set(best_sol)), trace
