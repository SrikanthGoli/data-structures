
# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s):

        """
        :type s: str
        :rtype: int
        """
        count = 0
        stp = s.strip()

        for i in range(len(stp) - 1, -1, -1):

            if stp[i] != " ":
                count += 1

            elif stp[i] == " ":
                break

        return count