# Set Cover Solver - Approximation, Local Search, and BnB Methods

This project implements and evaluates four different algorithms to solve instances of the Set Cover Problem:

- **LS1**: A greedy local search variant
- **LS2**: A more exploratory local search method
- **BnB**: Branch-and-Bound for optimality
- **Approximation**: A greedy approximation heuristic

## 🔧 Structure Overview

.
├── approx.py             # Approximation algorithm
├── bnb.py                # Branch-and-Bound algorithm
├── ls1.py                # Local Search 1
├── ls2.py                # Local Search 2
├── main.py               # Unified runner for all algorithms
├── run_all_tests.sh      # Script to run all algorithms on all datasets
├── run_10_tests.sh       # Script to run LS2 over 20 seeds
├── rel_error.py          # Relative error calculation
├── data_analysis.ipynb   # Jupyter notebook for visualizing results and generate the required graphs
├── data/                 # Dataset .in files and .out (optimal) files
├── outputs/              # Trace and solution files


---
## ⚙️ Requirements

- Python 3.10+
- Required packages:
  - `matplotlib`
  - `pandas`
  - `math`, `os`, `random`, `regex`, `time` (standard)

Install required packages with:

```bash
pip install matplotlib pandas
---
## How to Run

### Run a single instance

python main.py -inst data/large1.in -alg LS1 -time 300 -seed 1
python main.py -inst data/large1.in -alg LS2 -time 300 -seed 1
python main.py -inst data/large1.in -alg BnB -time 1800
python main.py -inst data/large1.in -alg APPROX

### Run LS2/LS1 with seeds 1 to 20

./run_10_tests.sh

### **Run a selected algorithms on all datasets**

./run_all_tests.sh

### Analyzing Results

jupyter notebook data_analysis.ipynb

### Output Files

Each run generates:

* `*.trace`: Quality improvements over time
* `*.sol`: Final solution (list of subset indices)
* `*.out`: Reference optimal solutions (used for evaluation)
