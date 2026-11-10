class Solution:
    def findMedianSortedArrays(self, A: list[int], B: list[int]) -> float:
        if len(A) > len(B):
            A, B = B, A
        x, y = len(A), len(B)
        low, high = 0, x
        while low <= high:
            px = (low + high) // 2
            py = (x + y + 1) // 2 - px
            lx = float('-inf') if px == 0 else A[px - 1]
            rx = float('inf') if px == x else A[px]
            ly = float('-inf') if py == 0 else B[py - 1]
            ry = float('inf') if py == y else B[py]
            if lx <= ry and ly <= rx:
                return (max(lx, ly) + min(rx, ry)) / 2 if (x + y) % 2 == 0 else max(lx, ly)
            elif lx > ry:
                high = px - 1
            else:
                low = px + 1