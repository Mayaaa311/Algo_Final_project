import sys
import time
import os
from bnb import branch_and_bound
from approx import greedy_set_cover
from ls1 import local_search_1
from ls2 import local_search_2

def read_instance(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        n, m = map(int, lines[0].split())
        subsets = []
        for line in lines[1:]:
            nums = list(map(int, line.strip().split()))
            subsets.append(set(nums[1:]))
    U = set(range(1, n+1))
    return U, subsets

def write_solution(path, selected):
    with open(path, 'w') as f:
        f.write(str(len(selected)) + '\n')
        f.write(' '.join(str(i) for i in sorted(selected)) + '\n')

def write_trace(path, trace):
    with open(path, 'w') as f:
        for t, q in trace:
            f.write(f"{t} {q}\n")



def evaluate(filename, method, cutoff, seed=None,basefolder = "outfile"):
    os.makedirs(basefolder, exist_ok=True)
    U, subsets = read_instance(filename)
    start_time = time.time()
    trace = []
    
    if method == "BnB":
        Approx = "Approx"
        base = os.path.splitext(os.path.basename(filename))[0]
        best_file = f"{basefolder}/{base}_{Approx}_{60}.sol" 
        with open(best_file, 'r') as file:
            first_line = file.readline()
            best_size = int(first_line.strip().split()[0])
        solution, trace = branch_and_bound(U, subsets, cutoff, start_time,best_size)
    elif method == "Approx":
        solution = greedy_set_cover(U, subsets)
    elif method == "LS1":
        solution, trace = local_search_1(U, subsets, cutoff, seed)
    elif method == "LS2":
        solution, trace = local_search_2(U, subsets, cutoff, seed)
    else:
        raise ValueError("Invalid method")

    elapsed = round(time.time() - start_time, 6)
    
    # Output filenames
    base = os.path.splitext(os.path.basename(filename))[0]
    sol_file = f"{basefolder}/{base}_{method}_{cutoff}" + (f"_{seed}.sol" if seed else ".sol")
    trace_file = f"{basefolder}/{base}_{method}_{cutoff}" + (f"_{seed}.trace" if seed else ".trace")

    # Write output
    write_solution(sol_file, solution)
    if method != "Approx":  # Only BnB and LS need trace
        write_trace(trace_file, trace)


   # === ✅ Print runtime and relative error ===
    # Try to read from corresponding .out file
    opt_path = f"data/{base}.out"

    with open(opt_path, 'r') as f:
        opt_val = int(f.readline().strip())
    alg_val = len(solution)
    rel_err = (alg_val - opt_val) / opt_val


    print(f"[{base} | {method}] Total Runtime: {elapsed:.4f} seconds, Collection Size: {alg_val}, OPT: {opt_val}, RelErr: {rel_err:.4f}")

if __name__ == "__main__":
    args = sys.argv
    inst, method, cutoff, seed = None, None, None, None
    for i in range(len(args)):
        if args[i] == '-inst':
            inst = args[i+1]
        elif args[i] == '-alg':
            method = args[i+1]
        elif args[i] == '-time':
            cutoff = int(args[i+1])
        elif args[i] == '-seed':
            seed = int(args[i+1])
        elif args[i] == '-outfile':
            basefolder = args[i+1]
    
    evaluate(inst, method, cutoff, seed,basefolder)
