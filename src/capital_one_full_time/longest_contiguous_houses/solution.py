from typing import List, Dict

class solution:
    def check_adjacent_house(self, house_location: int, location_dict: Dict[int, bool], visited: set[int]) -> int:
        if house_location not in location_dict or house_location in visited:
            return 0
        
        visited.add(house_location)
        
        left_count = self.check_adjacent_house(house_location - 1, location_dict, visited)
        right_count = self.check_adjacent_house(house_location + 1, location_dict, visited)

        return 1 + left_count + right_count

    def longest_contiguous_house(self, query: List[int]) -> List:
        location_dict: Dict[int, bool] = {}
        result: List[int] = []
        current_max_contiguous_len = 0

        for num in query:
            location_dict[num] = True

            visited: set[int] = set()
            contiguous_length = self.check_adjacent_house(num, location_dict, visited)

            current_max_contiguous_len = max(current_max_contiguous_len, contiguous_length)
            result.append(current_max_contiguous_len)

        return result
