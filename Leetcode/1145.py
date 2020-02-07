# 1145. Binary Tree Coloring Game

'''
Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
'''

Basic idea: Binary Tree Traverse

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]
        
        def count(root):
            if root is None:
                return 0
            cntL = count(root.left)
            cntR = count(root.right)
            if root.val == x:
                c[0], c[1] = cntL, cntR
            return 1 + cntL + cntR
        
        count(root)
        return max(max(c), n-1-sum(c)) > n//2
                