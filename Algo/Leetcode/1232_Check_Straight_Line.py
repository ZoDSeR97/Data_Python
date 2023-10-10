# You are given an array coordinates, coordinates[i] = [x, y], 
# Where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

# Contraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        return True
        
        
if __name__ == "__main__":
    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    expected = False
    solution = Solution()
    print(solution.checkStraightLine(coordinates) == expected)