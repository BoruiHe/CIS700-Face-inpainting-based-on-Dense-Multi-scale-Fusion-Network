import random


train_ls = open(r'C:\Users\hbrch\Desktop\CIS700\CelebA_txt\train.txt', 'rt').read().splitlines()
test_ls = []
while len(test_ls)<2000 :
    L = random.randint(1,202599)
    L = str(L).zfill(6)+'.jpg'
    if L not in train_ls:
        test_ls.append(L)
        print(L, len(test_ls))

textfile = open(r'C:\Users\hbrch\Desktop\CIS700\CelebA_txt\mytest.txt', "w")
for element in test_ls:
    if element == test_ls[-1]:
        textfile.write(element)
    else:
        textfile.write(element + '\n')
textfile.close()