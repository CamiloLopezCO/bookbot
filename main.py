def main():
      
    # Use the 'with' block to open the file
    with open("books/frankenstein.txt") as f:
        # Read the contents of the file
        file_contents = f.read()
    
    # Print the contents to the console
    print(file_contents)

    main()
