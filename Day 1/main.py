numbers = '0123456789'
letters = 'otfsen' #first letter of each possible wrd number
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
words = words_dict.keys()
def main():
    selected_chars = ''
    with open('calibration.txt', 'r') as file:
        lines = [line.strip() for line in file]
        for line in lines:
            selected_chars = []
            for index, c in enumerate(line):
                
                if c in numbers:
                    selected_chars.append(int(c))
                    
                if c in letters:
                    
                    for word in words_dict.keys():
                        x = word[0]
                        start_index = line[index:].find(word) + index
                        value = words_dict[word]
                        
                   
                        if  (x == c) and (start_index == index): #and (line[index+1] == word[1]):
                         selected_chars.append(int(value))
                         
            # print(selected_chars)
            first_char = selected_chars[0]
            last_char = selected_chars[-1]
            number = str(first_char) + str(last_char)
            array.append(int(number))
            print(f'{line} {number}')
    
            
    print(sum(array))
    # return (sum(array))

if __name__ == '__main__':
    main()

