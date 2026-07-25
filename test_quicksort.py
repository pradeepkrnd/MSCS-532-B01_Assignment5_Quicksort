"""Unit tests for both Quicksort implementations."""
import random
import unittest

from quicksort import deterministic_quicksort, randomized_quicksort


class QuicksortTests(unittest.TestCase):
    def check_both(self, values):
        expected = sorted(values)
        deterministic = values.copy()
        randomized = values.copy()
        deterministic_quicksort(deterministic)
        randomized_quicksort(randomized, rng=random.Random(42))
        self.assertEqual(deterministic, expected)
        self.assertEqual(randomized, expected)

    def test_empty(self):
        self.check_both([])

    def test_single_value(self):
        self.check_both([7])

    def test_duplicates(self):
        self.check_both([4, 2, 4, 1, 2, 4])

    def test_sorted(self):
        self.check_both(list(range(50)))

    def test_reverse_sorted(self):
        self.check_both(list(range(50, 0, -1)))

    def test_random_values(self):
        rng = random.Random(531)
        self.check_both([rng.randint(-1000, 1000) for _ in range(500)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
