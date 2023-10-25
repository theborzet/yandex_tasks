def main():
    N = int(input())
    included = [False] * N

    nails = list(map(int, input().split()))
    nails.sort()

    total_lenght = 0
    total_lenght += nails[1] - nails[0]
    included[0], included[1] = True, True
    for i in range(2, N-1):
        if not included[i]:
            distance = min(abs(nails[i] - nails[i-1]), abs(nails[i+1] - nails[i]))
            total_lenght += distance


    print(total_lenght)


if __name__ == '__main__':
    main()