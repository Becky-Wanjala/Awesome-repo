# File Creation
file_creation_success = False
file_reading_success = False
file_appending_success = False
file = None

# File Creation
try:
    file = open("my_file.txt", "w")
    file.write("Hello!\n")
    file.write("Welcome to Power Learn Project.\n")
    file.write("We offer full funded scholarship.\n")
    file.write("134\n")
    file_creation_success = True
except IOError as e:
    print("Error occurred while creating the file:", e)
finally:
    if file:
        file.close()

# File Reading and Display
if file_creation_success:
    try:
        file = open("my_file.txt", "r")
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
        file_reading_success = True
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
    except IOError as e:
        print("Error occurred while reading the file:", e)
    finally:
        if file:
            file.close()

# File Appending
if file_reading_success:
    try:
        file = open("my_file.txt", "a")
        file.write("Choose a course that you are comfortable with.\n")
        file.write("On finishing the course you will be awarded with a certificate.\n")
        file.write("Feel free to invite friends.\n")
        file.write("432\n")
        file_appending_success = True
    except IOError as e:
        print("Error occurred while appending to the file:", e)
    finally:
        if file:
            file.close()

# File Reading and Display after Appending
if file_appending_success:
    try:
        file = open("my_file.txt", "r")
        print("\nContents of my_file.txt after appending:")
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
    except IOError as e:
        print("Error occurred while reading the file:", e)
    finally:
        if file:
            file.close()
    