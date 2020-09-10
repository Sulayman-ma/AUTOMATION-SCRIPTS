#! python3


"""
TEXT FILE KEYWORD SEARCH.

Keyword search giving control over directory to search and file type to search.
Supported file types: txt, all languages, csv, html and css.

Only works on my PC for now. I'll work on it to be usable anywhere.
"""

import csv
import fileinput
import os
import re
import subprocess
import fnmatch



# DONE
def text_and_code(current_path, keyword, file_extension):
    matched_lines = []
    pattern = re.compile(fr"{keyword}", re.I)

    os.chdir(current_path)
    for file in os.listdir():
        if fnmatch.fnmatch(file, ('*.' + file_extension)):
            # Open for reading and get a list of all lines in the file
            with fileinput.input(files = file) as file_object:
                for each in file_object:
                    # Using the new walrus operator
                    if result := pattern.search(each):
                        pass
                        # Adding the line to the list if the word is found.
                        matched_lines += [file_object.filename() + " - " + each]
    if len(matched_lines) < 1:
        return None

    return matched_lines


# DONE
def csv_extract(current_path, keyword, file_extension):
    matched_rows = []

    os.chdir(current_path)
    for file in os.listdir():
        if fnmatch.fnmatch(file, ('*.' + file_extension)):
            csv_path = os.getcwd() + "\\" + file

            # Open for reading
            csv_object = open(file)
            csv_reader = csv.reader(csv_object)
            for row in csv_reader:
                if keyword.casefold() in row:
                    matched_rows += [os.path.basename(csv_path) + " - " + str(row)]
            csv_object.close()

    if len(matched_rows) < 1:
        return None

    return matched_rows


def pdf_extract():
    pass


def excel_extract():
    pass


user_path = input("Enter path: ")
user_keyword = input("Search keyword: ")
user_extension = input("File extension(exclude the '.'): ")


# DONE
if user_extension == '.py' or '.java' or '.txt' or '.html' or '.css' or '.js':
    code_result = open("C:\\Users\\Sulayman\\Desktop\\search_results.txt", 'w')

    if text_and_code(user_path, user_keyword, user_extension) is None:
        code_result.write("NO MATCHES FOUND.")
        subprocess.Popen(["C:\\Users\\Sulayman\\Desktop\\search_results.txt"],
                         shell = True)
    else:
        for code in text_and_code(user_path, user_keyword, user_extension):
            code_result.write(code + '\n')
        subprocess.Popen(["C:\\Users\\Sulayman\\Desktop\\search_results.txt"],
                         shell = True)

# DONE
elif user_extension == '.csv':
    code_result = open("C:\\Users\\Sulayman\\Desktop\\search_results.txt", 'w')

    if csv_extract(user_path, user_keyword, user_extension) is None:
        code_result.write("NO MATCHES FOUND.")
        subprocess.Popen(["C:\\Users\\Sulayman\\Desktop\\search_results.txt"],
                         shell = True)
    else:
        for code in csv_extract(user_path, user_keyword, user_extension):
            code_result.write(code + '\n')
        subprocess.Popen(["C:\\Users\\Sulayman\\Desktop\\search_results.txt"],
                         shell = True)

elif user_extension == '.xlsx':
    pass

elif user_extension == '.pdf':
    pass