from pathlib import Path

class EBookReader:
    def __init__(self):
        pass

    def display_file_info(self, file_path):
        path = Path(file_path)
        
        data = open(file_path, 'r')
        lines = data.readlines()
        
        for line in lines:
            print(line[0:-1])
        data.close()
    
    # Append content to the end of a file.
    def append_eof(self, file_path):
        content_to_append = "**** End of File ****"
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n")
            file.write(content_to_append)

def main():
    reader = EBookReader()
    reader.append_eof("./test_file.txt")
    reader.display_file_info("./test_file.txt")


if __name__ == "__main__":
    main()