'''
Solution:
1.  Brute force can be BFS: where goal state would be Y and start state would be X with 2 possible operations at each level.
2.  But, if we start from Y to X thinking about the question in reverse direction with reverse operations, whenever
    Y is divisible by 2 => reduce it by 2 to lessen the steps and whenever X >= Y reaches => stop and add (X - Y) to
    number of steps covered so far as there will be only one possible path if X >= Y.
3.  So, we can also reduce space if thought in the reverse path.

Time Complexity:    O(logY)
Space Complexity:   O(1)

--- Passed all testcases successfully on leetcode.
'''


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """

        #   initialization
        steps = 0

        #   iterate until Y > X
        while (Y > X):

            #   if even => reduce it by half
            if (Y % 2 == 0):
                Y /= 2
            else:
                Y += 1

            #   increment the steps
            steps += 1

        #   return the steps needed to reach X from Y
        return steps + (X - Y)