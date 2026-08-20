def Check_Palindrome(n: int, s: str) -> bool:
    count = 0

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            count += 1

    return count <= 1


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))