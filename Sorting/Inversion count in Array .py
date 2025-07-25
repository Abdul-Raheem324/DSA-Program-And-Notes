# Why Merge sort?
# Ans: merge sort me merge karne time hm elements ko compare karte h left and right elements ko.
# Compare time agar left wala bda hua right wale to ek inversion me count hoga.

# Observation: 1) Agar left[i] <= right[j] i.e left[i] right ka sbse smaller se bhi chota h then left[i]
# right ka kisi bhi elements se bda nhi ho sakta h.
# so in case simply incr 'i'.

# 2) left[i] > right[j] i.e it means left me jitna bhi element hoga from index 'i' sb right[i] se bda hoga.
# kyonki sb ele left wale left[i] se >= honge (arr will be in sorted order).

# Note: Here no need to write code separately for inversion count inside merge because merge logic and inversion logic is exactly same.

# Time : O(n*logn)

"""
Note vvvi: Jahan bhi count karna ho like: find no of elements on left/right greater than cur ele etc.. then try to think of merge sort.
Only need to modify merge function according to given question.
"""

class Solution:  
    def inversionCount(self, arr, n):
        return self.merge_sort_count_inversion(arr, 0, n-1)
    
    def merge_sort_count_inversion(self, arr,low,up):
        inv_count= 0
        if(low < up):   # to check if there is more than one element.
            mid= low+ (up-low)//2
            inv_count += self.merge_sort_count_inversion(arr, low, mid)
            inv_count += self.merge_sort_count_inversion(arr, mid+1, up)
            inv_count += self.merge(arr, low, mid, up)
        return inv_count
    
    # left part should be smaller and if it doesn't mean there are inversions.
    def merge(self, arr,low,mid,up):
        low1,up1,low2,up2= low,mid,mid+1,up
        inv_count= 0
        b= []
        while(low1<= up1 and low2<= up2):
            if(arr[low1] <= arr[low2]):
                b.append(arr[low1])
                low1+=1
            else:  # all ele from low1 to up1 will be greater so count= up1- low + 1
                inv_count+= up1 - low1 + 1   # being counted for each ele on left side.
                b.append(arr[low2])
                low2+=1
        while(low1<=up1):
            b.append(arr[low1])
            low1+=1
        while(low2<=up2):
            b.append(arr[low2])
            low2+=1
        j= low
        k= 0
        while(j<=up):
            arr[j]= b[k]
            j+= 1
            k+= 1
        return inv_count

# Java Code 
"""
class Solution {
    public int inversionCount(int[] arr, int n) {
        return mergeSortCountInversion(arr, 0, n - 1);
    }

    private int mergeSortCountInversion(int[] arr, int low, int up) {
        int invCount = 0;
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            invCount += mergeSortCountInversion(arr, low, mid);
            invCount += mergeSortCountInversion(arr, mid + 1, up);
            invCount += merge(arr, low, mid, up);
        }
        return invCount;
    }

    // left part should be smaller and if it doesn't, there are inversions.
    private int merge(int[] arr, int low, int mid, int up) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int invCount = 0;
        int[] b = new int[up - low + 1];
        int index = 0;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1] <= arr[low2]) {
                b[index++] = arr[low1++];
            } else {  // all ele from low1 to up1 will be greater so count = up1 - low1 + 1
                invCount += up1 - low1 + 1;  // being counted for each ele on left side.
                b[index++] = arr[low2++];
            }
        }

        while (low1 <= up1) {
            b[index++] = arr[low1++];
        }

        while (low2 <= up2) {
            b[index++] = arr[low2++];
        }

        for (int i = 0; i < b.length; i++) {
            arr[low + i] = b[i];
        }

        return invCount;
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int inversionCount(vector<int>& arr, int n) {
        return mergeSortCountInversion(arr, 0, n - 1);
    }

private:
    int mergeSortCountInversion(vector<int>& arr, int low, int up) {
        int invCount = 0;
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            invCount += mergeSortCountInversion(arr, low, mid);
            invCount += mergeSortCountInversion(arr, mid + 1, up);
            invCount += merge(arr, low, mid, up);
        }
        return invCount;
    }

    // left part should be smaller and if it doesn't, there are inversions.
    int merge(vector<int>& arr, int low, int mid, int up) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int invCount = 0;
        vector<int> b;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1] <= arr[low2]) {
                b.push_back(arr[low1++]);
            } else {  // all ele from low1 to up1 will be greater so count = up1 - low1 + 1
                invCount += up1 - low1 + 1;  // being counted for each ele on left side.
                b.push_back(arr[low2++]);
            }
        }

        while (low1 <= up1) {
            b.push_back(arr[low1++]);
        }

        while (low2 <= up2) {
            b.push_back(arr[low2++]);
        }

        for (int i = 0; i < b.size(); i++) {
            arr[low + i] = b[i];
        }

        return invCount;
    }
};
"""
