class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.arr) - 1

        while l <= r:
            m = (l + r) // 2

            if self.arr[m] < num:
                l = m + 1
            else:
                r = m - 1

        self.arr.insert(l, num)
        

    def findMedian(self) -> float:
        size = len(self.arr)
        idx = size // 2

        if size % 2 == 0:
            return (self.arr[idx] + self.arr[idx-1]) / 2
        else:
            return self.arr[idx]


        
        