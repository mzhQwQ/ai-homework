import unittest
from src.queens import solve_n_queens

class TestNQueens(unittest.TestCase):
    """测试 N 皇后问题求解器"""

    def test_4_queens(self):
        """测试 4 皇后问题：应有 2 个解"""
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2, "4 皇后解数错误")

    def test_8_queens(self):
        """测试 8 皇后问题：应有 92 个解"""
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92, "8 皇后解数错误")

if __name__ == '__main__':
    unittest.main()