# Method 1: 

# time: O(n^2) for loop and O(1) for while loop 
# to count the no of 1's after each xor operation

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count=0
        # find xor for each pair
        # and to count the no of 1's 
        # just incr the count whenever 'while' loop executes just same logic as count the no of set bits
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                xor_pair= nums[i]^nums[j]
                # now count the no of set bits for each pair
                while(xor_pair):
                    count+= 1
                    xor_pair= xor_pair & xor_pair-1
                xor_pair= 0   # to calculate for next pair
        return count

# Java Code 
"""
class Solution {
    public int totalHammingDistance(int[] nums) {
        int count = 0;
        // find xor for each pair
        // and to count the no of 1's 
        // just incr the count whenever 'while' loop executes just same logic as count the no of set bits
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int xor_pair = nums[i] ^ nums[j];
                // now count the no of set bits for each pair
                while (xor_pair != 0) {
                    count++;
                    xor_pair = xor_pair & (xor_pair - 1);
                }
                xor_pair = 0;   // to calculate for next pair
            }
        }
        return count;
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int count = 0;
        // find xor for each pair
        // and to count the no of 1's 
        // just incr the count whenever 'while' loop executes just same logic as count the no of set bits
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int xor_pair = nums[i] ^ nums[j];
                // now count the no of set bits for each pair
                while (xor_pair != 0) {
                    count++;
                    xor_pair = xor_pair & (xor_pair - 1);
                }
                xor_pair = 0;   // to calculate for next pair
            }
        }
        return count;
    }
};

"""

# method 2: 
# instead of directly finding xor and then calculating the no of set bit, 
# we are just going by the very basic of xor operation.
#logic: the idea is the basic of how we calculate the XOR
# and how xor gives the output '1'
# xor gives the output '1' for each position when bit differs to each other
# and thats also the hamming distance meaning.
# we are doing same, we are just calculating the no of set bit of all given
# numbers for each bit position one by one.

# and hamming distance for each bit position= (no of 1's)*(no of 0's) at that position. we calculate in the same way for two no
# no of 0's will be equal= len(nums)-(no of 1's at that bit position)
# so calculate the hamming distance for each bit and add all to get the ans.
# Time:O(n)

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n,result = len(nums), 0
        for i in range(32):  # as maximum no of bits allowed is 32
            set_bit= 0  # will count the no of set bits at each bit position.
            # to get the last bit of each ele in each iteration right shift by 'i'
            # after that 'i'th bit will come at right most and then take '&' 
            # check whether that bit is '1' or '0'
            # if 1 then add in set_bit
            for j in range(len(nums)):
                set_bit+= (nums[j] >> i) & 1          
            # after each time outer loop fails,add the hamming distance of that bit to the result         
            result+= set_bit*(n-set_bit)
        return result

# Java Code 
"""
class Solution {
    public int totalHammingDistance(int[] nums) {
        int n = nums.length, result = 0;
        for (int i = 0; i < 32; i++) {  // as maximum no of bits allowed is 32
            int set_bit = 0;  // will count the no of set bits at each bit position.
            for (int j = 0; j < nums.length; j++) {
                // to get the last bit of each ele in each iteration right shift by 'i'
                // after that 'i'th bit will come at right most and then take '&' 
                // check whether that bit is '1' or '0'
                // if 1 then add in set_bit
                set_bit += (nums[j] >> i) & 1;
            }
            // after each time outer loop fails, add the hamming distance of that bit to the result
            result += set_bit * (n - set_bit);
        }
        return result;
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int n = nums.size(), result = 0;
        for (int i = 0; i < 32; i++) {  // as maximum no of bits allowed is 32
            int set_bit = 0;  // will count the no of set bits at each bit position.
            for (int j = 0; j < nums.size(); j++) {
                // to get the last bit of each ele in each iteration right shift by 'i'
                // after that 'i'th bit will come at right most and then take '&' 
                // check whether that bit is '1' or '0'
                // if 1 then add in set_bit
                set_bit += (nums[j] >> i) & 1;
            }
            // after each time outer loop fails, add the hamming distance of that bit to the result
            result += set_bit * (n - set_bit);
        }
        return result;
    }
};

"""
