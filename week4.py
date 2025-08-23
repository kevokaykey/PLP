def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
        return

    modified_content = modify_content(content)
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{new_filename}'.")
    except IOError:
        print(f"Error: Cannot write to the file '{new_filename}'.")

if __name__ == "__main__":
    main()