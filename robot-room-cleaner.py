'''
------------------
Difficulty: Hard
------------------

You are controlling a robot that is located somewhere in a room.
The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty,
and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room).
The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up.
You can assume all four edges of the grid are all surrounded by a wall.

Custom testing:

The input is only given to initialize the room and the robot's position internally.
You must solve this problem "blindfolded". In other words, you must control the robot using
only the four mentioned APIs without knowing the room layout and the initial robot's position.

Example 1:

Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Example 2:

Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms. 

Constraints:

m == room.length
n == room[i].length
1 <= m <= 100
1 <= n <= 200
room[i][j] is either 0 or 1.
0 <= row < m
0 <= col < n
room[row][col] == 1
All the empty cells can be visited from the starting position.
'''

'''
------------------------------------------------------------------------
Solution 1: Spiral Backtracking
Time: O(n-m) -> n is number of cells, m is number of obstacles
Space: O(n-m) -> n is number of cells, m is number of obstacles

Note on time complexity: we visit each non-obstacle cell once, and on each
                         visit, we check 4 directions. Thus, the total number
                         of operations would be 4*(n-m).

Runtime: 102 ms
Memory: 14.4 MB

This problem is different from other backtracking problems because the direction
of the robot matters, and there is an interface provided to control the
movement of the robot.

As always, we are going to use two techniques, constrained programming and backtracking.
  - constrained programming: use a data structure to mark cells as visited
                            so that we can limit our movements within unvisited cells
  - backtracking: this allows us to revert back to our original position
                  when there all 4 sides are blocked by obstacles and visited cells.

Since the direction of the robot matters & its movements are controlled by
the provided interface, we are going to use the right-hand rule in order to
more easily align our use of "constrained programming" with the robot's movement.
We will always move in the following order from the robot's perspective: up, right, down, left.

Within the backtracking function, the underlying intuition is:
  - (1) process the current cell first
  - (2) explore all 4 directions and see if they're valid
  - (3) only recursively proceed to the valid directions
  - (4) backtrack after the recursive call
  - (4-1) we need to manually turn the robot to the right in this problem.
          Because we strictly follow the right-hand rule, the next direction 
          will always be towards the right of the current direction.
------------------------------------------------------------------------
'''
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot(object):
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0,0), d=0):
            visited.add(cell)
            robot.clean()
            
            for i in range(4):
                new_d = (d+i)%4
                new_cell = (cell[0]+DIRECTIONS[new_d][0], cell[1]+DIRECTIONS[new_d][1])
                
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    goback()
                
                robot.turnRight()
        
        #directions will go up, right, down, left
        DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()
        backtrack()