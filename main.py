import os
import getpass
import folder_system 
import shutil
import organizer 
def main():
    
    USER = getpass.getuser()
    PATH = '/home/{}/Descargas'.format(USER)
    folder_system.create_folders(PATH)
    organizer.organize(PATH, ['AUDIOVISUAL', 'TEXT', 'COMPRESSED_FOLDERS', 'CODE', 'OTHER'])





if __name__ == "__main__":
    main()