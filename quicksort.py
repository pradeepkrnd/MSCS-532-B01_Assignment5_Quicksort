"""Deterministic and randomized Quicksort implementations.

The deterministic version uses the last element as the pivot. The randomized
version swaps a randomly selected pivot into the last position before applying
Lomuto partitioning.
"""
from __future__ import annotations

import random
from typing import MutableSequence, TypeVar

T = TypeVar("T")


def partition(values: MutableSequence[T], low: int, high: int) -> int:
    """Partition values[low:high+1] using the last element as pivot."""
    pivot = values[high]
    i = low - 1
    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    values[i + 1], values[high] = values[high], values[i + 1]
    return i + 1


def deterministic_quicksort(values: MutableSequence[T], low: int = 0, high: int | None = None) -> None:
    """Sort *values* in place using deterministic Quicksort."""
    if high is None:
        high = len(values) - 1
    if low < high:
        pivot_index = partition(values, low, high)
        deterministic_quicksort(values, low, pivot_index - 1)
        deterministic_quicksort(values, pivot_index + 1, high)


def randomized_partition(values: MutableSequence[T], low: int, high: int, rng: random.Random) -> int:
    """Choose a random pivot and partition values[low:high+1]."""
    pivot_index = rng.randint(low, high)
    values[pivot_index], values[high] = values[high], values[pivot_index]
    return partition(values, low, high)


def randomized_quicksort(
    values: MutableSequence[T],
    low: int = 0,
    high: int | None = None,
    rng: random.Random | None = None,
) -> None:
    """Sort *values* in place using randomized Quicksort."""
    if high is None:
        high = len(values) - 1
    if rng is None:
        rng = random.Random()
    if low < high:
        pivot_index = randomized_partition(values, low, high, rng)
        randomized_quicksort(values, low, pivot_index - 1, rng)
        randomized_quicksort(values, pivot_index + 1, high, rng)


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    deterministic = sample.copy()
    randomized = sample.copy()
    deterministic_quicksort(deterministic)
    randomized_quicksort(randomized, rng=random.Random(42))
    print("Original:     ", sample)
    print("Deterministic:", deterministic)
    print("Randomized:   ", randomized)
