#time: o(n), space= o(1)
# logic: tranverse from right to left and store the element with max_ele_seen_so_far
# comparing the element in max_seen_so_far
# max_seen_so_far will contain the maximum ele seen till now from right side
# and replace the iterating element with max_ele_seen_so_far as we are traversing from right to left

# time = O(n), space = O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        max_ele_seen_so_far= arr[n-1]
        arr[n-1]= -1
        for i in range(n-2,-1,-1):
            temp=arr[i]  # because this can be maximum till now
            arr[i]= max_ele_seen_so_far
            max_ele_seen_so_far = max(max_ele_seen_so_far, temp)
        return arr

# Java
"""
class Solution {

    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        int maxElementSeenSoFar = arr[n - 1];
        arr[n - 1] = -1; // Last element is always -1
        
        for (int i = n - 2; i >= 0; i--) {
            int temp = arr[i]; // Store current element before overwriting
            arr[i] = maxElementSeenSoFar;
            maxElementSeenSoFar = Math.max(maxElementSeenSoFar, temp);
        }
        
        return arr;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        int max_ele_seen_so_far = arr[n - 1];
        arr[n - 1] = -1;

        for (int i = n - 2; i >= 0; i--) {
            int temp = arr[i];  // because this can be maximum till now
            arr[i] = max_ele_seen_so_far;
            max_ele_seen_so_far = max(max_ele_seen_so_far, temp);
        }

        return arr;
    }
};
"""
