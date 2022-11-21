'''
------------------
Difficulty: Medium
------------------

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
'''

'''
------------------------------------------------------------------------
Solution 1 - Min Heap
Time: O(nlogl) -> n is len(heights), l is ladders
Space: O(l)

Runtime: 806 ms
Memory: 24.2 MB

This is a really clever solution using the min-heap data structure.
Heap is the perfect data structure within this problem's context because
we need a data structure that we can insert climbs into, and then when needed,
retrieve the smallest climb.

The reason we want to retrieve the smallest climb is because ladders
should be used for the largest climbs. If we find a bigger climb than the
smallest ladder, we should use the ladder allocated to smallest ladder on
the bigger climb we found.

The base intuition is the following:
  - since we don't know how far we can reach with bricks and ladders we have,
    we should use ladders to the largest climbs we currently have seen.

Therefore, we first keep allocating ladders until we run out of them
a.k.a len(ladder_allocations) > ladders. If we run out of ladders and we
want to use it, we shouuld pop the smallest climb that was used by ladders
and use bricks instead for that climb.

In this process, if we run out of bricks too, that is the final index we
can reach, thus return it.
------------------------------------------------------------------------
'''
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        ladder_allocations = []
        for i in range(len(heights)-1):
            curr = heights[i]
            post = heights[i+1]
            diff = post - curr
            if diff <= 0:
                continue
            heapq.heappush(ladder_allocations, diff)
            if len(ladder_allocations) > ladders:
                smallest_ladder = heapq.heappop(ladder_allocations)
                bricks -= smallest_ladder
                if bricks < 0:
                    return i
        return len(heights)-1


'''
------------------------------------------------------------------------
Solution 2 - Binary Search for Final Researchable Building
Time: O(nlog^2n) -> binary search is O(logn) and we are going to do sorting O(nlogn) for each search
Space: O(n)

Runtime: 4319 ms
Memory: 31.8 MB

Note for binary search "mid":
  - The short rule to remember is: if you used hi = mid - 1, then use the higher midpoint.
    If you used lo = mid + 1, then use the lower midpoint. If you used both of these,
    then you can use either midpoint. If you didn’t use either (i.e., you have lo = mid and hi = mid),
    then, unfortunately, your code is buggy, and you won’t be able to guarantee convergence.
  
This is a solution that uses binary search to find which building is the
furthest reachable building. The intuition the algorithm uses is fairly simple,
it's just that it's hard to come up with it.

Given a specific building in the heights array, you are always able to figure out
whether that building is reachable or not by trying to use up all the bricks
and ladders. If we have leftover bricks/ladders or completely run out of them,
then the building is reachable. If we lack bricks/ladders, we can't reach that building.

Using binary search, we are going to find a mid point of the heights array
and see if that building is reachable using a helper function that does exactly
that. If it's reachable, it means that anything to the left is reachable
and there might or might not be a building reachable to its right. If it's
not reachable, it means anything to the right including the building is not
reachable. Thus,

            if is_reachable(mid):
                lo = mid
            else:
                hi = mid - 1
------------------------------------------------------------------------
'''
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        # Helper function to check whether or not the specified building is reachable
        # from the first building with the bricks and ladders we have.
        def is_reachable(building_index):
            # Make a sorted list of all the climbs needed to get to the given building.
            climbs = []
            for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
                if h2 - h1 > 0:
                    climbs.append(h2 - h1)
            climbs.sort()
            # Check whether or not we have enough bricks and ladders to cover all
            # of these climbs. Bricks will be used before ladders.
            bricks_remaining = bricks
            ladders_remaining = ladders
            for climb in climbs:
                # If there are enough bricks left, use those.
                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                # Otherwise, you'll have to use a ladder.
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                # And if there are no ladders either, we can't reach buildingIndex.
                else:
                    return False
            return True
         
        # Do the binary search to find the final reachable building.
        lo = 0
        hi = len(heights) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_reachable(mid):
                lo = mid
            else:
                hi = mid - 1
        return hi # Note that return lo would be equivalent.       