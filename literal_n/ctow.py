#!/usr/bin/python3

import sys, getopt

def main():
    inputFile = sys.argv[1]
    argumentList = sys.argv[1:]
    options = "hi:r"
    long_options = ["help", "ifile", "reverse"]
    reverse = False;

    try:
        opts, args = getopt.getopt(argumentList, options, long_options)
    except getopt.GetoptError:
        print("ERROR: literal-n.py -i <input-file> ")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("literal-n.py -i <input-file> ")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            print("Input file is ", inputFile)
        elif opt in ("-r", "--reverse"):
            reverse = True
    
    file_in = open(inputFile)
    lines = file_in.readlines()

    if reverse:
        for line in lines:
            newline = line.replace('\n', '\\n')
            newline = newline.replace('\t', '\\t')
            print(newline)
    else:
        for line in lines:
            newline = line.replace('\\n', '\n')
            newline = newline.replace('\\t', '\t')
            print(newline)


if __name__ == "__main__":
    main()
