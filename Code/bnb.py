import time
from heapq import heappush, heappop
import math


def branch_and_bound(U, subsets, cutoff, start_time,bs):
    U = set(U)
    n = len(subsets)
    best_solution = None
    best_size = bs
    log = []

    sorted_subsets = sorted(subsets, key=lambda s: len(s), reverse=True)
    subsets = sorted_subsets
    max_gain = len(subsets[0])
    least_num = math.ceil(len(U)/max_gain)
    m_gain = 0
    for i in range(0,least_num):
        m_gain+= len(subsets[i])
    max_gain=m_gain/least_num    
        
    print("max gain:",max_gain)
    
    # Stack for DFS: (cover, chosen, level)
    stack = [(set(), [], 0)]

    while stack:
        if time.time() - start_time > cutoff:
            break

        cover, chosen, level = stack.pop()

        # If even optimistic estimate is worse than current best, skip
        if len(chosen)+ math.ceil((len(U)-len(cover))/max_gain) > best_size:
            continue

        # If full cover, update best
        if cover == U and len(chosen):
            best_solution = list(chosen)
            best_size = len(chosen)
            print("current best:",best_size)
            log.append((time.time() - start_time, best_size))
            continue


        # If no more subsets
        if level >= n:
            continue

        # DFS: exclude and include branches
        # Push exclude first (so include gets explored first = DFS behavior)
        stack.append((cover, list(chosen), level + 1))  # exclude
        new_cover = cover | subsets[level]
        stack.append((new_cover, chosen + [level], level + 1))  # include

    return best_solution if best_solution is not None else [], log
