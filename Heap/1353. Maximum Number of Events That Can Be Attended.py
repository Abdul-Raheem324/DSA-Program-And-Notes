# Method 1:

# Very good and logical.

# Intuition: For attending maximum event, we will have to attend according to ending time.
# But for knowing which all event we can attend on current day, we need to know which all event has started till current day.
# For this we need to sort event according to starting time.
 
# For getting event having lesser ending time out of event that has started till currnet day, 
# We can use heap to store ending time of all the event that has started till today and then choose minimum among them.

# In short; 
# Logic: 1) To check the availability of event at any day, we need to sort the events according to the start date.
# 2) At any day we will try to attend the event that will end soonest to attend the maximum event.
# for this we need to get the least end day of events among the available events till today.
# for this we will use the minHeap to keep track of least end day of event.

"""
# Q: Why only sorting won't work?
# Because we can't decide the cur event we have to attend or not using the start and end date of pre one.
"""

# Time : O(N *log(N) + D*log(N)), D= totalDays


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # to check which all event that will start today
        totalDays = max(end for start, end in events)   # max date till which we can attend the event
        maxAttended = 0
        eventId = 0  # will tell till which event we have traversed. will help in keep track of events that will start on a day.
        day = 1   # minimum start day of any event.
        endingSooner = []    # minHeap. to get the event that will end the soonest.
        # we can attend event till last end day.
        while day  <= totalDays:
            # Add the ending date of all the events that will start today
            while eventId < len(events) and events[eventId][0] == day:
                heapq.heappush(endingSooner, events[eventId][1])
                eventId += 1
            
            # Now remove the event from heap whose ending date was less than the cur day
            # since we can't attend these events now.
            while endingSooner and endingSooner[0] < day:
                heapq.heappop(endingSooner)
            
            # Now attend one of the event that is going to end soon 
            if endingSooner:
                heapq.heappop(endingSooner)
                maxAttended += 1
            
            day += 1
        return maxAttended
    
# Java Code 
"""
import java.util.*;

class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, Comparator.comparingInt(a -> a[0])); // Sort events by start day
        int totalDays = 0, maxAttended = 0, eventId = 0, day = 1;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // Min heap for event ending soonest
        
        // Determine the last possible event day
        for (int[] event : events) {
            totalDays = Math.max(totalDays, event[1]);
        }

        while (day <= totalDays) {
            // Push all events that start today into the heap
            while (eventId < events.length && events[eventId][0] == day) {
                minHeap.offer(events[eventId][1]);
                eventId++;
            }
            
            // Remove expired events
            while (!minHeap.isEmpty() && minHeap.peek() < day) {
                minHeap.poll();
            }

            // Attend the event that ends the soonest
            if (!minHeap.isEmpty()) {
                minHeap.poll();
                maxAttended++;
            }
            
            day++;
        }
        
        return maxAttended;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end()); // Sort events by start day
        int totalDays = 0, maxAttended = 0, eventId = 0, day = 1;
        priority_queue<int, vector<int>, greater<int>> minHeap; // Min heap for event ending soonest
        
        // Determine the last possible event day
        for (const auto& event : events) {
            totalDays = max(totalDays, event[1]);
        }

        while (day <= totalDays) {
            // Push all events that start today into the heap
            while (eventId < events.size() && events[eventId][0] == day) {
                minHeap.push(events[eventId][1]);
                eventId++;
            }
            
            // Remove expired events
            while (!minHeap.empty() && minHeap.top() < day) {
                minHeap.pop();
            }

            // Attend the event that ends the soonest
            if (!minHeap.empty()) {
                minHeap.pop();
                maxAttended++;
            }
            
            day++;
        }
        
        return maxAttended;
    }
};
"""

