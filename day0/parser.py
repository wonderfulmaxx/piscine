

def parsing(recursive,level,path,nb_args):
   


    if not re.match(r'https?://', url):
        print ("Please enter a valid URL")
        sys.exit(1)

    counter = 1

    if nb_args < 2:
        print("Too few arguments")
        sys.exit(1)

    while counter < nb_args:
        if sys.argv[counter] == "-p":
            if counter + 1 < nb_args - 1 and not re.match(r'^-', sys.argv[counter+1]):
                path = sys.argv[counter + 1]
                counter += 1
            else:
                print("Enter a path after -p")
                sys.exit(1)
        elif sys.argv[counter] == "-r":
            recursive = True
        elif sys.argv[counter] == "-l":
            if counter + 1 < nb_args - 1 and sys.argv[counter + 1].isdigit() and not re.match(r'^-', sys.argv[counter+1]):
                level = sys.argv[counter+1]
                counter += 1
            else:
                print("Enter a maximum depht level after -l")
                sys.exit(1)
        elif counter == nb_args - 1:
            if not re.match(r'^https?://', sys.argv[counter]):
                print("Please enter a valid url")
                sys.exit(1)
        counter += 1

    return (recursive,level,path)