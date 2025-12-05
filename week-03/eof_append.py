from pathlib import Path

class EBookReader:
    def __init__(self):
        pass

    def display_file_info(self, file_path):
        path = Path(file_path)
            
        stat = path.stat()
        print(f"\nFile Information for '{file_path}':")
        print(f"  Size: {stat.st_size} bytes")
        print(f"  Modified: {stat.st_mtime}")
        print(f"  Is file: {path.is_file()}")
        
        data = open(file_path, 'r')
        lines = data.readlines()
        
        print("*" * 40)
        for line in lines:
            print(line[0:-1])
        data.close()
    
    # Append content to the end of a file.
    def append_eof(self, file_path, content_to_append):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content_to_append)

def main():
    reader = EBookReader()
    append_content = "**** End of File ****"
    reader.append_eof("./test_file.txt", append_content)
    reader.display_file_info("./test_file.txt")


if __name__ == "__main__":
    main()