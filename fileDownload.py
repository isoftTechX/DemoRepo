from urllib.request import urlretrieve
import getpass

# url = 'https://drive.google.com/uc?export=download&id=1IKmJGxZLgDSGEHynEGHBuZvQPRXhnbJJ'
url = 'https://docs.google.com/u/0/uc?export=download&confirm=0jGe&id=1IKmJGxZLgDSGEHynEGHBuZvQPRXhnbJJ'

print('File Downloading')

usrname = getpass.getuser()
# destination = f'C:\\Users\\{usrname}\\Downloads\\download.png'
destination = 'mainiTech.py'

download = urlretrieve(url, destination)

print('File Downloaded')


# import os

# print('File name : ', os.path.basename(__file__))
# dirName = os.path.dirname(__file__).replace('\\', '/')
# print('Directory Name:	 ', f"{dirName}/")