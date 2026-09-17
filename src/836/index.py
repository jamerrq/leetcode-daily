class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        idxs = [0, 0, 2, 2]
        idys = [1, 3, 3, 1]
        #
        for i in range(4):
            cx = rec1[idxs[i]]
            cy = rec1[idys[i]]
            if rec2[0] < cx < rec2[2] and rec2[1] < cy < rec2[3]:
                return True
            #
            dx = rec2[idxs[i]]
            dy = rec2[idys[i]]
            if rec1[0] < dx < rec1[2] and rec1[1] < dy < rec1[3]:
                return True

        if rec1[0] < (rec2[2] + rec2[0]) / 2 < rec1[2] and \
            rec1[1] < (rec2[3] + rec2[1]) / 2 < rec1[3]:
            return True

        if rec2[0] < (rec1[2] + rec1[0]) / 2 < rec2[2] and \
            rec2[1] < (rec1[3] + rec1[1]) / 2 < rec2[3]:
            return True

        return False
