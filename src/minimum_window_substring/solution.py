from collections import Counter, defaultdict
from typing import Tuple

class Solution:
    def get_minimum_window(original: str, check: str) -> str:
        original_len, check_len = len(original), len(check)
        if original_len < check_len:
            return ""

        def is_smaller_window(window_candidate: Tuple[int, int], best_window: Tuple[int, int]) -> bool:
            # compare by length, break ties lexicographically
            len_c = window_candidate[1] - window_candidate[0]
            len_b = best_window[1] - best_window[0]
            if len_c == len_b:
                for i in range(len_c):
                    a = original[window_candidate[0] + i]
                    b = original[best_window[0] + i]
                    if a != b:
                        return a < b
                return False
            return len_c < len_b

        required_counts = Counter(check)
        required_unique = len(required_counts)
        window_counts: defaultdict[str, int] = defaultdict(int)

        # best_window is (start, end_exclusive); initialize to an "infinite" window
        best_window: Tuple[int, int] = (-original_len - 1, 0)
        satisfied_unique = 0
        left = 0

        for right in range(original_len):
            char = original[right]
            if char in required_counts:
                window_counts[char] += 1
                if window_counts[char] == required_counts[char]:
                    satisfied_unique += 1

            while satisfied_unique == required_unique:
                window_candidate = (left, right + 1)
                if is_smaller_window(window_candidate, best_window):
                    best_window = window_candidate

                left_char = original[left]
                if left_char in required_counts:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < required_counts[left_char]:
                        satisfied_unique -= 1
                left += 1

        return original[best_window[0] : best_window[1]]