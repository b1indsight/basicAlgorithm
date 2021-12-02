import random

def minfree(l:list):
    x = 0
    while True:
        if x not in l:
            return x
        x = x + 1

def main():
    test_list = [random.randint(0, 100) for x in range(0, 99)]
    print(test_list)
    print(minfree(test_list))

if __name__ == "__main__":
    main()   