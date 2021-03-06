# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are(i, 0) and (i, height[i]).Find two
# lines that together with the x-axis for m a container, such that the container
# contains the most water.Return the maximum a mount of water a container canstore.
# Notice that you may not slant the container.
#
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
#
# Explanation: The above vertical lines are represent ed by array[1, 8, 6, 2, 5, 4, 8,
# 3, 7]. In this case, the max area of water(blue section) the container can contain
# is 49.
#
# Example 2:
# Input: height = [1, 1]
# Output: 1
#
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Programming-Assignment.git

# function for finding the meximum area
def maximumArea(A, Len):
    area = 0
    for i in range(Len):
        for j in range(i + 1, Len):
            area = max(area, min(A[j], A[i]) * (j - i))
    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maximumArea(height, len(height)))

height = [1, 1]
print(maximumArea(height, len(height)))
