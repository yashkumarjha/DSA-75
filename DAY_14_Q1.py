class TimeMap:

    def __init__(self):
        # Initialization
        self.map_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value and timestamp to the list with key
        self.map_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Initialize an empty string to store the result.
        res = ""
        # Retrieve the list of pairs associated with the given key.
        temp = self.map_dict.get(key, [])

        # Perform binary search within the list of pairs.
        low, high = 0, len(temp) - 1
        while low <= high:
            mid = (low + high) // 2

            # If the timestamp at mid is less than or equal to the target timestamp,
            # update the result and move the search to the right half.
            if temp[mid][1] <= timestamp:
                res = temp[mid][0]
                low = mid + 1
            # If the timestamp at mid is greater than the target timestamp,
            # move the search to the left half.
            else:
                high = mid - 1

        return res                
