def process_word(word, worddict):
    freq = worddict.get(word)
    if freq is None:
        worddict[word] = 1
    else:
        worddict[word] = freq + 1

def process_line(line, worddict):
    try:
        words = line.split()
        for word in words:
            process_word(word, worddict)
    except Exception as e:
        print(f"An error occurred while processing the line: {e}")

def process_file(file_path):
    worddict = dict()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                process_line(line, worddict)
        return worddict
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        raise

def write_output(worddict, output_path):
    try:
        with open(output_path, 'w') as file:
            for word, freq in worddict.items():
                file.write(f"{word}: {freq}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
