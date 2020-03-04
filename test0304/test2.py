#Midterm Exam
#Problem2.py
#Name: dohyun kim
#Date: 0304



def check_str ( param):

    A = ["a","A"]
    E = ["e","E"]
    I = ["i", "I"]
    O = ["o","O"]
    U = ["u","U"]

    result ={"A":0,"E":0,"I":0,"O":0,"U":0}
    for elem in param:
        if elem in A:
            result["A"] =result["A"] +1
        if elem in E:
            result["E"] = result["E"] + 1
        if elem in I:
            result["I"] = result["I"] + 1
        if elem in A:
            result["O"] = result["O"] + 1
        if elem in U:
            result["U"] = result["U"] + 1

    return result
my_input = input ("Enter a sentence: ")
result = check_str(my_input)
for key in result.keys():
    print ( key, ": ", result[key])