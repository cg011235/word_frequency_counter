#!/bin/python

import argparse
from process import process_file, write_output

def main():
    parser = argparse.ArgumentParser(description="A word frequency counter.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    parser.add_argument("-o", "--output", type=str, help="The output file name")
    args = parser.parse_args()
    
    filename = args.filename
    output = args.output

    try:
        word_freq = process_file(filename)
        if output:
            write_output(word_freq, output)
        else:
            for word, freq in word_freq.items():
                print(f"{word}: {freq}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()