import unittest
import percolation


class PercolationTest(unittest.TestCase):

    def setUp(self):
        self.p = percolation.Percolation(5)

    def test_init(self):
        self.assertEqual(len(self.p._grid), 27)
        self.assertEqual(self.p._grid, list(range(len(self.p._grid))))
        self.assertEqual(self.p._top, 0)
        self.assertEqual(self.p._bottom, 1)

    def test_to_n(self):
        self.assertEqual(self.p._to_n(0, 0), 2)
        self.assertEqual(self.p._to_n(1, 0), 7)
        self.assertEqual(self.p._to_n(0, 1), 3)
        self.assertEqual(self.p._to_n(1, 1), 8)

    def test_root(self):
        for n in range(len(self.p._grid)):
            self.assertEqual(self.p._root(n), n)

    def test_connect(self):
        self.p._connect(2, 3)
        self.assertEqual(self.p._root(2), self.p._root(3))
        self.p._connect(2, 4)
        self.assertEqual(self.p._root(2), self.p._root(4))
        self.assertEqual(self.p._root(3), self.p._root(4))

    def test_neibors(self):
        self.assertEqual(set(self.p._neibors(2)), {0, 3, 7})
        self.assertEqual(set(self.p._neibors(6)), {0, 5, 7, 11})
        self.assertEqual(set(self.p._neibors(7)), {2, 6, 8, 12})
        self.assertEqual(set(self.p._neibors(12)), {7, 11, 13, 17})
        self.assertEqual(set(self.p._neibors(21)), {16, 20, 22, 26})
        self.assertEqual(set(self.p._neibors(22)), {17, 21, 23, 1})
        self.assertEqual(set(self.p._neibors(26)), {21, 25, 1})

    def test_open(self):
        self.p.open(0, 0)
        self.assertEqual(self.p._root(self.p._top), self.p._root(2))
        self.assertEqual(self.p._root(3), self.p._root(2))
        self.assertEqual(self.p._root(7), self.p._root(2))

    def test_is_open(self):
        self.p.open(0, 0)
        self.assertTrue(self.p.is_open(0, 0))
        self.assertFalse(self.p.is_open(0, 1))
        self.assertFalse(self.p.is_open(1, 0))

    def test_is_full(self):
        self.assertFalse(self.p.is_full(0, 0))
        self.p.open(0, 0)
        self.assertTrue(self.p.is_full(0, 0))
        self.assertFalse(self.p.is_full(1, 0))
        self.assertFalse(self.p.is_full(0, 1))
        self.p.open(1, 0)
        self.assertTrue(self.p.is_full(1, 0))
        self.assertFalse(self.p.is_full(1, 1))

    def test_open_sites_num(self):
        self.assertEqual(self.p.open_sites_num, 0)
        self.p.open(0, 0)
        self.assertEqual(self.p.open_sites_num, 1)
        self.p.open(0, 0)
        self.assertEqual(self.p.open_sites_num, 1)
        self.p.open(0, 1)
        self.p.open(1, 0)
        self.assertEqual(self.p.open_sites_num, 3)

    def test_is_percolates(self):
        self.assertFalse(self.p.is_percolates())
        self.p.open(0, 3)
        self.assertFalse(self.p.is_percolates())
        self.p.open(1, 3)
        self.assertFalse(self.p.is_percolates())
        self.p.open(2, 3)
        self.assertFalse(self.p.is_percolates())
        self.p.open(3, 3)
        self.assertFalse(self.p.is_percolates())
        self.p.open(4, 3)
        self.assertTrue(self.p.is_percolates())


if __name__ == '__main__':
    unittest.main()
