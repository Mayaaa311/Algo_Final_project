
import random
import time
import math

def is_valid(solution, subsets, universe):
    covered = set()
    for idx in solution:
        covered |= subsets[idx]
    return covered == universe


def get_initial_solution(subsets, universe):
    indices = list(range(len(subsets)))
    random.shuffle(indices)
    covered = set()
    solution = []
    for idx in indices:
        if not universe.issubset(covered):
            if subsets[idx] - covered:
                solution.append(idx)
                covered |= subsets[idx]
        if covered == universe:
            break
    return solution if covered == universe else []


def get_neighbors(solution, subsets, universe, max_tries=500):
    neighbors = []
    solution_set = set(solution)
    total_subsets = len(subsets)

    for _ in range(max_tries):
        op_type = random.choice(["remove", "replace", "add"])
        
        # Try removing a subset
        if op_type == "remove" and len(solution) > 1:
            i = random.randint(0, len(solution) - 1)
            new_solution = solution[:i] + solution[i+1:]
            if is_valid(new_solution, subsets, universe):
                neighbors.append(new_solution)
                # break

        # Try replacing a subset with another not in the solution
        elif op_type == "replace" and len(solution) > 0:
            i = random.randint(0, len(solution) - 1)
            j = random.randint(0, total_subsets - 1)
            if j not in solution_set:
                new_solution = solution[:i] + [j] + solution[i+1:]
                if is_valid(new_solution, subsets, universe):
                    neighbors.append(new_solution)
                    # break

        # Try adding a new subset not already in the solution
        elif op_type == "add":
            j = random.randint(0, total_subsets - 1)
            if j not in solution_set:
                new_solution = solution + [j]
                if is_valid(new_solution, subsets, universe):
                    neighbors.append(new_solution)
                    # break
    return neighbors


def local_search_1(U, subsets, cutoff, seed):
    import time, random
    random.seed(seed)
    start_time = time.time()
    universe = set(U)

    curr_sol = get_initial_solution(subsets, universe)
    best_sol = curr_sol[:]
    best_val = len(best_sol)
    trace = [(0.0, best_val)]

    while time.time() - start_time < cutoff:
        neighbors = get_neighbors(curr_sol, subsets, universe)
        if not neighbors:
            break

        # Find the best neighbor with strictly fewer subsets
        next_sol = min(neighbors, key=lambda x: len(x))
        if len(next_sol) < len(curr_sol):
            curr_sol = next_sol
            if len(curr_sol) < best_val:
                best_sol = curr_sol[:]
                best_val = len(curr_sol)
                trace.append((round(time.time() - start_time, 6), best_val))
        else:
            break  # Local optimum reached

    return best_sol, trace

