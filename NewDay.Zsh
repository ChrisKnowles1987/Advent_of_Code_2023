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
touch input.txt test.txt instructions.txt part1.py part2.py
