from typing import List, Dict

class Solution:
    def digital_sum(self, number: int) -> int:
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        return sum
    
    def find_highest_freq(self, frequency_map: Dict) -> int:
        max_freq = 0
        result_digit = 0
        
        for digit, count in frequency_map.items():
            if count > max_freq or (count == max_freq and digit > result_digit):
                max_freq = count
                result_digit = digit
        return result_digit
    
    def digital_root_freq(self, numbers: List) -> int:
        freq = {}
        for num in numbers:
            while num > 9:
                num = self.digital_sum(num)
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return self.find_highest_freq(freq)