import os
import getpass
import folder_system  
def main():
    
    USER = getpass.getuser()
    PATH = '/home/{}/Descargas'.format(USER)
    os.chdir(PATH)
    downloads_container = os.listdir()
    folder_system.create_folders(PATH)





if __name__ == "__main__":
    main()