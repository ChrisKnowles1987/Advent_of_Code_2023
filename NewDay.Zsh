#!/bin/zsh

# Check if a directory name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 directory_name"
    exit 1
fi

DIR_NAME=$1
file_name=$1  # Assign the directory name to file_name

# Create a new directory
mkdir -p "$DIR_NAME"

# Change into the new directory
cd "$DIR_NAME"

# Create the files
touch input.txt test.txt instructions.txt

# Create the .py file with the specified template
cat > "${file_name}.py" << EOF
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
def part1():
    # Your code for part 1
    return

def part2():
    # Your code for part 2
    return

print(f'part1: {part1()}')
print(f'part2: {part2()}')
EOF
