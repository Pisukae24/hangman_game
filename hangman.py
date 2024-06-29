import random
word=["samridhi","khushi","cheeku"]
lives=6
word_selected = random.choice(word)
# print (word_selected)
display=[]
for i in word_selected :#range (len(word_selected))
    display+='_'
print (display)
game_over=False
while not game_over:
        guessed_letter=input("guess a letter").lower()
        for position in range(len(word_selected)):
            letter = word_selected[position]
            if letter == guessed_letter :
                display[position]=guessed_letter
        print(display)
        if guessed_letter not in word_selected :
             lives-=1
             if lives==0:
                 game_over=True
                 print("you lose")
        if'_' not in display:
            guessed_letter =True
            print("you win")