def solve_n_queens(n: int) -> list[list[str]]:
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_safe(row: int, col: int) -> bool:
        # 检查列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查左上对角线
        i, j = row-1 , col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row: int):
        if row == n:
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions

if __name__ == "__main__":
    n = 8
    results = solve_n_queens(n)
    print(f"✅ {n} 皇后问题共有 {len(results)} 个解")
    if results:
        print("第一个解的棋盘：")
        for row in results[0]:
            print(row)