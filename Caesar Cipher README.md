# 凯撒密码的加密和解密
## 小组成员
国彧 2246324060 负责程序编写
钱龙洁 2244323722 负责说明文件编写
## 程序流程图
flowchart TD
    Start[开始] --> InputMode[输入模式选择]
    InputMode --> CheckMode{模式检查}
    CheckMode -- A --> Encrypt[加密流程]
    CheckMode -- B --> Decrypt[解密流程]
    CheckMode -- 无效 --> ReInputMode[重新输入模式]

    Encrypt --> InputKey[输入密钥]
    Decrypt --> InputKey
    InputKey --> ValidateKey{密钥验证}
    ValidateKey -- 有效 --> Process[处理文本]
    ValidateKey -- 无效 --> ReInputKey[重新输入密钥]

    Process --> EncryptFunc[调用加密函数]:::encrypt
    Process --> DecryptFunc[调用解密函数]:::decrypt

    subgraph 加解密核心算法
        EncryptFunc --> LoopText[遍历每个字符]
        DecryptFunc --> LoopText
        LoopText --> CheckCase{字符类型判断}
        CheckCase -- 大写 --> CalcUpper[计算大写偏移]
        CheckCase -- 小写 --> CalcLower[计算小写偏移]
        CheckCase -- 其他 --> KeepOriginal[保留原字符]
        CalcUpper --> StoreResult[存储结果]
        CalcLower --> StoreResult
        KeepOriginal --> StoreResult
    end

    StoreResult --> Output[输出结果]
    Output --> End[结束]

    classDef encrypt fill:#c1e1c1,stroke:#4da64d;
    classDef decrypt fill:#c6d9f1,stroke:#4d79ff;
## 程序编写
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
## 程序说明
我们在这次的程序编写中主要运用了函数的定义、if条件语句、while循环三个知识点，通过定义Encryption、Decryption两个函数实现加密和解密函数的调用，使用if条件语句完成大小写字母的分别加密和解密和调用函数的选择，使用while循环判断输入字符是否合规。同时，我们调用了函数ord()和chr()实现ASCII码转换。
## 程序运行实例
【凯撒密码的加密-哔哩哔哩】 https://b23.tv/SGxe0zh
【凯撒密码的解密-哔哩哔哩】 https://b23.tv/XQXrVve