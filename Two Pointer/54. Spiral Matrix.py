# method 1: 

# Logic: Just move in all the four directions sequentially that will give the ans.
# first move into top row -> then last row -> then last col ->  then 1st col (in remaining one).
# Time complexity = O(m * n)  
# Space Complexity: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col= len(matrix), len(matrix[0])
        up= 0                  # rowBegin
        down= row -1    # rowEnd
        left= 0                # colBegin
        right= col  -1  # colEnd
        res= []
        while len(res) < row * col:
            # Traverse right, proper row should be fixed
            for c in range(left, right +1):
                if len(res) >= row * col:
                    break
                res.append(matrix[up][c])
            # Traverse down, proper col should be fixed
            for r in range(up +1, down +1):
                if len(res) >= row * col:
                    break
                res.append(matrix[r][right])
            # Traverse left, proper row should be fixed
            for c in range(right-1, left-1, -1):
                if len(res) >= row * col:
                    break
                res.append(matrix[down][c])
            # Traverse up, proper col should be fixed
            for r in range(down-1, up, -1):
                if len(res) >= row * col:
                    break
                res.append(matrix[r][left])
            up, down, left, right= up + 1, down -1, left + 1, right -1
        return res



# Java
""""

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return res;

        int row = matrix.length;
        int col = matrix[0].length;
        int up = 0, down = row - 1;
        int left = 0, right = col - 1;

        while (res.size() < row * col) {
            // Traverse right, proper row should be fixed
            for (int c = left; c <= right && res.size() < row * col; c++) {
                res.add(matrix[up][c]);
            }
            // Traverse down, proper col should be fixed

            for (int r = up + 1; r <= down && res.size() < row * col; r++) {
                res.add(matrix[r][right]);
            }
            // Traverse left, proper row should be fixed
            for (int c = right - 1; c >= left && res.size() < row * col; c--) {
                res.add(matrix[down][c]);
            }
            // Traverse up, proper col should be fixed
            for (int r = down - 1; r > up && res.size() < row * col; r--) {
                res.add(matrix[r][left]);
            }
            up++;
            down--;
            left++;
            right--;
        }

        return res;
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        int up = 0;          // rowBegin
        int down = row - 1;  // rowEnd
        int left = 0;        // colBegin
        int right = col - 1; // colEnd
        vector<int> res;

        while (res.size() < row * col) {
            // Traverse right, proper row should be fixed
            for (int c = left; c <= right; c++) {
                if (res.size() >= row * col) break;
                res.push_back(matrix[up][c]);
            }
            // Traverse down, proper col should be fixed
            for (int r = up + 1; r <= down; r++) {
                if (res.size() >= row * col) break;
                res.push_back(matrix[r][right]);
            }
            // Traverse left, proper row should be fixed
            for (int c = right - 1; c >= left; c--) {
                if (res.size() >= row * col) break;
                res.push_back(matrix[down][c]);
            }
            // Traverse up, proper col should be fixed
            for (int r = down - 1; r > up; r--) {
                if (res.size() >= row * col) break;
                res.push_back(matrix[r][left]);
            }
            up++, down--, left++, right--;
        }
        return res;
    }
};
"""