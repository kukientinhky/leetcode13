def main():
    s = "MCMXCIV"
    change = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    begin = 0
    ans = 0
    while begin < len(s)-1:

        if (begin <= len(s) - 2) and (change[s[begin]]>=change[s[begin+1]]):
            ans = ans + change[s[begin]]
            begin = begin + 1
        else:
            ans = ans + change[s[begin + 1]] - change[s[begin]]
            begin = begin + 2
    if begin == len(s) - 1:
        ans = ans + change[s[begin]]
    print(ans)
if __name__ == "__main__":
    main()