class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        ----    ----   ----  
            ------ ------ --
                       --

        there is overlap if end_i > start_i+1:

        sort by end 

        1,2.   1,4  1,4.  

        '''

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        overlap_count = 0

        for start, end in intervals[1:]:
            if prev_end == -1:
                continue

            if prev_end > start:
                overlap_count += 1
            else:
                prev_end = end 

        return overlap_count 





        