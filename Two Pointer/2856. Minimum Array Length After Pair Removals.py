# My mistake:

# It will give wrong ans in cases like : 
# [1,3,3,3,4] , this will give ans = 3 but ans should be equal to '1'.
# (1,3),(1, 4) then only one '3' will be remaining.

# Why ?
# Because here we only need 2 ele unequal ele to cancel each other.
# And we should focus on how we can cancel the most frequent ele to minimum length.

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        i , j = 0, n-1
        while i <= j:
            if nums[j] > nums[i]:
                i += 1
                j -= 1
            else:
                # all are equal so can't cancel now 
                break
        return j - i + 1
    

# Java
"""
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        int i = 0, j = n - 1;
        while (i <= j) {
            if (nums.get(j) > nums.get(i)) {
                i++;
                j--;
            } else {
                // all are equal so can't cancel now 
                break;
            }
        }
        return j - i + 1;
    }
}
"""

# C++
"""
class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        int n = nums.size();
        int i = 0, j = n - 1;
        while (i <= j) {
            if (nums[j] > nums[i]) {
                i++;
                j--;
            } else {
                // all are equal so can't cancel now 
                break;
            }
        }
        return j - i + 1;
    }
};
"""

# Method 1:
# Observation: all left elements must be same only otherwise they can cancel each other.

# Cancelling the two most frequent ele first to minimise the length.

# Here we need to cancel the two most frequent ele and then again we need to put their remaining frequency after cancellation
# and we will keep on cancelling like this.
# For this type of operation where we need min/max always then use heap.

# In this we only care about freq not indices or element value because we need a pair(distinct ele) to cancel.

# Note: this will work for increasing order array and normal array also.

# Time : O(n*logn)
# space = O(n)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        maxHeap = []
        for value in freq.values():
            heapq.heappush(maxHeap, -1*value)  # we only care about freq not values
        
        # if there is >= 2 element then there is chance of cancellation
        while len(maxHeap) >= 2:
            # pick two most frequent ele remaining. 
            max1 = -1 * heapq.heappop(maxHeap)
            max2 = -1 * heapq.heappop(maxHeap)
            max1 -= 1
            max2 -= 1
            if max1:
                heapq.heappush(maxHeap, -1*max1)
            if max2:
                heapq.heappush(maxHeap, -1*max2)
        return -1*maxHeap[0] if maxHeap else 0
    

# Method 2: 
# Using two pointer
# Optimising taking benefit of sorted array.

# Logic:  compare the last element with the element in the middle of the array. 
# If our condition is satisfied, then remove this pair.
#  otherwise, traverse left of the array from the middle to find a smaller element that satisfies our condition for removal.

# Time : O(n)
# SPace : O(1)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)  # Total number of elements in the array.
        mid = n // 2    

        i = n - 1     # Pointer to the end of the array.
        j = mid - 1   # Pointer to the middle of the array. '-1' to get the more smaller element.
        ans = n

        # Iterate from the end of the array towards the middle.
        while j >= 0:
            if nums[i] > nums[j]:
                ans -= 2  # If nums[i] > nums[j], we need to remove two elements.
                i -= 1  # we got smaller ele to cancel nums[i] so decrease 'i'.
            j -= 1   # to find even more smaller if condition doesn't satisfy or if satisfy then find other ele for nums[i]
            
        return ans


# Method 3:
# other way of writing the same logic if we compare start and middle.
# Logic: compare the 1st ele with middle ele and if they satify the condition cancel both.

# Time : O(n)

# Note:Analyse this method properly.

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        i = 0
        j = (n + 1) // 2   # to get more bigger element.
        while i < n //2 and j < n:
            if nums[i] < nums[j]:
                ans -= 2   # cancel that pair so ele remaining will be 'ans-2'.
                i += 1
            j += 1
        return ans


# method 4:

# Logic: 1) if the count of max occuring element is less than n/2 times, 
# then al the max_coccuring element can be cancelled by other elements.
# Also all remaining elements left after cancellation of max_occuring_element will be cancelled amongst themselves. 

# In this case, if array size is even, then we say that ans is 0 and 1 in case the array size is odd. 
# Because after cancelling all elements, 1 element is still remaining at the end.

# 2) If the element occurs more than n/2 times say 'maxi' no of times, 
# then, all max_occuring ele won't be cancelled. But will cancel all other elements than max_occuring ele.
# How many elements are remaining? 
# The elements remaining are (n - maxi). 
# So elements left after cancellation are maxi - (n - maxi) = 2*maxi - n;
# All these left elements will be 'max_occuring ele' only.

# time = space = O(n)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        max_count = max(freq.values())   # frequency of maximum ele in nums
        if max_count *2 < n:
            return n & 1  # '0' if 'n' is even else '1'.
        return 2 * max_count - n   # max_count - (n - max_count)


# Java
"""
// Method 1
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) freq.put(num, freq.getOrDefault(num, 0) + 1);

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int count : freq.values()) {
            maxHeap.add(count);  // we only care about freq not values
        }

        // if there is >= 2 element then there is chance of cancellation
        while (maxHeap.size() >= 2) {
            int max1 = maxHeap.poll();
            int max2 = maxHeap.poll();
            max1 -= 1;
            max2 -= 1;
            if (max1 > 0) maxHeap.add(max1);
            if (max2 > 0) maxHeap.add(max2);
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}

// Method 2
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        int mid = n / 2;
        int i = n - 1;       // Pointer to the end of the array.
        int j = mid - 1;     // Pointer to the middle of the array. '-1' to get more smaller element.
        int ans = n;

        // Iterate from the end of the array towards the middle.
        while (j >= 0) {
            if (nums.get(i) > nums.get(j)) {
                ans -= 2;   // remove both elements
                i--;
            }
            j--;
        }
        return ans;
    }
}

// Method 3
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        int ans = n;
        int i = 0;
        int j = (n + 1) / 2;  // to get more bigger element.
        while (i < n / 2 && j < n) {
            if (nums.get(i) < nums.get(j)) {
                ans -= 2;   // cancel that pair so ele remaining will be 'ans-2'.
                i++;
            }
            j++;
        }
        return ans;
    }
}

// Method 4
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) freq.put(num, freq.getOrDefault(num, 0) + 1);

        int maxCount = Collections.max(freq.values()); // frequency of maximum ele in nums
        if (maxCount * 2 < n) {
            return n % 2; // '0' if 'n' is even else '1'
        }
        return 2 * maxCount - n;
    }
}
"""


# C++
"""
// Method 1:
class Solution {
    public int minLengthAfterRemovals(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int value : freq.values()) {
            maxHeap.offer(value);  // we only care about freq not values
        }

        // if there is >= 2 element then there is chance of cancellation
        while (maxHeap.size() >= 2) {
            int max1 = maxHeap.poll();
            int max2 = maxHeap.poll();
            max1--;
            max2--;
            if (max1 > 0) maxHeap.offer(max1);
            if (max2 > 0) maxHeap.offer(max2);
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}


// Method 2:
class Solution {
    public int minLengthAfterRemovals(int[] nums) {
        int n = nums.length;
        int mid = n / 2;

        int i = n - 1;      // Pointer to the end of the array.
        int j = mid - 1;    // Pointer to the middle of the array.
        int ans = n;

        // Iterate from the end of the array towards the middle.
        while (j >= 0) {
            if (nums[i] > nums[j]) {
                ans -= 2;  // Remove two elements if nums[i] > nums[j]
                i--;       // got smaller ele to cancel nums[i]
            }
            j--;  // find smaller or next candidate
        }

        return ans;
    }
}


// Method 3:
class Solution {
    public int minLengthAfterRemovals(int[] nums) {
        int n = nums.length;
        int ans = n;
        int i = 0;
        int j = (n + 1) / 2;  // to get more bigger element

        while (i < n / 2 && j < n) {
            if (nums[i] < nums[j]) {
                ans -= 2;  // cancel that pair
                i++;
            }
            j++;
        }

        return ans;
    }
}


// Method 4:
class Solution {
    public int minLengthAfterRemovals(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> freq = new HashMap<>();
        int maxCount = 0;

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            maxCount = Math.max(maxCount, freq.get(num));  // frequency of max ele
        }

        if (maxCount * 2 < n) {
            return n % 2;  // return 0 if even, 1 if odd
        }

        return 2 * maxCount - n;  // maxCount - (n - maxCount)
    }
}
"""