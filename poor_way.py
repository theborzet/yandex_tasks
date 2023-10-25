#basic games theory
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) == m:
            matrix.append(row)
        else:
            raise(ValueError)
    ans = [[0] * m for _ in range(n)]

    ans[0][0] = matrix[0][0]
    for i in range(1, n):
        ans[i][0] = ans[i-1][0] + matrix[i][0]
    for j in range(1, m):
        ans[0][j] = ans[0][j - 1] + matrix[0][j]
    for i in range(1,n):
        for j in range(1, m):
            ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + matrix[i][j]
    print(ans[-1][-1])
    # print(*matrix, sep='\n')
if __name__ == '__main__':
    main()