# SECRET CODE LANGUAGE

import random
import string


print("1. Code")
print("2. Decode")
choice = int(input("Choose one from the above: "))

if choice == 1:
    word = input("Enter the word you want to code: ")
    s1 = random.choice(string.ascii_lowercase)
    s2 = random.choice(string.ascii_lowercase)
    s3 = random.choice(string.ascii_lowercase)
    s_1 = s1 + s2 + s3
    s4 = random.choice(string.ascii_lowercase)
    s5 = random.choice(string.ascii_lowercase)
    s6 = random.choice(string.ascii_lowercase)
    s_2 = s4+s5+s6
    split_word = word.split()
    list1 = []
    for i in split_word:
        if len(i) <= 3:
            i = i[::-1]
            print(i)
            list1.append(i)
            
        else:
            j = str(i[0])
            k = i.replace(j, "", 1)
            coded_word = s_1 + k + s_2
            list1.append(coded_word)
        codeword = ' '.join(map(str,list1))
        print(codeword)


elif choice == 2:
    word = input("Enter the word you want to code: ")
    split_word = word.split()
    list1 = []
    for i in split_word:
        if len(i) <= 3:
            code = i[::-1]
            list1.append(code)
        else:
            j1 = i[0:3]
            j2 = i[-3:]
            i = i.replace(j1, "").replace(j2, "")
            i = i[::-1]
            list1.append(i)
    decodeword = ' '.join(list1)
    print(decodeword)
        
else:
    print("Enter correct choice...")