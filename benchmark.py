"""Empirical comparison of deterministic and randomized Quicksort."""
from __future__ import annotations

import csv
import random
import sys
import time
from pathlib import Path
from statistics import mean

from quicksort import deterministic_quicksort, randomized_quicksort

sys.setrecursionlimit(100_000)

SIZES = [100, 500, 1000, 2000, 4000]
TRIALS = 5
SEED = 531


def build_input(size: int, distribution: str, rng: random.Random) -> list[int]:
    if distribution == "random":
        return [rng.randint(0, size * 10) for _ in range(size)]
    if distribution == "sorted":
        return list(range(size))
    if distribution == "reverse_sorted":
        return list(range(size, 0, -1))
    raise ValueError(f"Unknown distribution: {distribution}")


def timed_run(data: list[int], randomized: bool, seed: int) -> float:
    working = data.copy()
    start = time.perf_counter()
    if randomized:
        randomized_quicksort(working, rng=random.Random(seed))
    else:
        deterministic_quicksort(working)
    elapsed = time.perf_counter() - start
    assert working == sorted(data)
    return elapsed


def main() -> None:
    output = Path("results/benchmark_results.csv")
    output.parent.mkdir(exist_ok=True)
    rows: list[dict[str, object]] = []
    data_rng = random.Random(SEED)

    for distribution in ("random", "sorted", "reverse_sorted"):
        for size in SIZES:
            data = build_input(size, distribution, data_rng)
            det_times = [timed_run(data, False, SEED + t) for t in range(TRIALS)]
            rand_times = [timed_run(data, True, SEED + t) for t in range(TRIALS)]
            rows.append({
                "distribution": distribution,
                "size": size,
                "deterministic_seconds": mean(det_times),
                "randomized_seconds": mean(rand_times),
            })
            print(f"{distribution:14s} n={size:5d} deterministic={mean(det_times):.6f}s randomized={mean(rand_times):.6f}s")

    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSaved results to {output}")


if __name__ == "__main__":
    main()
