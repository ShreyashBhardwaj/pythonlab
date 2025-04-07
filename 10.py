def write_text_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Text file written successfully.")


def read_text_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    print("Text file content:")
    print(content)


def append_text_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
    print("Content appended successfully.")


def write_binary_file(filename, data):
    with open(filename, "wb") as file:
        file.write(data)
    print("Binary file written successfully.")


def read_binary_file(filename):
    with open(filename, "rb") as file:
        data = file.read()
    print("Binary file content:")
    print(data)


# Example Usage
text_filename = "sample.txt"
binary_filename = "sample.bin"

write_text_file(text_filename, "Hello, this is a sample text file.\n")
read_text_file(text_filename)

append_text_file(text_filename, "Appending new text.\n")
read_text_file(text_filename)

write_binary_file(binary_filename, b"\x41\x42\x43\x44")  # Writing binary data: ABCD
read_binary_file(binary_filename)
