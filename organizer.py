import os
import shutil

def organize(path, folders):
    EXTENSIONS = {'AUDIOVISUAL':['jpg', 'png', 'mp4', 'mp3', 'jpeg', 'raw'], 'TEXT':['doc', 'odt', 'pdf', 'ppt', 'txt'], 'COMPRESSED_FOLDER': ['zip', 'rar', '7z'], 'CODE': ['py', 'c', 'cpp', 'html', 'css', 'pyw', 'cs', 'js', 'php']}
    os.chdir(path)
    path_container = os.listdir()

    for i in range(len(path_container)):
        
        if not(path_container[i] in folders):

            try:
                file_extension = path_container[i].split('.')[1]

                if file_extension in EXTENSIONS['AUDIOVISUAL']:
                    shutil.move(path_container[i], './AUDIOVISUAL')

                elif file_extension in EXTENSIONS['TEXT']:
                    shutil.move(path_container[i], './TEXT')

                elif file_extension in EXTENSIONS['COMPRESSED_FOLDER']:
                    shutil.move(path_container[i], './COMPRESSED_FOLDER')

                elif file_extension in EXTENSIONS['CODE']:
                    shutil.move(path_container[i], './CODE')

                else:
                    shutil.move(path_container[i], './OTHER')

                
            except:
                shutil.move(path_container[i], './COMPRESSED_FOLDER')    



        