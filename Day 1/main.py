numbers = '0123456789'
words_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }   
array =[]
    
def main():
    
    with open('calibration.txt', 'r') as file:
        lines = [line.strip() for line in file]
        for line in lines:
            for word in words_dict.keys():
                value = words_dict[word]
                if word in line:
                    line = line.replace(word,value)
                    print(line)
            
            selected_chars = ''.join([c for c in line if c in numbers])
            first_char = selected_chars[0]
            last_char = selected_chars[-1]
            number = first_char + last_char
            array.append(int(number))
            
        print(sum(array))
    return (sum(array))

if __name__ == '__main__':
    main()

