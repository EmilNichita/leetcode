#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def get_neighbour_sum(i, j):
            candidate_positions = [
                [i-1, j-1],
                [i-1, j],
                [i-1, j+1],
                [i, j-1],
                [i, j+1],
                [i+1, j-1],
                [i+1, j],
                [i+1, j+1],
            ]
            valid_positions = [pos for pos in candidate_positions if (pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n)]

            return sum([board[pos[0]][pos[1]] % 2 for pos in valid_positions])
        
        for i in range(m):
            for j in range(n):
                s = get_neighbour_sum(i, j)
                
                if board[i][j] % 2 == 1:

                    if s < 2:
                        board[i][j] += 2
                    elif s > 3:
                        board[i][j] += 2
                else:
                    if s == 3:
                        board[i][j] += 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] % 2 == 1:
                    if board[i][j] == 3:
                        board[i][j] = 0
                else:
                    if board[i][j] == 2:
                        board[i][j] = 1
# @lc code=end

