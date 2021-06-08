word= 'kiss'

life= 10

print("HI! welcome to the game hangman\n")
print("guess the word!!\n")
pr_word=''
for i in word:
    pr_word=pr_word + '_ '
print(pr_word)
flag=[]
content= []
for i in word:
    content.append('_')
for i in range(0,len(word)):
    flag.append(False)
while life > 0:
    token = False
    chara_guess = input("guess a character") 
    for i in range(0,len(word)):
        if word[i]==chara_guess:
            flag[i]=True
            token=True
        
    for i in range(0,len(flag)):
        if flag[i] == True:
            print(f'{word[i]}\t')
            content[i]= word[i]
        else:
            print("_\t")
    cont = ''.join(content)
    if cont == word:
        print(f'you won and {life-1} is left')
        break
    if token == False:
        print(f'Character not present , now you have only {life-1}\n')
    else: 
        print(f'yohoo! you got it right, keep it up! Now you have to find more ')

    life = life - 1
    if life == 0:
        print("you lose, better luck next time:")


    



