# Method 1: 

# Note vvi: In this type of questions, focus on most frequent char first.
# And try to put them one after the other first.

# Here try to put the most frequent char just after other.

# Logic:  store pair of {frequency,char} in a Heap. Then while Heap.size()>1 , 
# at every iteration, take out the top two elements, append them to the ans string, 
# decrease their frequency by 1 and push them again in the Heap.

# When the loop will break, either the Heap became empty or of 1 size.

# If it's empty, return the ans string.
# if it has size == 1, check the remaining frequency of the top/last element, if its 1, append it and return ans.
# Otherwise, return ""

# Note: If there is some character c with freq(c)>(n+1)/2 then it is impossible

# Time: O(n*logn), space: O(n)

import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        frequency = collections.defaultdict(int)
        for i, c in enumerate(s):
            frequency[c] += 1
        
        maxHeap = []
        for key, value in frequency.items():
            maxHeap.append((-1* value, key))  
            # while inserting converting freq into negative to get the char with max freq first

        heapq.heapify(maxHeap)   # to get char with max freq on top
        while len(maxHeap) > 1:
            f1, c1 = heapq.heappop(maxHeap)
            f2, c2 = heapq.heappop(maxHeap)
            ans += c1 + c2
            f1 , f2 = -1*f1 - 1,  -1*f2 - 1   # converting into +ve
            if f1 > 0 :
                heapq.heappush(maxHeap, (-1*f1, c1))  
            if f2 > 0 :
                heapq.heappush(maxHeap, (-1*f2 , c2))
        if len(maxHeap) == 0:
            return ans
        f, c = heapq.heappop(maxHeap)
        if -1*f == 1:
            return ans + c
        return ""

# Java Code 
"""
import java.util.*;

public class Solution {
    public String reorganizeString(String s) {
        StringBuilder ans = new StringBuilder();
        Map<Character, Integer> frequency = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (Map.Entry<Character, Integer> entry : frequency.entrySet()) {
            maxHeap.add(new int[]{-1 * entry.getValue(), entry.getKey()});  
            // while inserting converting freq into negative to get the char with max freq first
        }

        while (maxHeap.size() > 1) {
            int[] f1 = maxHeap.poll();
            int[] f2 = maxHeap.poll();
            ans.append((char)f1[1]);
            ans.append((char)f2[1]);
            f1[0] = -f1[0] - 1;   // converting into +ve
            f2[0] = -f2[0] - 1;
            if (f1[0] > 0) {
                maxHeap.add(new int[]{-1 * f1[0], f1[1]});
            }
            if (f2[0] > 0) {
                maxHeap.add(new int[]{-1 * f2[0], f2[1]});
            }
        }

        if (maxHeap.isEmpty()) {
            return ans.toString();
        }

        int[] last = maxHeap.poll();
        if (-last[0] == 1) {
            return ans.append((char)last[1]).toString();
        }

        return "";
    }
}
"""
# C++ Code 
"""
#include <string>
#include <unordered_map>
#include <queue>

class Solution {
public:
    std::string reorganizeString(std::string s) {
        std::string ans = "";
        std::unordered_map<char, int> frequency;
        for (int i = 0; i < s.size(); ++i) {
            frequency[s[i]]++;
        }

        using pii = std::pair<int, char>;
        auto cmp = [](pii a, pii b) { return a.first > b.first; };
        std::priority_queue<pii, std::vector<pii>, decltype(cmp)> maxHeap(cmp);

        for (auto& [key, value] : frequency) {
            maxHeap.push({-1 * value, key});
            // while inserting converting freq into negative to get the char with max freq first
        }

        while (maxHeap.size() > 1) {
            auto [f1, c1] = maxHeap.top(); maxHeap.pop();
            auto [f2, c2] = maxHeap.top(); maxHeap.pop();
            ans += c1;
            ans += c2;
            f1 = -f1 - 1;   // converting into +ve
            f2 = -f2 - 1;
            if (f1 > 0) {
                maxHeap.push({-1 * f1, c1});
            }
            if (f2 > 0) {
                maxHeap.push({-1 * f2, c2});
            }
        }

        if (maxHeap.empty()) {
            return ans;
        }

        auto [f, c] = maxHeap.top(); maxHeap.pop();
        if (-f == 1) {
            return ans + c;
        }

        return "";
    }
};
"""

# Method 2: 
# Most optimised

# Note: Keep this Q and logic in mind, it is used in a lot of problems.

# Logic: 
# We construct the resulting string in sequence: at position 0, 2, 4, ... and then 1, 3, 5, ...
# In this way, we can make sure there is always a gap between the same characters

# Consider this example: "aaabbbcdd", we will construct the string in this way:

# a _ a _ a _ _ _ _ // fill in "a" at position 0, 2, 4
# a b a _ a _ b _ b // fill in "b" at position 6, 8, 1
# a b a c a _ b _ b // fill in "c" at position 3
# a b a c a d b d b // fill in "d" at position 5, 7

# Note: 1st put the most frequent element.

# Time: O(n)

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        frequency = collections.defaultdict(int)
        maxLength , letter = 0 , None
        for c in s:
            frequency[c] += 1
            if frequency[c] > maxLength:
                maxLength = frequency[c]
                letter = c

        if maxLength > (n + 1)//2:
            return ""
        # 1st put the char at even index i.e 0, 2, 4, 6,..
        # Then put at odd index i.e 1, 3, 5,...
        ans = [None] * n
        # first put the most frequent char i.e letter
        ind = 0
        while frequency[letter] > 0:
            ans[ind] = letter
            ind += 2   # putting with gap to avoid same char together
            frequency[letter] -= 1
        # Now place remaining char after index 'ind' if got filled till last then start from index 1, 3, 5,...
        for c in s:
            while frequency[c] > 0:
                if ind >= n:
                    ind = 1  # start putting from index '1'.
                ans[ind] = c
                ind += 2
                frequency[c] -= 1
        return "".join(ans)

# Java Code 
"""
import java.util.*;

public class Solution {
    public String reorganizeString(String s) {
        int n = s.length();
        Map<Character, Integer> frequency = new HashMap<>();
        int maxLength = 0;
        char letter = 0;
        for (char c : s.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
            if (frequency.get(c) > maxLength) {
                maxLength = frequency.get(c);
                letter = c;
            }
        }

        if (maxLength > (n + 1) / 2) {
            return "";
        }
        // 1st put the char at even index i.e 0, 2, 4, 6,..
        // Then put at odd index i.e 1, 3, 5,...
        char[] ans = new char[n];
        // first put the most frequent char i.e letter
        int ind = 0;
        while (frequency.get(letter) > 0) {
            ans[ind] = letter;
            ind += 2;   // putting with gap to avoid same char together
            frequency.put(letter, frequency.get(letter) - 1);
        }
        // Now place remaining char after index 'ind' if got filled till last then start from index 1, 3, 5,...
        for (char c : s.toCharArray()) {
            while (frequency.getOrDefault(c, 0) > 0) {
                if (ind >= n) {
                    ind = 1;  // start putting from index '1'.
                }
                ans[ind] = c;
                ind += 2;
                frequency.put(c, frequency.get(c) - 1);
            }
        }
        return new String(ans);
    }
}
"""
# C++ Code 
"""
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string reorganizeString(std::string s) {
        int n = s.size();
        std::unordered_map<char, int> frequency;
        int maxLength = 0;
        char letter = 0;
        for (char c : s) {
            frequency[c]++;
            if (frequency[c] > maxLength) {
                maxLength = frequency[c];
                letter = c;
            }
        }

        if (maxLength > (n + 1) / 2) {
            return "";
        }
        // 1st put the char at even index i.e 0, 2, 4, 6,..
        // Then put at odd index i.e 1, 3, 5,...
        std::vector<char> ans(n);
        // first put the most frequent char i.e letter
        int ind = 0;
        while (frequency[letter] > 0) {
            ans[ind] = letter;
            ind += 2;   // putting with gap to avoid same char together
            frequency[letter]--;
        }
        // Now place remaining char after index 'ind' if got filled till last then start from index 1, 3, 5,...
        for (char c : s) {
            while (frequency[c] > 0) {
                if (ind >= n) {
                    ind = 1;  // start putting from index '1'.
                }
                ans[ind] = c;
                ind += 2;
                frequency[c]--;
            }
        }
        return std::string(ans.begin(), ans.end());
    }
};
"""