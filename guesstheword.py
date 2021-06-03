import random
name=input("Hello, What's your name?")
print("Oh hey "+name+",Lets play word guessing.")
rule= input("To display the rules enter 1 else enter 0 ")
if rule=='1':
    print("Rules:")
    print("You have 8 points at the start. I will think of a word. You have to guess the letters that might be in that word.")
    print("If you guess it correctly, I will display the letter. If you guess it incorrectly, you lose a point.")
    print("If you are able to guess all the letters in the word, you win. But if you can’t figure it out in time, you lose.")
print("Let's start the game:")

def letfound(let,found,pos):
    print(let + " letter found")
    found.append(let)


def letnotfound(guess,missing):
    print(guess + " letter not found")
    missing.append(guess)


def playhangman(list,totalg):
    secret=list[word]
    #print(secret)
    dash=len(secret)*'_ '
    print("Word length - "+str(len(secret)))
    print("The word is- "+dash)

    found=[]
    missing=[]
    while totalg>0:
        pos=1
        guess=input("Guess a letter").lower()


        boo=False
        if guess in found or guess in missing:
            print("You have already guessed this letter")
            boo=True
        else:
            for let in secret:
            #print(let)

                if let==guess:
                    letfound(let,found,pos)
                    boo=True

                #print(pos)
                pos=pos+1

        if boo==False:
            letnotfound(guess,missing)
            totalg=totalg-1

            if totalg==0:
                print("You lose the game. The word was " + secret)
                break
            print("Point deducted. You have " +str(totalg)+ " points left")

        print(''.join('_ ' if l not in found else l for l in secret))
        #print(*found)
        if len(found)==len(secret):
            print("Congratulations, You have deciphered the word "+ secret)
            break
        #print(*missing)


again='y'

while again=='y':
    list='aeroplane scrabble dictionary watermelon refridgerator television laptop baboon badger beaver coyote ferret lizard parrot engagement matrimony balling peekaboo massacre certificate adventure showdown nostalgia hunting travellers couples fairyland princess toothbrush spaceship helicopter pirates beaches mountains vampires doodles orangutan cockroach'.split()
    word=random.randint(1,len(list)-1)
    totalg=8
    playhangman(list,totalg)
    again=input("Do you want to play again? y/n?").lower()

print("Thanks for playing. Code- Rashi Agarwal")
