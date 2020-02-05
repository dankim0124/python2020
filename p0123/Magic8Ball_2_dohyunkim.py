#Magic8Ball.py
#Name: dohyun kim
#Date: 2020-01-22
#Assignment: assignment #2

#We will need random for this program, import to use this package.
import random

def main():
    answers = ["yes", "no"]
    response = random.choice(answers)
    print(response)

    responses = ["padding:0=>random",
"as I see it, yes.",
"ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don’t count on it.",
"It is certain.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Outlook good.",
"Reply hazy, try again.",
"Signs point to yes.",
"Very doubtful.",
"Without a doubt.",
"Yes.",
"Yes – definitely.",
"You may rely on it"]

    myInput = int(input("input number (0~"+ str(len(responses)) +"): "))

    if( myInput == 0 ):
       print(random.choice(responses))

    else:
       print(responses[myInput])

  #Create a list of your responses.

  #Prompt the user for their question.

  # Answer question randomly with one of the options from your earlier list.


main()