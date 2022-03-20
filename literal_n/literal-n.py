from getopt import GetoptError, getopt
import sys

def main():
    inputFile = ''
    outputFile = ''

    try:
        opts, args = getopt.getopt(sys.argv, "hi:o", ["ifile=", "ofile="])
    except GetoptError:
        print("literal-n.py -i <input-file> -o <output-file>")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print("literal-n.py -i <input-file> -o <output-file>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
    
    print("Input file is ", inputFile)
    print("Output file is", outputFile)


if __name__ == "__main__":
    main()
