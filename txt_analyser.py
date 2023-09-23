import string
from collections import Counter

def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def analyze_text_file(file_path):
    try:
        word_gen = word_generator(file_path)
        file_size = max(1, sum(1 for line in open(file_path)))

        # Counting words and total letters
        num_words = 0
        total_letters = 0
        translator = str.maketrans('', '', string.punctuation)

        print("Analyzing text...\n")

        for idx, word in enumerate(word_gen, start=1):
            num_words += 1
            cleaned_word = word.translate(translator)
            total_letters += len(cleaned_word)

            # Print progress every 10% completion
            if idx % max(1, file_size // 10) == 0:
                progress = (idx / file_size) * 100
                print(f"\rProgress: {min(progress, 100):.1f}%", end='', flush=True)

        # Counting lines
        num_lines = file_size

        # Average word length
        average_word_length = total_letters / num_words if num_words > 0 else 0

        return {
            'num_words': num_words,
            'total_letters': total_letters,
            'num_lines': num_lines,
            'average_word_length': average_word_length
        }
    except FileNotFoundError:
        return None

def sort_alphabetically(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines.sort()
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("File sorted alphabetically.")
    except FileNotFoundError:
        print("File not found.")

def sort_by_word_length(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().split()
        lines.sort(key=len)
        with open(file_path, 'w') as file:
            file.write(' '.join(lines))
        print("File sorted by word length.")
    except FileNotFoundError:
        print("File not found.")

def remove_duplicates(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        unique_words = list(set(words))
        with open(file_path, 'w') as file:
            file.write(' '.join(unique_words))
        print("Duplicate words removed.")
    except FileNotFoundError:
        print("File not found.")

def main():
    print('''
                            
            ██╗  ██╗  ████████╗██████╗  █████╗  ██████╗████████╗
            ╚██╗██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
             ╚███╔╝█████╗██║   ██████╔╝███████║██║        ██║   
             ██╔██╗╚════╝██║   ██╔══██╗██╔══██║██║        ██║   
            ██╔╝ ██╗     ██║   ██║  ██║██║  ██║╚██████╗   ██║   
            ╚═╝  ╚═╝     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   
                                                                


''')
    
    while True:
        try:
            file_path = input("Path: ")
            analysis_result = analyze_text_file(file_path)

            if analysis_result is not None:
                print("\n\nAnalysis completed:")
                print(f"Number of words: {analysis_result['num_words']}")
                print(f"Total letters: {analysis_result['total_letters']}")
                print(f"Number of lines: {analysis_result['num_lines']}")
                print(f"Average word length: {analysis_result['average_word_length']:.2f}")
        except:
            print("File not found.")
        
        print("\nOptions:")
        print("1. Sort alphabetically")
        print("2. Sort by word length")
        print("3. Remove duplicate words")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            sort_alphabetically(file_path)
        elif choice == '2':
            sort_by_word_length(file_path)
        elif choice == '3':
            remove_duplicates(file_path)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
