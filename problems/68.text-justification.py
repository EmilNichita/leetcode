#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        rows = [[words[0]]]
        row_lengths = [len(words[0])]

        for word in words[1:]:
            # can we put this word in the previous row?
            if row_lengths[-1] + len(rows[-1]) + len(word) <= maxWidth:
                rows[-1].append(word)
                row_lengths[-1] += len(word)
            else:
                rows.append([word])
                row_lengths.append(len(word))
        
        processed_rows = []

        for i, (row, row_length) in enumerate(zip(rows, row_lengths)):
            processed_rows.append(self.process_row(row, row_length, maxWidth, is_last_row=(i==len(rows)-1)))
        
        return processed_rows

        
    def process_row(self, row, row_length, maxWidth, is_last_row: bool):
        if not is_last_row:
            needed_spaces = maxWidth - row_length
            n_words = len(row)

            if n_words == 1:
                return f"{row[0]}{' '*needed_spaces}"
            

            min_space = needed_spaces // (n_words - 1)
            remainder = needed_spaces % (n_words - 1)

            spaces = []

            for _ in range(remainder):
                spaces.append(" "*(min_space+1))
            for _ in range(n_words-1-remainder):
                spaces.append(" "*min_space)
            
            result = []
            for word, space in zip(row, spaces):
                result.append(word)
                result.append(space)
            result.append(row[-1])

            return "".join(result)
        else:
            joined_string = " ".join(row)
            return f"{joined_string}{' '*(maxWidth - len(joined_string))}"

# @lc code=end

