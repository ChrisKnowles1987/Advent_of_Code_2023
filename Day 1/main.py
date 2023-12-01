

def main():
    with open('calibration.txt', 'r') as file:
        lines = [line.strip() for line in file]
        print (lines)
    
    return

if __name__ == '__main__':
    main()

