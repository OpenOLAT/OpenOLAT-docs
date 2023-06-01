import subprocess
import openpyxl
import os
import shutil

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
    
#searches through the .md file and finds all asset references. then produces a list of the asset file names and returns them
def search_for_assets(file_path):

    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.split('\n')

        occurrences = []
        asset_list = []

        for line in lines:
            if 'assets/' in line:
                occurrences.append(line)

        for element in occurrences:
            inside_brackets = False
            after_assets = False
            asset_name = ""
            for char in element:
                if char == "s" and not inside_brackets:
                    after_assets = True
                elif char == "/" and after_assets:
                    inside_brackets = True
                    after_assets = False
                elif char == ")" and inside_brackets:
                    inside_brackets = False
                    after_assets = False
                    break
                elif inside_brackets:
                    asset_name += char
                    after_assets = False
                else:
                    after_assets = False
                

            asset_list.append(asset_name)

        return asset_list
    
#iterates through a folder searching for  a specific file
def search_file(start_dir, target_file):

    for root, dirs, files in os.walk(start_dir):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            return file_path
    print(target_file+" File not found.")
    return None
    


file_path = '/Users/yves.meister/Handbuch Umstrukturierung/Neue_Struktur_nach_IA.xlsx'
sheet_name = 'Mappting'
missing_assets_list = []


for i in range(2,215):
    print("----------Current line: " + str(i))
    if i in range(31,36):
        continue
    if i in (44, 64, 65, 91, 124, 129, 130, 143, 147, 151, 163, 168, 176, 180, 193, 200):
        continue

    old_folder = read_excel_cell(file_path, sheet_name,'A'+str(i))

    if old_folder is None:
        continue

    old_file = read_excel_cell(file_path, sheet_name,'B'+str(i))
    new_folder = read_excel_cell(file_path, sheet_name,'D'+str(i))
    old_file_no_ending = remove_last_three_characters(old_file)
    old_file_german = old_file_no_ending + '.de.md'

    if os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file):
        en_assets = search_for_assets('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file)

        git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/'+old_file)

        for en_asset in en_assets.copy():
            if os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets/'+en_asset):
                en_assets.remove(en_asset)
                continue
            elif os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/assets/'+en_asset):
                git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/assets/'+en_asset, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets/'+en_asset)
                en_assets.remove(en_asset)
                continue
            else:
                file_location = search_file('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs',en_asset)
                if file_location != None:
                    shutil.copy(file_location, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets')
                    en_assets.remove(en_asset)
                    continue
            missing_assets_list.append('ASSET: '+en_asset+' is missing from FILE: '+old_file)


    if os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file_german):
        de_assets = search_for_assets('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file_german)

        git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/'+old_file_german, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/'+old_file_german)

        for de_asset in de_assets.copy():
            if os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets/'+de_asset):
                de_assets.remove(de_asset)
                continue
            elif os.path.isfile('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/assets/'+de_asset):
                git_mv('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+old_folder+'/assets/'+de_asset, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets/'+de_asset)
                de_assets.remove(de_asset)
                continue
            else:
                file_location = search_file('/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs',de_asset)
                if file_location != None:
                    shutil.copy(file_location, '/Users/yves.meister/OpenOLAT-docs/sites/manual_user/docs/'+new_folder+'/assets')
                    de_assets.remove(de_asset)
                    continue
            missing_assets_list.append('ASSET: '+de_asset+' is missing from FILE: '+old_file_german)

print('------MOVEMENTS COMPLETE------')
print('Following files are missing: ')
print(missing_assets_list)

            


    
    

    

    

