import random

def minfree(l:list):
    N = len(l) + 1
    buffer = [False for i in range(0, N)]
    for i in l:
        if i < N:
            buffer[i] = True
    for i, flag in enumerate(buffer):
        if flag is False:
            return i

def main():
    test_list = [random.randint(0, 100) for x in range(0, 99)]
    print(test_list)
    print(minfree(test_list))

if __name__ == '__main__':
    main()