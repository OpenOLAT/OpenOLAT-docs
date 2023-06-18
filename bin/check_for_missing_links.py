import os
import openpyxl

def search_for_faulty_links(directory):
    number = 0
    for root, dirs, files in os.walk(directory):

        for file in files:
            already_done = []
            if file.endswith(".md"):
                number = number +1
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    # Perform operations on the file
                    print(f"Opening file number: {file_path}")
                    print("NUMBER "+ str(number))
                    content = f.read()

                lines = content.split('\n')
                occurrences = []

                for line in lines:
                    if '.md' in line:
                        occurrences.append(line)

                for element in occurrences:
                    inside_brackets = False
                    check_for_ending = 0
                    link_name = ""
                    for char in element:
                        
                        if char == "(" and not inside_brackets:
                            inside_brackets = True
                        elif char == "(" and inside_brackets:
                            check_for_ending = 0
                            link_name = ""
                        elif char == "." and inside_brackets:
                            check_for_ending = 1
                            link_name += char
                        elif char == "m" and inside_brackets and check_for_ending == 1:
                            check_for_ending = 2
                            link_name += char
                        elif char == "d" and inside_brackets and  check_for_ending == 2:
                            link_name += char
                            inside_brackets = False
                            check_for_ending = 0

                            os.chdir(os.path.dirname(file_path))

                            if not os.path.isfile(link_name) and link_name not in already_done:
                                if link_name.startswith("../../manual_admin/"):
                                    new_link = link_name.replace("../../manual_admin/","../../manual_admin/docs/")
                                    if not os.path.isfile(new_link):
                                        with open("/Users/yves.meister/OpenOLAT-docs/bin/faulty_links.txt", "a") as file:
                                            file.write(file_path+"\n")
                                            file.write("---------" + link_name+"\n")
                                            file.write("\n")
                                    else:
                                        modified_content = content.replace(link_name, new_link)
                                        content = modified_content
                                        os.chdir(original_directory)

                                        with open(file_path, "w") as file:
                                            file.write(content)

                                        os.chdir(os.path.dirname(file_path))

                                else:
                                    new_link = get_correct_link(link_name, file_path)

                                    if new_link != "..//" and new_link != None:

                                        if not os.path.isfile(new_link):
                                            with open("/Users/yves.meister/OpenOLAT-docs/bin/faulty_links.txt", "a") as file:
                                                file.write(file_path+"\n")
                                                file.write("XXXXXXXXXXX" + new_link+"\n")
                                                file.write("\n")

                                        else:
                                            modified_content = content.replace(link_name, new_link)
                                            content = modified_content
                                            os.chdir(original_directory)

                                            with open(file_path, "w") as file:
                                                file.write(content)

                                            os.chdir(os.path.dirname(file_path))

                                    else:     
                                        with open("/Users/yves.meister/OpenOLAT-docs/bin/faulty_links.txt", "a") as file:
                                            file.write(file_path+"\n")
                                            file.write("---------" + link_name+"\n")
                                            file.write("\n")

                            os.chdir(original_directory)
                            already_done.append(link_name)
                            link_name=""
                        elif inside_brackets:
                            check_for_ending = 0
                            link_name += char

#retrievs the correct relative path to  the file
def get_correct_link(current_link, file_path):
    if current_link.startswith("../") and current_link[3] != ".":
        delimiter = "/"
        split_string = current_link.split(delimiter)
        folder = split_string[1]
        file = split_string[2]
        new_folder = ""
        new_file = ""
        new_link = ""
        german = False

        if ".de" in file:
            file = remove_last_six_characters(file)
            file = file + ".md"
            german = True

        for i in range(2,215): 
            if i in (38, 44, 64, 65, 91, 124, 129, 130, 134, 143, 147, 151, 163, 168, 176, 180, 193):
                continue
            if read_excel_cell(excel_path, sheet_name, "A"+str(i)) == folder and read_excel_cell(excel_path, sheet_name, "B"+str(i)) == file:
                new_folder = read_excel_cell(excel_path, sheet_name, "D"+str(i))
                new_file = read_excel_cell(excel_path, sheet_name, "E"+str(i))
                break
        
        new_link = "../" + new_folder + "/" + new_file
        if german and new_link != "..//":
            new_link = remove_last_three_characters(new_link)
            new_link = new_link + ".de.md"
        return new_link     
    elif  current_link[0] != ".":
        delimiter = "/"
        split_string = file_path.split(delimiter)
        folder = split_string[-2]
        file = split_string[-1]
        new_folder = ""
        new_file = current_link
        new_link = ""
        german = False

        if ".de" in file:
            file = remove_last_six_characters(file)
            file = file + ".md"

        if ".de" in new_file:
            new_file = remove_last_six_characters(new_file)
            new_file = new_file + ".md"
            german = True
        
        for i in range(2,215): 
            if i in (38, 44, 64, 65, 91, 124, 129, 130, 134, 143, 147, 151, 163, 168, 176, 180, 193):
                continue
            if read_excel_cell(excel_path, sheet_name, "D"+str(i)) == folder and read_excel_cell(excel_path, sheet_name, "E"+str(i)) == file:
                new_folder = read_excel_cell(excel_path, sheet_name, "A"+str(i))
                break

        if new_folder == "":
            new_folder = folder

        if os.path.isfile("../" + new_folder + "/" + new_file):
            new_link = "../" + new_folder + "/" + new_file
            if german and new_link != "..//":
                new_link = remove_last_three_characters(new_link)
                new_link = new_link + ".de.md"
            return new_link     
        
        for i in range(2,215): 
            if i in (38, 44, 64, 65, 91, 124, 129, 130, 134, 143, 147, 151, 163, 168, 176, 180, 193):
                continue
            if read_excel_cell(excel_path, sheet_name, "A"+str(i)) == new_folder and read_excel_cell(excel_path, sheet_name, "B"+str(i)) == new_file:
                new_folder = read_excel_cell(excel_path, sheet_name, "D"+str(i))
                new_file = read_excel_cell(excel_path, sheet_name, "E"+str(i))
                break

        new_link = "../" + new_folder + "/" + new_file
        if german and new_link != "..//":
            new_link = remove_last_three_characters(new_link)
            new_link = new_link + ".de.md"
        return new_link     

#reads and returns the contents of an excel cell
def read_excel_cell(file_path, sheet_name, cell):

    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]

        cell_value = sheet[cell].value

        if isinstance(cell_value, str):
            return cell_value
        else:
            return None

    except openpyxl.exceptions.InvalidFileException as e:
        print(f"Error reading Excel file: {e}")
        return None   

#removes the last 3 characters of a string to get rid of the ".md" ending of a file
def remove_last_three_characters(input_string):

    if len(input_string) >= 3:
        return input_string[:-3]
    else:
        return input_string           

#removes the last 6 characters of a string to get rid of the ".de.md" ending of a file
def remove_last_six_characters(input_string):

    if len(input_string) >= 6:
        return input_string[:-6]
    else:
        return input_string          


base_directory = "sites/manual_user/docs"
original_directory = os.getcwd()
excel_path = '/Users/yves.meister/Handbuch Umstrukturierung/Neue_Struktur_nach_IA.xlsx'
sheet_name = 'Mappting'

with open("bin/faulty_links.txt", "w") as file:
    pass

search_for_faulty_links(base_directory)