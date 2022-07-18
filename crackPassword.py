import hashlib

flag = 0

pass_hash = input('Enter md5: ')
common_pass = input('File name: ')

try:
    pass_file_name = open(common_pass , "r")
except:
    print('No file found')
    quit()

for word in pass_file_name:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print('Password Found is ' + word)
        flag = 1
        break
    else:
        print('Password not found in list')
        



