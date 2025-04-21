import random
import time
import math

def is_valid(solution, subsets, universe):
    covered = set()
    for idx in solution:
        covered |= subsets[idx]
    return covered == universe

def get_random_initial_solution(subsets, universe):
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


def objective(sol):
    return len(set(sol))

def acceptance_probability(curr_val, next_val, temperature):
    if next_val < curr_val:
        return 1.0
    else:
        return math.exp((curr_val - next_val) / temperature)

def local_search_2(U, subsets, cutoff, seed,
                   initial_temp=100.0, cooling_rate=0.95,
                   min_temp=1e-3, max_no_improve=200):
    
    random.seed(seed)
    start_time = time.time()
    universe = set(U)

    curr_sol = get_random_initial_solution(subsets, universe)
    if not curr_sol:
        return [], []  # Could not find valid initial solution

    best_sol = curr_sol[:]
    best_val = objective(best_sol)
    trace = [(0.0, best_val)]

    temperature = initial_temp
    no_improve_count = 0

    while time.time() - start_time < cutoff and temperature > min_temp and no_improve_count < max_no_improve:
        neighbors = get_neighbors(curr_sol, subsets, universe)
        if not neighbors:
            no_improve_count += 1
            continue

        next_sol = random.choice(neighbors)
        next_val = objective(next_sol)
        curr_val = objective(curr_sol)

        if random.random() < acceptance_probability(curr_val, next_val, temperature):
            curr_sol = next_sol
            if next_val < best_val:
                best_sol = next_sol[:]
                best_val = next_val
                trace.append((round(time.time() - start_time, 6), best_val))
                no_improve_count = 0
            else:
                no_improve_count += 1
        else:
            no_improve_count += 1

        temperature *= cooling_rate

    return list(set(best_sol)), trace