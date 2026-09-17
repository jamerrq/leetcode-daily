class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check every corner
        # corner 1
        c1_x, c1_y = rec1[0], rec1[1]
        c2_x, c2_y = rec1[0], rec1[3]
        c3_x, c3_y = rec1[2], rec1[3]
        c4_x, c4_y = rec1[2], rec1[1]
        # add middle point
        c5_x, c5_y = (rec1[0] + rec1[2]) / 2, (rec1[1] + rec1[3]) / 2
        #
        d1_x, d1_y = rec2[0], rec2[1]
        d2_x, d2_y = rec2[0], rec2[3]
        d3_x, d3_y = rec2[2], rec2[3]
        d4_x, d4_y = rec2[2], rec2[1]
        # add middle point
        d5_x, d5_y = (rec2[0] + rec2[2]) / 2, (rec2[1] + rec2[3]) / 2
        #
        cxs = [c1_x, c2_x, c3_x, c4_x, c5_x]
        cys = [c1_y, c2_y, c3_y, c4_y, c5_y]
        dxs = [d1_x, d2_x, d3_x, d4_x, d5_x]
        dys = [d1_y, d2_y, d3_y, d4_y, d5_y]
        #
        for i in range(5):
            cx = cxs[i]
            cy = cys[i]
            if d1_x < cx < d3_x and d1_y < cy < d3_y:
                return True
            #
            dx = dxs[i]
            dy = dys[i]
            if c1_x < dx < c3_x and c1_y < dy < c3_y:
                return True

        return False
