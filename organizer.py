import os
import shutil


def move_files(original_name, new_name, to_move, counter):
    if not(new_name in os.listdir(to_move)):
        os.rename(original_name, new_name)
        print('Moviendo', new_name, 'a', to_move)
        shutil.move(new_name, to_move)
    
    else:
        n_name = '({})'.format(counter) + original_name
        print(n_name)
        move_files(original_name, n_name, to_move, counter+1)        


def organize(path, folders):
    EXTENSIONS = {'AUDIOVISUAL':['jpg', 'png', 'mp4', 'mp3', 'jpeg', 'raw'], 'TEXT':['doc', 'odt', 'pdf', 'ppt', 'txt'], 'COMPRESSED_FOLDER': ['zip', 'rar', '7z'], 'CODE': ['py', 'c', 'cpp', 'html', 'css', 'pyw', 'cs', 'js', 'php']}
    os.chdir(path)
    path_container = os.listdir()

    for i in range(len(path_container)):
        
        if not(path_container[i] in folders):

            try:
                file_extension = path_container[i].split('.')[1]

                if file_extension in EXTENSIONS['AUDIOVISUAL']:
                    move_files(path_container[i], path_container[i], './AUDIOVISUAL', 1)


                elif file_extension in EXTENSIONS['TEXT']:
                    move_files(path_container[i], path_container[i], './TEXT', 1)

                
                elif file_extension in EXTENSIONS['COMPRESSED_FOLDER']:
                    move_files(path_container[i], path_container[i], './COMPRESSED_FOLDER', 1)

                
                elif file_extension in EXTENSIONS['CODE']:
                    move_files(path_container[i], path_container[i], './CODE', 1)

                
                else:
                    move_files(path_container[i], path_container[i], './OTHER', 1)

                
            except:
                #shutil.move(path_container[i], './COMPRESSED_FOLDER')    
                pass


        