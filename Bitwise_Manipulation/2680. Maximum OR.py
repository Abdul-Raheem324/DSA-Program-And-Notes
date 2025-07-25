# Method 1: 

# we will get max ans by changing the same number by "num*(2^k)".
# Reason: To maximize the result, we should pick the numbers having their Left Most Set Bit (LMSB) farthest among all elements.

# logic: just change each number by "num*(2^k)" and check for max ans.

# Approach
# 1. Evaluate 2^k
# 2. Then calculate prefix & suffix bit wise value and store it. This will help to find OR of all ele after changing the value of an ele.
# 3. check each number by multiplying 2^k, if it has max ans or not.


# Q. Why this works :
# Ans : When we multiply a number by 2 then this equal to shifting the values to the left by 1 places.
# So to have a largest value we should shift a single number to the k number of times which end up with max value possible.
# now we don't know exactly which value to shift k times, so we check the same for all possible numbers and keep tracking the max value.
# https://leetcode.com/problems/maximum-or/solutions/3521223/c-intuition-with-explanation-proof-of-why-time-o-n/



class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n= len(nums)
        prefix= [0]*n  # prefix[i]= OR till index 'i'. OR of first 'i+1' ele.
        suffix= [0]*n  # Suffix[i]= OR of last 'i+1' ele from last.
        prefix[0], suffix[n-1]= nums[0], nums[-1]
        mul= 2**k
        for i in range(1, n):
            prefix[i]= prefix[i-1] | nums[i]
            suffix[n-i-1]= suffix[n- i] | nums[n- i- 1]
        mul= 2**k
        ans= 0
        for i in range(n):
            temp= nums[i]*mul
            if i- 1 >= 0:
                temp= temp | prefix[i-1]
            if i+1 <= n-1:
                temp= temp | suffix[i+1]
            ans= max(ans, temp)
        return ans

# Java Code 
"""
class Solution {
    public long maximumOr(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n]; // OR of first 'i+1' elements
        long[] suffix = new long[n]; // OR of last 'i+1' elements from the end
        prefix[0] = nums[0];
        suffix[n - 1] = nums[n - 1];
        long mul = 1L << k; // Equivalent to 2^k
        
        // Compute prefix and suffix OR values
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] | nums[i];
            suffix[n - i - 1] = suffix[n - i] | nums[n - i - 1];
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long temp = nums[i] * mul;
            if (i - 1 >= 0) temp |= prefix[i - 1];
            if (i + 1 <= n - 1) temp |= suffix[i + 1];
            ans = Math.max(ans, temp);
        }

        return ans;
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
    long long maximumOr(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n, 0); // OR of first 'i+1' elements
        vector<long long> suffix(n, 0); // OR of last 'i+1' elements from the end
        prefix[0] = nums[0];
        suffix[n - 1] = nums[n - 1];
        long long mul = 1LL << k; // Equivalent to 2^k
        
        // Compute prefix and suffix OR values
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] | nums[i];
            suffix[n - i - 1] = suffix[n - i] | nums[n - i - 1];
        }

        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long temp = nums[i] * mul;
            if (i - 1 >= 0) temp |= prefix[i - 1];
            if (i + 1 <= n - 1) temp |= suffix[i + 1];
            ans = max(ans, temp);
        }

        return ans;
    }
};
"""