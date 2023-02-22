import zipfile
import subprocess

#
# command01 = [r'C:\Program Files\7-Zip\7z.exe', "x", "-ppassword", "tmp.zip"]
# subprocess.call(command01)

count = 1

zip_file = zipfile.ZipFile('test2.zip')

# read password list file
# passwords = [line.strip() for line in open('rockyou.txt')]
passwords = [line.strip() for line in open('darkweb2017-top10000.txt')]

for password in passwords:
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f'Successful: Password is {password}')
        break
    except:
        number = count
        print('[%s] [-] Password failed! - %s' % (number,password))
        count += 1
        pass
