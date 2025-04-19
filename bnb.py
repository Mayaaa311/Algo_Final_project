import time
def branch_and_bound(U, subsets, cutoff, start_time):
    n = len(U)
    best_solution = list(range(len(subsets)))  # start with all sets
    best_cost = len(best_solution)
    trace = [(0.0, best_cost)]
    
    # Naive: enumerate subsets
    from itertools import combinations
    for r in range(1, len(subsets)+1):
        for comb in combinations(range(len(subsets)), r):
            if time.time() - start_time > cutoff:
                return best_solution, trace
            
            covered = set()
            for idx in comb:
                covered.update(subsets[idx])
            if covered == U and r < best_cost:
                best_solution = list(comb)
                best_cost = r
                trace.append((round(time.time() - start_time, 2), best_cost))
                break

    return best_solution, trace
