import os

def calculate_relative_errors(sol_folder, data_folder):
    for fname in os.listdir(sol_folder):
        if not fname.endswith(".sol"):
            continue

        # Extract base instance name (e.g., large1)
        instance = fname.split('_')[0]
        sol_path = os.path.join(sol_folder, fname)
        out_path = os.path.join(data_folder, f"{instance}.out")

        if not os.path.exists(out_path):
            print(f"❌ No corresponding .out file for {fname}")
            continue

        # Read algorithm solution size
        with open(sol_path, 'r') as f:
            alg_val = int(f.readline().strip())

        # Read optimal value from .out file
        with open(out_path, 'r') as f:
            opt_val = int(f.readline().strip())

        rel_err = (alg_val - opt_val) / opt_val
        print(f"{instance}: Alg={alg_val}, OPT={opt_val}, RelErr={rel_err:.4f}")
calculate_relative_errors("output_approx", "data")