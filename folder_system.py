import os


def create_folders(path):
    FOLDER_TYPES = ['AUDIOVISUAL', 'TEXT', 'COMPRESSED_FOLDERS', 'CODE', 'OTHER']
    os.chdir(path)
    path_container = os.listdir()

    for i in range(len(FOLDER_TYPES)):
        if not (FOLDER_TYPES[i] in path_container):
            os.mkdir(path + '/{}'.format(FOLDER_TYPES[i]))

    