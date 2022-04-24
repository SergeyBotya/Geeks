import sys

if __name__ == "__main__":
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(str(sys.argv))
        f.write('\n')
