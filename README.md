本项目使用**回溯法**求解 N 皇后问题：
1.  逐行放置皇后，保证每行仅放 1 个皇后；
2.  每次放置前，通过 `is_safe` 函数检查当前位置是否与已放置皇后**同列、同左上对角线、同右上对角线**；
3.  若位置合法，则放置皇后并递归处理下一行；若递归到最后一行，则记录为一个合法解；
4.  若当前行无合法位置，则回溯至上一行，撤销当前皇后并尝试下一列。运行方式
### 1. 直接运行求解器
在 `hw01` 目录下执行：
```bash
python src/queens.py引入 Bug：将 is_safe 函数中对角线检查的起始行 row - 1 误写为 row，导致无法找到任何合法解；
错误表现：运行测试时，4 皇后和 8 皇后的解数量均为 0，触发 AssertionError；
修复方法：将 row 改回 row - 1，恢复对角线检查逻辑；
验证：重新运行测试，所有用例通过，解数量恢复正常。
### 错误日志示例
运行测试命令：
```bash
python -m unittest tests.test_queens -vtest_4_queens (tests.test_queens.TestNQueens) ... FAIL
test_8_queens (tests.test_queens.TestNQueens) ... FAIL

======================================================================
FAIL: test_4_queens (tests.test_queens.TestNQueens)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\18492\Desktop\ai-homework-main\hw01\tests\test_queens.py", line 7, in test_4_queens
    self.assertEqual(len(solutions), 2, "4 皇后问题解数量错误")
AssertionError: 0 != 2 : 4 皇后问题解数量错误

======================================================================
FAIL: test_8_queens (tests.test_queens.TestNQueens)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\18492\Desktop\ai-homework-main\hw01\tests\test_queens.py", line 11, in test_8_queens
    self.assertEqual(len(solutions), 92, "8 皇后问题解数量错误")
AssertionError: 0 != 92 : 8 皇后问题解数量错误

----------------------------------------------------------------------
Ran 2 tests in 0.005s

FAILED (failures=2)i, j = row - 1, col - 1
