# Assignment 5: Quicksort Algorithm
 
This repository contains deterministic and randomized Quicksort implementations, unit tests, and an empirical benchmark for random, sorted, and reverse-sorted inputs.
 
## Files
 
- `quicksort.py` - deterministic and randomized implementations.
- `test_quicksort.py` - correctness tests.
- `benchmark.py` - timing experiment.
- `results/benchmark_results.csv` - benchmark output.
 
## Requirements

Python 3.10 or newer. No third-party packages are needed.
 
## Run
 
```bash
python --version
python quicksort.py
python -m unittest -v
python benchmark.py
```
 
## Summary of findings
 
The deterministic implementation uses the final element as pivot. It performs well on many random inputs but produces highly unbalanced partitions for already sorted and reverse-sorted data, causing quadratic behavior. Random pivot selection makes the partition pattern independent of the original order and substantially reduces the chance of repeatedly selecting an extreme element.
 
