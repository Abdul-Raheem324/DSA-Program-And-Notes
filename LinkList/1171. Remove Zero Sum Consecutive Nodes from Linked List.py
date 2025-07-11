# My mistakes:

# Reason for my mistakes:
# we are updating the pointer of ans when we find any possible ans.
# Hmko same curSum aage bhi mil sakta h and size is samay subarray ka bda hoga.(isi ke chalte mera ans galat aa rha).
# agar aage mila to ans ke saath hm connect nhi payenge "other nodes ko remove karke".

# How to solve this?
# since we have to get max nodes for a curSum so in 1st iteration we will store the prefixSum with last node.
# Then in 2nd iteratin we will move our pointer to the value of prefixSum (all these nodes will be part of ans).
# kyonki hmko duplicate curSum milne pe beech wala nodes ko remove kar denge (sum== 0 ya k mil jayega beech wala ko remove karke).

# yhi hm correct wale me karenge

# my mistake:
# after removing there still can be such sequence.
# Because here storing only first node for each 'curSum' so we may get more sequence even after removing. 
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= pre= ListNode(0)
        dummy.next= head
        cur= head
        prefixSum= {0: dummy}  # sum-> till node. if we remove this extra sum(cursum- k),k= 0 here. then we can get sum= 0 from 'node.next' in hashmap  till cur.
        curSum= 0
        while cur:
            curSum+= cur.val
            if (curSum- 0) in prefixSum:  # just generalise from sum= 0 to 'k'. 
                prefixSum[(curSum- 0)].next= cur.next   # we can get sum= 0. so just remove that zero sum part.
            if curSum not in prefixSum:
                prefixSum[curSum]= cur
            cur= cur.next
        return dummy.next


# Method 1: 

# Logic:
# Assume the input is an array like 'count subarray having sum = k' etc.
# Do you know how to solve it?
# Scan from the left, and calculate the prefix sum.
# Whenever meet the seen prefix,
# remove all elements of the subarray between them.

# Implementation:
# Iterate for the first time,
# calculate the prefix sum.

# Iterate for the second time,
# calculate the prefix sum,
# and directly skip to last occurrence of this prefix

# Note: Calculating prefixSum and updating ans parallely won't work here 
# Because we can't traverse backward in linklist. We won't be able to connect the nodes.
# So 1st calculate the prefixSum and then find the ans.

"""
First we will calculate the prefix sum of each node and store it in a hashmap.
Then we will iterate through the linked list again, using the prefix sum to determine which nodes to remove.
So we will use a hashmap to store the prefix sums and their corresponding nodes.
"""
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list twice.
Space Complexity: O(n), for the hashmap that stores the prefix sums and their corresponding nodes.
"""
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next = head
        cur = head
        prefixSum = {0: dummy}  # [presum: cur]. prefix calculates the prefix sum from the first node to the current cur node.
                                # in case of same curSum it will store the latest node . 
                                # Storing latest will help in removing longest chain of nodes.
        curSum= 0
        while cur:
            curSum += cur.val
            prefixSum[curSum] = cur
            cur = cur.next
        
        curSum= 0
        # Go from the dummy node again to set the next node to be the last node for a prefix sum 
        cur= dummy  # starting from 'dummy' node because we may have to remove nodes from start also
                     # if prefixSum has value = 0
        while cur:
            curSum += cur.val
            # if curSum is in 'prefixSum' then it means sum of node from 'cur.next' to node 'prefixSum[curSum]' is = 0.
            # So point 'cur.next' to node after node 'prefixSum[curSum]'.
            cur.next= prefixSum[curSum].next   # remove the nodes if cursum has occured more than one time else will automatically point to his next.
            cur = cur.next
        return dummy.next


# Java
"""
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = head;
        Map<Integer, ListNode> prefixSum = new HashMap<>();
        int curSum = 0;

        prefixSum.put(0, dummy); 
        // [presum: cur]. prefix calculates the prefix sum from the first node to the current cur node.
        // in case of same curSum it will store the latest node.
        // Storing latest will help in removing longest chain of nodes.

        while (cur != null) {
            curSum += cur.val;
            prefixSum.put(curSum, cur);
            cur = cur.next;
        }

        curSum = 0;
        // Go from the dummy node again to set the next node to be the last node for a prefix sum 
        cur = dummy; 
        // starting from 'dummy' node because we may have to remove nodes from start also
        // if prefixSum has value = 0

        while (cur != null) {
            curSum += cur.val;
            // if curSum is in 'prefixSum' then it means sum of node from 'cur.next' to node 'prefixSum[curSum]' is = 0.
            // So point 'cur.next' to node after node 'prefixSum[curSum]'.
            cur.next = prefixSum.get(curSum).next; 
            // remove the nodes if cursum has occurred more than one time else will automatically point to his next.
            cur = cur.next;
        }

        return dummy.next;
    }
}


"""

# C++
"""
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        unordered_map<int, ListNode*> prefixSum;
        ListNode* cur = head;
        int curSum = 0;

        prefixSum[0] = dummy;
        // [presum: cur]. prefix calculates the prefix sum from the first node to the current cur node.
        // in case of same curSum it will store the latest node.
        // Storing latest will help in removing longest chain of nodes.

        while (cur) {
            curSum += cur->val;
            prefixSum[curSum] = cur;
            cur = cur->next;
        }

        curSum = 0;
        // Go from the dummy node again to set the next node to be the last node for a prefix sum 
        cur = dummy; 
        // starting from 'dummy' node because we may have to remove nodes from start also
        // if prefixSum has value = 0

        while (cur) {
            curSum += cur->val;
            // if curSum is in 'prefixSum' then it means sum of node from 'cur->next' to node 'prefixSum[curSum]' is = 0.
            // So point 'cur->next' to node after node 'prefixSum[curSum]'.
            cur->next = prefixSum[curSum]->next; 
            // remove the nodes if cursum has occurred more than one time else will automatically point to his next.
            cur = cur->next;
        }

        return dummy->next;
    }
};


"""

