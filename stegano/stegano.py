# This app will encode or decode text messages in an image file.
# The app will use RGB channels so only PNG files will be accepted.
# This technique will focus on Least Signifigant Bit (LSB) encoding.

from PIL import Image
import os
import sys

def encode(img, msg,imageName):
    # TODO: You need to convert the RGB to binary
    # Then we will adjust the pixels to encode the message binary value into the last bit.
    # Each letter will take three pixels, with a spare pixel unchanged.

    pixels = img.load()
    width, height = img.size
    letterSpot = 0
    pixel = 0
    letterBinary = ""
    msgLength = len(msg)
    red, green, blue = pixels[0, 0]
    secretName = imageName[:-4] + "_secret.png"
    pixels[0, 0] = (msgLength, green, blue)

    for i in range(msgLength * 3):
        x = i % width
        y = i // width

        red, green, blue = pixels[x, y]
        redBinary = numberToBinary(red)
        greenBinary = numberToBinary(green)
        blueBinary = numberToBinary(blue)

        if pixel % 3 == 0:
            letterBinary = numberToBinary(ord(msg[letterSpot]))
            # ignore the red  on the first pixel of each letter  ( 8 digit )
            greenBinary = greenBinary[0:7] + letterBinary[0]
            blueBinary = blueBinary[0:7] + letterBinary[1]
        elif pixel % 3 == 1:
            redBinary = redBinary[0:7] + letterBinary[2]
            greenBinary = greenBinary[0:7] + letterBinary[3]
            blueBinary = blueBinary[0:7] + letterBinary[4]
        else:
            redBinary = redBinary[0:7] + letterBinary[5]
            greenBinary = greenBinary[0:7] + letterBinary[6]
            blueBinary = blueBinary[0:7] + letterBinary[7]

            letterSpot += 1

        red = binaryToNumber(redBinary)
        blue = binaryToNumber(blueBinary)
        green = binaryToNumber(greenBinary)

        pixels[x, y] = (red, green, blue)
        pixel +=1
    # Save the file that has now been encoded.
    img.save(imageName[:-4] + "_secret.png", 'png')
    print("secret Image : ",imageName[:-4] + "_secret.png")


def decode(img):
    """Takes the image file and reads the least significant bit from the RGBA channels.
    Converts that binary to decimal to ASCII."""
    msg = ""

    pixels = img.load()  # Pixels is the pixel map, a 2-dimensional list of pixel data
    red, green, blue = pixels[0, 0]
    msgLength = red
    width, height = img.size
    letterSpot = 0
    pixel = 0
    letterBinary = ""
    x = 0
    y = 0
    while len(msg) < msgLength:
        red, green, blue = pixels[x, y]
        redBinary = numberToBinary(red)
        greenBinary = numberToBinary(green)
        blueBinary = numberToBinary(blue)

        if pixel % 3 == 0:
            letterBinary = greenBinary[7] + blueBinary[7]

        elif pixel % 3 == 1:
            letterBinary = letterBinary + redBinary[7] + greenBinary[7] + blueBinary[7]

        else:
            letterBinary = letterBinary + redBinary[7] + greenBinary[7] + blueBinary[7]
            letterAscii = binaryToNumber(letterBinary)
            letter = chr(letterAscii)
            msg = msg + chr(letterAscii)

        pixel = pixel + 1
        x = pixel % width
        y = pixel // width

    return msg


# Helper functions

def numberToBinary(num):
    """Takes a base10 number and converts to a binary string with 8 bits"""
    binary = ""
    # Convert from decimal to binary
    if num > 255 or num < 0:
        raise Exception("FUNCTION numberToBinary :  out of range  num is : %i", num)

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    while len(binary) < 8:
        binary = "0" + binary

    return binary


def binaryToNumber(bin):
    """Takes a string binary value and converts it to a base10 integer."""
    decimal = 0
    value = 1
    while len(bin) > 0:
        lastSpot = len(bin) - 1
        lastDigit = bin[lastSpot]
        if lastDigit == "1":
            decimal = decimal + value

        bin = bin[0:lastSpot]
        value = value * 2

    return decimal

def getPNG (fileList):
    result = []
    for file in fileList:
        if file[-4:] == ".png":
            result.append(file)
    return result

def main():
    # Ask user if they want to encode/decode

    message=""
    imageName = ""
    userOption =input ("Enter user input ( Encode or Decode or End) : ")

    if userOption == "Encode":
        cwd = os.getcwd()
        print("image available : ", getPNG(os.listdir(cwd)))
        imageName = input("Choose image to convert : " )
        message = input ("input your message : ")
        myImg = Image.open(imageName)
        encode(myImg, message,imageName)
        myImg.close()
        print ("Done!")

    elif userOption =="Decode":
        cwd = os.getcwd()
        print("image available : ", getPNG(os.listdir(cwd)))
        imageName = input("Choose image to convert : ")
        yourImg = Image.open(imageName)
        msg = decode(yourImg)
        print("decoded message : ",msg)
        print("Done!")

    elif userOption =="End":
        sys.exit()

    """
    myImg = Image.open('pki.png')
    myMsg = "This is a secret message I will hide in an image."
    encode(myImg, myMsg)
    myImg.close()

    userInput = input("Enter an option: Encode or Decode")

    
    for i in range(256):
        print( " decimal :  %i\t binary : %s" %(i, numberToBinary(i)))
        
    yourImg = Image.open('secretImg.png')
    msg = decode(yourImg)
    print(msg)
    """


if __name__ == '__main__':
    while(1):
        main()
