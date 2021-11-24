import math

def kombinacijas(cik, no_cik):

    comb = (math.comb(cik, no_cik))
    print("tas ir combinacija skaitla", comb)



def klasiska(cik, no_cik):
    klasika = cik/no_cik
    procent2 = klasika*100
    if klasika > 1 or klasika < 0 :
        print("\033[91mError Avakadu")
    print("\033[1;97mvarbūtība ir = " + format(procent2, ",.2f") + '%')
    return klasika


def value_input():
    cik = int(input("\033[93mEnter first number:"))
    no_cik = int(input("Enter second number:"))
    cik1 = int(input("\033[92mEnter again first number:"))
    no_cik2 = int(input("Enter again second number:"))
    p1 = klasiska(cik, no_cik)
    p2 = klasiska(cik1, no_cik2)

    if p1 > p2:
        print("Pirmaja varbutiba ir veiksmigaks "+ str(cik) + " no " + str(no_cik))
        kombinacijas(cik,no_cik)
    else:
        print("Otraja varbutiba ir veiksmigaks " + str(cik1) + " no " + str(no_cik2))
        kombinacijas(cik1,no_cik2)




if __name__ == '__main__':
    while True:
       value_input()
       restart = input('do you want again?').lower()
       if restart == "yes":
           value_input()