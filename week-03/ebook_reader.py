import os
import sys
from pathlib import Path

class EBookReader:
    def __init__(self):
        pass

    def read_text_file(self, file_path):
        # Path handling
        # e.g. ./demo_file.txt -> demo_file.txt
        path = Path(file_path)
            
        # Check if file exists
        if not path.exists():
            print(f"Error: File '{file_path}' does not exist.")
            return None
            
        # Read the file with UTF-8 encoding
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Successfully read {len(content)} characters from '{file_path}'")
            return content

    def display_file_info(self, file_path):
        path = Path(file_path)
            
        stat = path.stat()
        print(f"\nFile Information for '{file_path}':")
        print(f"  Size: {stat.st_size} bytes")
        print(f"  Modified: {stat.st_mtime}")
        print(f"  Is file: {path.is_file()}")
        print(f"  Is readable: {os.access(path, os.R_OK)}")
        
        data = open(file_path)
        lines = data.readlines()
        
        print("*" * 40)
        for line in lines:
            print(line[0:-1])
        data.close()

    def count_asterisk_in_code(self, file_path):
        path = Path(file_path)
            
        file = open(path)
        content = file.read()
        file.close()
        
        asterisk_count = content.count('*')
        
        print(f"Total '*' characters found: {asterisk_count}")
        
        lines = content.split('\n')
        print("\nLine-by-line breakdown:")
        line_num = 1
        for line in lines:
            line_asterisk_count = line.count('*')
            if line_asterisk_count > 0:
                print(f"  Line {line_num}: {line_asterisk_count} asterisk(s) - '{line.strip()}'")
            line_num += 1
        
        return asterisk_count

def main():
    reader = EBookReader()
    reader.read_text_file("./demo_file.txt")
    reader.display_file_info("./demo_file.txt")
    
    # Count asterisks in the current code file
    current_file = __file__
    reader.count_asterisk_in_code(current_file)


if __name__ == "__main__":
    main()