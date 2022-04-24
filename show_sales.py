import sys

if __name__ == "__main__":
    prices = [0]
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            lines = line.replace('\n', '')
            lines = lines.replace("'", '')
            lines = lines.replace(']', '')
            lines = lines.split(', ')
            prices.append(lines[1])
    if sys.argv == ['show_sales.py']:
        print(*prices[1:], sep='\n')
    elif len(sys.argv) == 2:
        print(*prices[int(sys.argv[1]):], sep='\n')
    else:
        print(*prices[int(sys.argv[1]):int(sys.argv[2])+1], sep='\n')

