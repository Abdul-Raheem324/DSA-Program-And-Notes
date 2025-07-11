# method 1:
# logic: just make the recursion tree by including the first letetr 
# and 'not including' the 1st letter .
# and whenever you will find the given string empty then that will be our one of the subset.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        
        def dfs(i, subset):   # just backtracking
            if i== len(nums):
                res.append(subset)
                return
            # when you include the curr index ele.
            dfs(i+1, subset + [nums[i]])
            # when you don't include the curr index ele.
            dfs(i+1, subset)

        dfs(0, [])  
        return res

# Method 2 : Using Bit Masking

# n : len(nums)
# every subset is represented by a binary number of 'n' bits.
# VVI: Each bit represents whether the number at that index exists in the subset or not.
# No of subsets = 2^n . Using these 2^n numbers [0,2^n-1], we will try to find the number in that subset.

# For better understanding, go through link in sheet.

# if asked for only non-empty subsets then before adding temp into ans check:
# if len(temp) > 0 then only add.

# Time: O(2^n * n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for num in range(1 << n):
            temp = []
            # add the number whose 'index' bit is set in num
            for i in range(n):
                # if 'i'th bit is set in 'num then nums[i] is part of this subset.
                if (num >> i) & 1:
                    temp.append(nums[i])
            ans.append(temp)
        return ans

# method 3:
# iterative way:

# logic: Accept and reject is happening with 'ans so far'
# for each new number, 
# we can either pick it or not pick it. 
# 1, if pick, just add current number to every existing subset.
# 2, if not pick, just leave all existing subsets as they are.
# We just combine both into our result.

# For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
# Considering 1, if not use it, still [], if use 1, add it to [ ], so we have [1] now
# Combine them, now we have [ [ ], [1] ] as all possible subset

# Next considering 2, if not use it, we still have [ [ ], [1] ], 
# if use 2, just add 2 to each previous subset, we have [2], [1,2]
# Combine them, now we have [ [ ], [1], [2], [1,2] ]

# Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], 
# if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
# Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

# time: O(n*2^n), where 2^n is the total no of subsets and 
# we are copying the number to n subsets each time we encounter a num of the array

# space- O(n*2^n), where 2^n is the total no of subsets and 
# n is the space taken by each subset

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer= [[]]   # our final ans will contain list of list
        for num in nums:   # for each number in the array
            n= len(outer) 
            for i in range(n):
                internal= outer[i].copy()  # copy the internal list of outer list one by one
                internal.append(num)       # and append the number to all the existing list
                outer.append(internal)    # and at alst append the internal created list to the outer list
        return outer

# concise way of writing method 3 in python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer= [[]]   # our final ans will contain list of list
        for num in nums:
            outer+= [items+ [num] for items in outer]
        return outer


# Java Code 
"""
// method 1:
import java.util.*;

class Solution {
    List<List<Integer>> res = new ArrayList<>();

    private void dfs(int i, int[] nums, List<Integer> subset) {  
        // Just backtracking
        if (i == nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }
        // When you include the current index element.
        subset.add(nums[i]);
        dfs(i + 1, nums, subset);
        subset.remove(subset.size() - 1);

        // When you don't include the current index element.
        dfs(i + 1, nums, subset);
    }

    public List<List<Integer>> subsets(int[] nums) {
        res.clear();
        dfs(0, nums, new ArrayList<>());
        return res;
    }
}

// method 2:
import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();

        // Every subset is represented by a binary number of 'n' bits.
        // Each bit represents whether the number at that index exists in the subset or not.
        // No of subsets = 2^n. Using these 2^n numbers [0, 2^n-1], we will try to find the number in that subset.
        for (int num = 0; num < (1 << n); num++) {  
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                // If 'i'th bit is set in 'num' then nums[i] is part of this subset.
                if ((num >> i) & 1) {
                    temp.add(nums[i]);
                }
            }
            ans.add(temp);
        }
        return ans;
    }
}

// method 3:
import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> outer = new ArrayList<>();
        outer.add(new ArrayList<>()); // Initial empty subset

        // Accept and reject is happening with 'ans so far'
        for (int num : nums) {  
            int n = outer.size();  
            for (int i = 0; i < n; i++) {  
                List<Integer> internal = new ArrayList<>(outer.get(i));  // Copy the internal list of outer list one by one
                internal.add(num);       // Append the number to all the existing lists
                outer.add(internal);    // Append the internal created list to the outer list
            }
        }
        return outer;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> res;

    void dfs(int i, vector<int>& nums, vector<int> subset) {  
        // Just backtracking
        if (i == nums.size()) {
            res.push_back(subset);
            return;
        }
        // When you include the current index element.
        subset.push_back(nums[i]);
        dfs(i + 1, nums, subset);
        subset.pop_back();

        // When you don't include the current index element.
        dfs(i + 1, nums, subset);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        res.clear();
        vector<int> subset;
        dfs(0, nums, subset);
        return res;
    }
};

//Method 2
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;

        // Every subset is represented by a binary number of 'n' bits.
        // Each bit represents whether the number at that index exists in the subset or not.
        // No of subsets = 2^n. Using these 2^n numbers [0, 2^n-1], we will try to find the number in that subset.
        for (int num = 0; num < (1 << n); num++) {  
            vector<int> temp;
            for (int i = 0; i < n; i++) {
                // If 'i'th bit is set in 'num' then nums[i] is part of this subset.
                if ((num >> i) & 1) {
                    temp.push_back(nums[i]);
                }
            }
            ans.push_back(temp);
        }
        return ans;
    }
};

//Method 3
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> outer = {{}};
        
        // Accept and reject is happening with 'ans so far'
        for (int num : nums) {  
            int n = outer.size();  
            for (int i = 0; i < n; i++) {  
                vector<int> internal = outer[i];  // Copy the internal list of outer list one by one
                internal.push_back(num);       // Append the number to all the existing lists
                outer.push_back(internal);    // Append the internal created list to the outer list
            }
        }
        return outer;
    }
};

"""