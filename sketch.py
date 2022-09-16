if __name__ == '__main__':
    numRows = 4
    ans = [[1]] * numRows
    index = 0
    while index < numRows:
        ans[index] = [1] * (index + 1)
        index += 1
    index = 2
    while index < numRows:
        j = 1
        while j < len(ans[index]) - 1:
            print(index)
            print(j)
            print(ans[index - 1][j - 1])
            print(ans[index - 1][j])
            # print()
            ans[index][j] = ans[index - 1][j - 1] + ans[index - 1][j]
            j += 1

        index += 1