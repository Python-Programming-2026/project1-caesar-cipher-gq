#此函数为明文加密函数
def Encryption(text,key):
    result=''
    for char in text:#遍历输入的字符
        #判断并加密大写字母
        if char.isupper():
            result+=chr((ord(char)-ord('A')+key)%26+ord('A'))
        #判断并加密小写字母
        elif char.islower():
            result+=chr((ord(char)-ord('a')+key)%26+ord('a'))
        #其余字符例如数字符号等保持不变
        else:
            result+=char
    return result#返回加密后的密文

#此函数为密文解密函数
def Decryption(text,key):
    result=''
    for char in text:#遍历输入的字符
        #判断并解密大写字母
        if char.isupper():
            result+=chr((ord(char)-ord('A')-key)%26+ord('A'))
        #判断并解密小写字母
        elif char.islower():
            result+=chr((ord(char)-ord('a')-key)%26+ord('a'))
        #其余字符保持不变
        else:
            result+=char
    return result#返回解密后的明文

user=input('明文加密请按A，密文解密请按B:')
#判断输入是否符合要求
while(user!='A' and user!='B'):
    user=input('请重新输入：')
key=int(input('请输入密钥:'))#字母偏移量
#判断输入密钥的偏移量是否符合要求
while(key<=0 or key>=26):
    key=input('请重新输入密钥:')
#获取明文
if user=='A':
    plaintext=input('请输入明文:')
    Ciphertext=Encryption(plaintext,key)
    print(f'\n密文为:{Ciphertext}')
#获取密文
else:
    ciphertext=input('请输入密文:')
    Plaintext=Decryption(ciphertext,key)
    print(f'\n明文为:{Plaintext}')