#!/bin/zsh

# Check if a directory name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 directory_name"
    exit 1
fi

DIR_NAME=$1

# Create a new directory
mkdir -p "$DIR_NAME"

# Change into the new directory
cd "$DIR_NAME"

# Create the files
touch input.txt test.txt instructions.txt

# Create the .py file in the python directory with the specified template
    cat > "python/${file_name}.py" << EOF
with open('../input/${file_name}.txt', 'r') as file:
    lines = file.readlines
    
def part1():
    
    return

def part2():
    
    return

print(f'part1: {part1()}')
print(f'part2: {part2()}')
EOF
