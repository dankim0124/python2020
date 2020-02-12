# BasicEnigma.py
# Name: dohyun kim
# Date: 2020 02 12
# Assignment: basic enigma

# This is a simplified version of the German Enigma used during WWII.

def translate(startLetters, endLetters, spot):
    # find the letter at (spot) in the startLetters string.
    # find the location of the letter in the endLetters string.
    letter = startLetters[spot]
    spot = endLetters.find(letter)
    return spot


def rotate(alphabet):
    # move the first letter of the alphabet to the end
    # shift all the letters
    alphabet = alphabet[1:] + alphabet[0]
    return alphabet  # this has been rotated


def main():
    alpha =      "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor1 =     "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 =     "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 =     "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"
    count = 0

    # get a message from the user

    message = "ODWFQEFUMKROXTNVCQUMTRFTLYZEUFURLRFOXGPICTUMHRTYNJFTZ"
    letter = message[0]
    secret = ""
    message = message.upper()

    for letter in message:
        # Find location of letter in alphabet
        pos = alpha.find(letter)
        if pos >=0:
            pos = translate(alpha, rotor1, pos)  # starting, ending, current position
            pos = translate(alpha, rotor2, pos)
            pos = translate(alpha, rotor3, pos)

            pos = translate(alpha, reflectorA, pos)

            pos = translate(rotor3, alpha, pos)
            pos = translate(rotor2, alpha, pos)
            pos = translate(rotor1, alpha, pos)
            # Translate back from position to a letter
            letter = alpha[pos]
            # Now that we have been through one pass, adjust any of the rotors that need to be rotated.

            rotor1 = rotate(rotor1)
            count = count+1
            if (count %26 ==0):
                rotor2 = rotate(rotor2)
            secret +=letter

    print(secret)  # This one letter has been encoded


main()