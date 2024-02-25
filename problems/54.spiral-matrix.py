#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        next_horisontal_is_right = True
        next_vertical_is_down = True

        m, n = len(matrix), len(matrix[0])

        curr_horisontal_size = n
        curr_vertical_size = m-1
        curr_direction_horisontal = True

        result = []
        curr_pos = [0, -1]

        total_cells = m*n

        while(len(result)!= total_cells):
            if curr_direction_horisontal:
                
                if next_horisontal_is_right:
                    for _ in range(curr_horisontal_size):
                        curr_pos[1] += 1
                        result.append(matrix[curr_pos[0]][curr_pos[1]])
 
                else:
                    for _ in range(curr_horisontal_size):
                        curr_pos[1] -= 1
                        result.append(matrix[curr_pos[0]][curr_pos[1]])
                
                next_horisontal_is_right = not next_horisontal_is_right
                curr_direction_horisontal = not curr_direction_horisontal
                curr_horisontal_size -= 1

            else:
                if next_vertical_is_down:
                    for _ in range(curr_vertical_size):
                        curr_pos[0] += 1
                        result.append(matrix[curr_pos[0]][curr_pos[1]])
 
                else:
                    for _ in range(curr_vertical_size):
                        curr_pos[0] -= 1
                        result.append(matrix[curr_pos[0]][curr_pos[1]])
                
                next_vertical_is_down = not next_vertical_is_down
                curr_direction_horisontal = not curr_direction_horisontal
                curr_vertical_size -= 1
        
        return result
# @lc code=end

