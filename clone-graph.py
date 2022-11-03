'''
------------------
Difficulty: Medium
------------------

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list.
The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''

'''
------------------------------------------------------------------------
Solution 1: DFS
Time: O(n+m) -> n is number of nodes, m is number of edges
Space: O(n)

Runtime: 46 ms
Memory: 13.8 MB

Once you get the concept, this is a pretty straightforward DFS solution.
There are two important intuitions here:
  - (1) we need to clone nodes while we proceed with neighbors
  - (2) we need to keep a data structure that tells which nodes have already been visitied
        in order to avoid entering an infinite cycle

There are two base cases (termination conditions) here:
  - (1) when given node does not exist -> only applies in the beginning if graph doesn't exist at all
  - (2) when node has already been visited -> we know that we can't proceed if all nodes have been visited

Thus, we check base cases, clone the node, put in visited hashmap, and do the same to the neighbors.
Line 99 is really important because we actually need to assign the list
storing recursive calls to clone_node.neighbors.
------------------------------------------------------------------------
'''
class Solution(object): 
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node):
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node

'''
------------------------------------------------------------------------
Solution 2: BFS
Time: O(n+m)
Space: O(n)

Runtime: 43 ms
Memory: 13.6 MB

This is the BFS version of the solution, where it does not use a recursion stack
but instead uses a queue (deque in order to use popleft() in this case).

We keep track of the visited nodes using a hashmap where key is original node
and value is the cloned node.

Since we're using a BFS approach, for each element we pop from the left side
of the queue, we need to check up on all its neighbors and add to queue
if it's not already been visited (and mark as visited of course).

One important thing to notice is that, for each popped node, you need to add
the cloned neighbors of it to its cloned node using line 143. This is because
we are returning visited[node] at the end, so the cloned node needs to
have all the cloned neighbors as well as its attribute.
------------------------------------------------------------------------
'''
class Solution(object):
    
    def cloneGraph(self, node):
        if not node:
            return node
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)
        
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
                
        return visited[node]