class UnionFind:
    def __init__(self, arr):
        self.parents = {}
        self.rank = {}

        for i in arr:
            self.parents[i] = i
            self.rank[i] = 1

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def add(self, i):
        if i not in self.parents:
            self.parents[i] = i
            self.rank[i] = 1

    def union(self, i, j):
        rootx = self.find(i)
        rooty = self.find(j)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parents[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, i, j):
        if i not in self.parents or j not in self.parents:
            return False
        return self.find(i) == self.find(j)
