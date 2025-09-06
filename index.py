import os

# 1 - Acessa diretório raiz  do SO
base_path = os.path.expanduser('~')
print(base_path)

# 2 - Navega no diretório downloads
path = os.path.join(base_path, 'Downloads')
print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos do diretório
list_files = os.listdir(work_dir)
print(list_files)

# 4 - Organizando os arquivos e criando pastas
type_files = ['exe', 'csv', 'jpg', 'pdf', 'zip', 'txt', 'py', 'xlsx', 'png', 'jpeg', 'mp4', 'mp3', 'm4a']
for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - Organizando os arquivos
for file in list_files:
    for type in type_files:
        if '.' + type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)
            print(f'Arquivo {file} movido com sucesso!')