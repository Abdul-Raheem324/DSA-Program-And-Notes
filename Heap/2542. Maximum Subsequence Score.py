# Method 1: 

# Intuition: 1) we have to take sum from num1 and minimum from nums2.
# so order will not matter.
# 2) for maximum we have to maximise ele in both the array i.e maximize both the sum and the multiplier(min ele from nums2).

# logic: Taking each ele in nums2(say at index j) as minimum, find the max score we can get.
# after that take 'k' ele from nums1 such that those ele include index 'j' and nums2[j] is minimum

# for this sorting can make our work easy.
# But we have to keep track of mapping of ele in both arrays. => zip(nums1, nums)

# Then sort the above zipped array into descending order and keep adding element one by one in minHeap.
# Why descending order based on 'nums2?
# Because if we sort based on nums1 then we can't make sure that cur element of heap is minimum among all.
# we want maximum(minimum) and sum should also be maximum.  => Descending

# Why minHeap?
# So to remove ele when len(sub) > k , & removed one must be minimum for maximum sum. => maximising sum
# And current ele of nums2 must be minimum among all selected till now.
# for this we will use minHeap. => want length atmost k and also want to remove minimum.

# say n1 -> nums1 , n2 -> nums2
# for (n1, n2):
# n2 will always minimum since we are traversing in descending order. 
# But at the same time it will be also maximum(among minimum) for which we have selected k ele till now. ==>? maximising minimum

# Also we can use all ele we have seen till now in nums1 for current 'n2' as 
# this will be minimum till now so it will be minimum for all ele seen also.

# Note: Because of above condition sorting in ascending order won't work.
# Since 'n2' won't be minimum till now so we can't use all the ele that we have seen till now in nums1.

# From above idea, we also get intitution to use min heap.

# Note: Zip + sorting +  heap + slding window(poping)

# Note: Array length must be equal otherwise this logic won't work.

"""
Note: while poping when len(minHeap) > k then , current n1 can be also poped.
e.g: Take both array in descending order
then why we are blindly multiplying by 'n2' since it's pair can get poped also??
Because in such case answer won't come multiplying by current 'n2'.



Note: Why won't sort both array in descending order.
And traverse nums2 and for each ele of nums2 take 'k' max_ele from nums1.

This won't work because this will not guarantee that ele of nums2 is one of the chosen indices of nums1.

But ziping it together will guarantee this.
"""

# Time complexity: O( N * Log(N) + (N-k) * Log(k) )
# Space complexity: O(N) + O(k) = O(N+K)


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # for mapping the ele from num1 to nums2
        pairs= [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        # sort the above array 'pair' according to values of nums2 in descending order
        pairs = sorted(pairs, key= lambda p: p[1], reverse= True)
        
        # now consider each ele in nums2 as minimum and find the maximum score we can get.
        ans= 0
        n1sum = 0  # will store the sum of ele from nums1 that we have included till now.
        minHeap = []
        
        for n1, n2 in pairs:
            n1sum += n1
            heapq.heappush(minHeap, n1)  # we have to remove the min from num1 if len(heap)=>subsequence become greater than 'k'
                                        # removing min because we have to maximise ans.
            if len(minHeap) > k:
                # then it is better to not include top of heap for cur num 'n2'.
                n1pop = heapq.heappop(minHeap)
                n1sum -= n1pop
            if len(minHeap) == k:
                # 'n2' is minimum till now from 'nums2' and maximum sum we can get when 'n2' will be minimum = n1sum * n2.
                ans= max(ans, n1sum * n2)
        return ans

# Java Code
"""
import java.util.*;

public class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        // for mapping the ele from num1 to nums2
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums1[i];
            pairs[i][1] = nums2[i];
        }

        // sort the above array 'pair' according to values of nums2 in descending order
        Arrays.sort(pairs, (a, b) -> Integer.compare(b[1], a[1]));

        // now consider each ele in nums2 as minimum and find the maximum score we can get.
        long ans = 0;
        long n1sum = 0;  // will store the sum of ele from nums1 that we have included till now.
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int[] pair : pairs) {
            int n1 = pair[0], n2 = pair[1];
            n1sum += n1;
            minHeap.add(n1);  // we have to remove the min from num1 if len(heap)=>subsequence become greater than 'k'
                              // removing min because we have to maximise ans.
            if (minHeap.size() > k) {
                // then it is better to not include top of heap for cur num 'n2'.
                n1sum -= minHeap.poll();
            }
            if (minHeap.size() == k) {
                // 'n2' is minimum till now from 'nums2' and maximum sum we can get when 'n2' will be minimum = n1sum * n2.
                ans = Math.max(ans, n1sum * n2);
            }
        }
        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    long long maxScore(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        // for mapping the ele from num1 to nums2
        int n = nums1.size();
        std::vector<std::pair<int, int>> pairs;
        for (int i = 0; i < n; ++i) {
            pairs.push_back({nums1[i], nums2[i]});
        }

        // sort the above array 'pair' according to values of nums2 in descending order
        std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        // now consider each ele in nums2 as minimum and find the maximum score we can get.
        long long ans = 0;
        long long n1sum = 0;  // will store the sum of ele from nums1 that we have included till now.
        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

        for (auto& [n1, n2] : pairs) {
            n1sum += n1;
            minHeap.push(n1);  // we have to remove the min from num1 if len(heap)=>subsequence become greater than 'k'
                               // removing min because we have to maximise ans.
            if (minHeap.size() > k) {
                // then it is better to not include top of heap for cur num 'n2'.
                n1sum -= minHeap.top();
                minHeap.pop();
            }
            if (minHeap.size() == k) {
                // 'n2' is minimum till now from 'nums2' and maximum sum we can get when 'n2' will be minimum = n1sum * n2.
                ans = std::max(ans, n1sum * static_cast<long long>(n2));
            }
        }

        return ans;
    }
};
"""

# Related Q:
# 1383. Maximum Performance of a Team    => Exactly same question

# Intuition: Idea is simple: try every efficiency value from highest to lowest and at the same time
#  maintain an as-large-as-possible speed group, keep adding speed to total speed, 
# if size of engineers group exceeds K, lay off the engineer with lowest speed.

# Logic: Speed -> Nums1, performance -> nums2
# We hire the team from the most efficent people to less.
# The current iterated engineer has the smallest efficency in the team.
# The performance of a team = efficency[i] * sumSpeed

