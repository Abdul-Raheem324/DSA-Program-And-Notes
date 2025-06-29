# Note: just focus on minimum and maximum element.
# ans = bring the last maximum ele at 'n-1'th index + bring the 1st minimum ele at '0'th index

# VVI: But while bringing the 1st minimum ele(say at index 'i') at '0'th index last maximum ele may also get swapped
# so to bring the last maximum ele(say at inex 'j') at 'n-1'th index , we will need '1' less swap 
# when i > j

# Therefore in this case, we will subtract '1' from ans.
# time : O(n), space : O(1)

class Solution:
    def minimumSwaps(self, nums):
        n  = len(nums)
        minEle , maxEle = min(nums) , max(nums)
        first_index_min , last_index_max = n-1, 0
        for i, num in enumerate(nums):
            if num == minEle:
                first_index_min = min(first_index_min, i)
            if num == maxEle:
                last_index_max = max(last_index_max, i)
        swaps = 0
        swaps += (n - 1) - last_index_max  # to bring the last maximum ele at 'n-1'th index
        swaps += first_index_min             # to bring the 1st minimum ele at '0'th index
        # Now check if last maximum ele get swapped automatically while bringing the 1st minimum ele at '0'th index
        if last_index_max < first_index_min:  
            swaps -= 1
        return swaps

s= Solution()
arr = [3,4,5,5,3,1]
arr = [9]
arr = [1,3,5,2,8]
arr = [10, 8, 6, 2, 2, 12, 9, 12]
print("minimum no of swaps needed is : ", s.minimumSwaps(arr))

# Java
"""
class Solution {
    public int minimumSwaps(int[] nums) {
        int n = nums.length;
        int minEle = Integer.MAX_VALUE, maxEle = Integer.MIN_VALUE;
        int firstIndexMin = n - 1, lastIndexMax = 0;

        // Find the minimum and maximum elements
        for (int num : nums) {
            minEle = Math.min(minEle, num);
            maxEle = Math.max(maxEle, num);
        }

        // Find the first occurrence of minEle and last occurrence of maxEle
        for (int i = 0; i < n; i++) {
            if (nums[i] == minEle) {
                firstIndexMin = Math.min(firstIndexMin, i);
            }
            if (nums[i] == maxEle) {
                lastIndexMax = Math.max(lastIndexMax, i);
            }
        }

        // Calculate swaps
        int swaps = (n - 1 - lastIndexMax) + firstIndexMin;

        // Adjust swap count if the last max element gets swapped automatically
        if (lastIndexMax < firstIndexMin) {
            swaps -= 1;
        }

        return swaps;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {3, 4, 5, 1, 2, 6}; // Example input
        System.out.println(sol.minimumSwaps(nums)); // Output the result
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumSwaps(vector<int>& nums) {
        int n = nums.size();
        int minEle = *min_element(nums.begin(), nums.end());
        int maxEle = *max_element(nums.begin(), nums.end());
        int first_index_min = n - 1, last_index_max = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == minEle) {
                first_index_min = min(first_index_min, i);
            }
            if (nums[i] == maxEle) {
                last_index_max = max(last_index_max, i);
            }
        }

        int swaps = 0;
        swaps += (n - 1) - last_index_max;  // to bring the last maximum element to the 'n-1'th index
        swaps += first_index_min;           // to bring the first minimum element to the '0'th index

        // Check if last maximum element gets swapped automatically while bringing the first minimum element to '0'th index
        if (last_index_max < first_index_min) {
            swaps -= 1;
        }

        return swaps;
    }
};

int main() {
    Solution s;
    vector<int> arr = {3, 4, 5, 5, 3, 1};
    arr = {9};
    arr = {1, 3, 5, 2, 8};
    arr = {10, 8, 6, 2, 2, 12, 9, 12};
    cout << "Minimum number of swaps needed is: " << s.minimumSwaps(arr) << endl;
    return 0;
}
"""
