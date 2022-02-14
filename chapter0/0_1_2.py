import random

def minfree(l:list):
    def bsearch(l, left, right):
        if left == right:
            return left
        mid = (right - left) // 2 + left
        i = left
        j = right
        while (i <= j):
            if l[i] <= mid:
                i += 1
            else:
                l[i], l[j] = l[j], l[i]
                j -= 1
        if i - left != mid - left + 1:
            return bsearch(l, left, mid)
        else:
            return bsearch(l, mid + 1, right)
    
    return bsearch(l, 0, len(l) - 1)

def main():
    test_list = list(set([random.randint(0, 10) for x in range(0, 9)]))
    print(test_list)
    print(minfree(test_list))

if __name__ == "__main__":
    main()