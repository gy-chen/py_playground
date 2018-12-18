

class Percolation:

    def __init__(self, n):
        self._s = n ** 2
        self._grid = list(range(self._s + 2))
        self._open_grid = [False] * (self._s + 2)
        self._top = 0
        self._bottom = 1

    def open(self, row, col):
        n = self._to_n(row, col)
        self._open_grid[n] = True
        for neibor in self._neibors(n):
            self._connect(n, neibor)

    def is_open(self, row, col):
        return self._open_grid[self._to_n(row, col)]

    def is_full(self, row, col):
        if not self.is_open(row, col):
            return False
        top_root = self._root(self._top)
        n = self._to_n(row, col)
        n_root = self._root(n)
        return top_root == n_root

    @property
    def open_sites_num(self):
        return sum(self._open_grid)

    def is_percolates(self):
        top_root = self._root(self._top)
        bottom_root = self._root(self._bottom)
        return top_root == bottom_root

    def _root(self, n):
        while n != self._grid[n]:
            self._grid[n] = self._grid[self._grid[n]]
            n = self._grid[n]
        return n

    def _neibors(self, n):
        # ignore top or bottom
        n -= 2
        if n < 0:
            return
        row_size = int(self._s ** .5)
        neibors = set()
        for r_d, c_d in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            neibor = n + (r_d * row_size) + c_d
            if neibor < 0:
                neibors.add(self._top)
            elif neibor >= self._s:
                neibors.add(self._bottom)
            else:
                neibors.add(neibor + 2)
        yield from neibors

    def _connect(self, n1, n2):
        n1_root = self._root(n1)
        n2_root = self._root(n2)
        self._grid[n1_root] = n2_root

    def _to_n(self, row, col):
        size = int(self._s ** .5)
        return row * size + col + 2
