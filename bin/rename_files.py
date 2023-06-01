import subprocess
import openpyxl
import os

#uses "git mv" to move a file from one location to another
def git_mv(source_path, destination_path):

    try:
        subprocess.run(['git', 'mv', source_path, destination_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error moving '{source_path}' to '{destination_path}': {e}")

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
    
file_path = '/Users/yves.meister/Handbuch Umstrukturierung/Neue_Struktur_nach_IA.xlsx'
sheet_name = 'Mappting'
    
for i in range(2,215):
    print("----------Current line: " + str(i))
    if i in range(31,36):
        continue
    if i in (44, 64, 65, 91, 124, 129, 130, 143, 147, 151, 163, 168, 176, 180, 193, 200):
        continue
        
    folder = read_excel_cell(file_path, sheet_name,'A'+str(i))

    if i == 175:
        folder = folder[1:]

    if folder is None:
        continue

    old_file = read_excel_cell(file_path, sheet_name,'B'+str(i))
    new_file = read_excel_cell(file_path, sheet_name,'E'+str(i))
    old_file_no_ending = remove_last_three_characters(old_file)
    old_file_german = old_file_no_ending + '.de.md'
    new_file_no_ending = remove_last_three_characters(new_file)
    new_file_german = new_file_no_ending + '.de.md'

    if old_file != new_file:
        git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+folder+'/'+old_file, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+folder+'/'+new_file)
        git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+folder+'/'+old_file_german, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+folder+'/'+new_file_german)

print('------RENAMING COMPLETE------')