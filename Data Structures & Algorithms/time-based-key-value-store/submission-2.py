class TimeMap:
    """
    from my understanding, you can only do this problem in Olog(n) if the map values 
    are sorted. this must mean that when you set a new value to a key, the timestamp is always
    later than any previously set values
    this makes the value lists sorted and allows for binary search
    """
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        lst = self.time_map[key]
        l = 0
        h = len(lst) - 1
        max_time = (-10000000000000, "")
        while l <= h:
            mp = (l + h) // 2
            time = lst[mp][0]
            val = lst[mp][1]
            if time == timestamp:
                return val
            if time < timestamp:
                if time > max_time[0]:
                    max_time = (time, val)
                l = mp + 1
            else:
                h = mp - 1
        return max_time[1]
            
            
