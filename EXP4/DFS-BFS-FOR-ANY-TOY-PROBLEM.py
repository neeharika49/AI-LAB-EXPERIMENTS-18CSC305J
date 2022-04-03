from queue import Queue

class NQueens:

def _init_(self, size):
self.size = size

def solve_dfs(self):
if self.size &lt; 1:
return []
solutions = []
stack = [[]]
while stack:
solution = stack.pop()
if self.conflict(solution):
continue
row = len(solution)
if row == self.size:
solutions.append(solution)
continue
for col in range(self.size):
queen = (row, col)
queens = solution.copy()
queens.append(queen)
stack.append(queens)
return solutions

def solve_bfs(self):
if self.size &lt; 1:
