def main():
    file_name = input("What file would you like to open?")
    try:
        file_handle = open(file_name, "r")
        for line in file_handle:
            print("line")
    except: FileExistsError
    print("The file {file_name}does not exist")

    if_name_=="_main_main():
