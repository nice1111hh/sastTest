# import pandas as pd
import os
import shutil

# df_old = pd.read_excel('old_file.xlsx')

# df_new = pd.read_excel('new_file.xlsx')

# df_diff = pd.concat([df_old,df_new]).drop_duplicates(keep=False)

# list_of_new_urls = df_diff['URLs'].to_list()

# for repo_url in list_of_new_urls:
#     print(repo_url) 
#     command_to_run = 'git clone ' + repo_url

#     # print(command_to_run)
#     os.system(command_to_run)

with open('old_file.txt', 'r') as file1:
    with open('new_file.txt', 'r') as file2:
        same = set(file2).difference(file1)

same.discard('\n')

# with open('some_output_file.txt', 'w') as file_out:
#     for line in same:
#         file_out.write(line)

for line in same:
    print(line)
    command_to_run = 'git clone ' + line
    # os.system(command_to_run)
    os.remove("old_file.txt")
    os.rename('new_file.txt', 'old_file.txt')
    shutil.copy('new_file.txt', 'old_file.txt')
    