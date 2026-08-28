
import time
import random

def Spacer():
    print("")
def SpacerB():
    print("___________")
def SpacerSS():
    print("")
    print("")
def SpacerSSS():
    print("")
    print("")
    print("")
def SpacerBS():
    print("___________")
    print("")
def DnaReader():
    T = "T"
    A = "A"
    G = "G"
    C = "C"
    U = "U"
    Z = "Z"
    Q = "Q"
    num_letter = 0
    place = 0
    Spacer()
    code = input("'INPUT' Enter DNA Strand - ")
    code = code.replace(A, Q)
    code = code.replace(T, A)
    code = code.replace(G, Z)
    code = code.replace(U, A)
    code = code.replace(C, G)
    code = code.replace(Z, C)
    code = code.replace(Q, U)
    print("mRNA Strand - ", code)
    for letter in code:
            num_letter = num_letter + 1
            if num_letter == 3:
                print(code[place:place + 3])
                if "AUU" in (code[place:place + 3]):
                    print("Amino Acid - Ile")
                    print("____________________")
                if "AUC" in (code[place:place + 3]):
                    print("Amino Acid - Ile")
                    print("____________________")
                if "AUA" in (code[place:place + 3]):
                    print("Amino Acid - Ile")
                    print("____________________")
                if "AUG" in (code[place:place + 3]):
                    print("Amino Acid - Start Codon")
                    print("____________________")
                if "ACU" in (code[place:place + 3]):
                    print("Amino Acid - Thr")
                    print("____________________")
                if "ACC" in (code[place:place + 3]):
                    print("Amino Acid - Thr")
                    print("____________________")
                if "ACA" in (code[place:place + 3]):
                    print("Amino Acid - Thr")
                    print("____________________")
                if "ACG" in (code[place:place + 3]):
                    print("Amino Acid - Thr")
                    print("____________________")
                if "AAC" in (code[place:place + 3]):
                    print("Amino Acid - Ansa")
                    print("____________________")
                if "AAU" in (code[place:place + 3]):
                    print("Amino Acid - Ansa")
                    print("____________________")
                if "AAA" in (code[place:place + 3]):
                    print("Amino Acid - Lys")
                    print("____________________")
                if "AAG" in (code[place:place + 3]):
                    print("Amino Acid - Lys")
                    print("____________________")
                if "AGC" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "AGU" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "AGA" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                if "AGG" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                if "GUU" in (code[place:place + 3]):
                    print("Amino Acid - Val")
                    print("____________________")
                if "GUA" in (code[place:place + 3]):
                    print("Amino Acid - Val")
                    print("____________________")
                if "GUC" in (code[place:place + 3]):
                    print("Amino Acid - Val")
                    print("____________________")
                if "GUG" in (code[place:place + 3]):
                    print("Amino Acid - Val")
                    print("____________________")
                if "GCA" in (code[place:place + 3]):
                    print("Amino Acid - Ala")
                    print("____________________")
                if "GCU" in (code[place:place + 3]):
                    print("Amino Acid - Ala")
                    print("____________________")
                if "GCG" in (code[place:place + 3]):
                    print("Amino Acid - Ala")
                    print("____________________")
                if "GCC" in (code[place:place + 3]):
                    print("Amino Acid - Ala")
                    print("____________________")
                if "GAG" in (code[place:place + 3]):
                    print("Amino Acid - Glu")
                    print("____________________")
                if "GAA" in (code[place:place + 3]):
                    print("Amino Acid - Glu")
                    print("____________________")
                if "GAC" in (code[place:place + 3]):
                    print("Amino Acid - Asp")
                    print("____________________")
                if "GAU" in (code[place:place + 3]):
                    print("Amino Acid - Asp")
                    print("____________________")
                if "GGG" in (code[place:place + 3]):
                    print("Amino Acid - Gly")
                    print("____________________")
                if "GGC" in (code[place:place + 3]):
                    print("Amino Acid - Gly")
                    print("____________________")
                if "GGA" in (code[place:place + 3]):
                    print("Amino Acid - Gly")
                    print("____________________")
                if "GGU" in (code[place:place + 3]):
                    print("Amino Acid - Gly")
                    print("____________________")
                if "UUG" in (code[place:place + 3]):
                    print("Amino Acid - Leu")
                    print("____________________")
                if "UUA" in (code[place:place + 3]):
                    print("Amino Acid - leu")
                    print("____________________")
                if "UUC" in (code[place:place + 3]):
                    print("Amino Acid - Phe")
                    print("____________________")
                if "UUU" in (code[place:place + 3]):
                    print("Amino Acid - Phe")
                    print("____________________")
                if "UCC" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "UCG" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "UCA" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "UCU" in (code[place:place + 3]):
                    print("Amino Acid - Ser")
                    print("____________________")
                if "UAU" in (code[place:place + 3]):
                    print("Amino Acid - Tyr")
                    print("____________________")
                if "UAC" in (code[place:place + 3]):
                    print("Amino Acid - Tyr")
                    print("____________________")
                if "UAA" in (code[place:place + 3]):
                    print("Amino Acid - Stop Codon")
                    print("____________________")
                if "UAG" in (code[place:place + 3]):
                    print("Amino Acid - Stop Codon")
                    print("____________________")
                if "UGU" in (code[place:place + 3]):
                    print("Amino Acid - Cys")
                    print("____________________")
                if "UGC" in (code[place:place + 3]):
                    print("Amino Acid - Cys")
                    print("____________________")
                if "UGA" in (code[place:place + 3]):
                    print("Amino Acid - Stop Codon")
                    print("____________________")
                if "UGG" in (code[place:place + 3]):
                    print("Amino Acid - Trp")
                    print("____________________")
                if "CUC" in (code[place:place + 3]):
                    print("Amino Acid - Leu")
                    print("____________________")
                if "CUG" in (code[place:place + 3]):
                    print("Amino Acid - Leu")
                    print("____________________")
                if "CUU" in (code[place:place + 3]):
                    print("Amino Acid - Leu")
                    print("____________________")
                if "CUA" in (code[place:place + 3]):
                    print("Amino Acid - Leu")
                    print("____________________")
                if "CCG" in (code[place:place + 3]):
                    print("Amino Acid - pro")
                    print("____________________")
                if "CCC" in (code[place:place + 3]):
                    print("Amino Acid - pro")
                    print("____________________")
                if "CCU" in (code[place:place + 3]):
                    print("Amino Acid - Pro")
                    print("____________________")
                if "CCA" in (code[place:place + 3]):
                    print("Amino Acid - Pro")
                    print("____________________")
                if "CAA" in (code[place:place + 3]):
                    print("Amino Acid - Gin")
                    print("____________________")
                if "CAG" in (code[place:place + 3]):
                    print("Amino Acid - Gin")
                    print("____________________")
                if "CAC" in (code[place:place + 3]):
                    print("Amino Acid - His")
                    print("____________________")
                if "CAU" in (code[place:place + 3]):
                    print("Amino Acid - His")
                    print("____________________")
                if "CGC" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                if "CGU" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                if "CGA" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                if "CGG" in (code[place:place + 3]):
                    print("Amino Acid - Arg")
                    print("____________________")
                place = place + 3
                num_letter = 0
    else:
        SpacerSS()
        Rebound = int(input("'INPUT' Type '1' to be returned back to the HOMEPAGE, Type '2' to go back to DNA Reader - "))
        if Rebound == 1:
            print("Sending You back to the HOMEPAGE")
            time.sleep(1)
            print("Connecting...")
            HOMEPAGE()
        if Rebound == 2:
            print("Sending You back to the Dna Reader")
            time.sleep(1)
            print("Connecting...")
            DnaReader()
        else:
            print("Connection throttled...")
            print("Please type correctly next time")
            time.sleep(2)
            HOMEPAGE()
def Blackjack():
    print("Hello!")
    Spacer()
    print("Im H.L.N.A, your dealer.")
    SpacerBS()
    time.sleep(2)
    print("Let me explain the rules..")
    Spacer()
    time.sleep(1)
    print(" - Only type when it says 'INPUT'")
    print(" - Or else the code will break and you will be put back to the HOMEPAGE")
    Spacer()
    time.sleep(1)
    print(" - Type 'H' to hit and 'S' to stand")
    Spacer()
    time.sleep(1)
    print(" - Lastly, last time I checked you needed money to play BlackJack, am I wrong?")
    print("Money")
def HLNAHOMEPAGE_help():
    time.sleep(1)
    SpacerB()
    print("Hello, Im H.L.N.A, an assistant built for the HOMEPAGE")
    time.sleep(1)
    print("Im here to help with any concerns!")
    time.sleep(1)
    print("So What seems to be the problem?")
    print(" - System error? (Type 1)")
    print(" - Code is not working right? (Type 2)")
    print(" - Unable to understand something? (Type 3)")
    print(" - If these are not the problems at hand, then please notify Blaine.")
    time.sleep(1)
    print("How to notify me - ")
    print(" - Email")
    print(" - In person")
    Choice_help = input("'INPUT' Type here - ")
    if "1" in Choice_help.lower():
        SpacerB()
        print("Please notify Blaine:")
        Spacer()
        print(" - Where the crash is")
        print(" - When it happens")
        print("Thank you for using H.L.N.A, and enjoy the HOMEPAGE")
        SpacerSS()
        Rebound = int(input("'INPUT' Type '1' to be returned back to the HOMEPAGE - "))
        if Rebound == 1:
            print("Sending You back to the HOMEPAGE")
            time.sleep(1)
            print("Connecting...")
            HOMEPAGE()
        else:
            print("Connection throttled...")
            print("Please type correctly next time")
            time.sleep(2)
            HOMEPAGE()
    if "2" in Choice_help.lower():
        SpacerB()
        print("What part of the code is not functional?")
        print(" - The 'Dna Reader'")
        print(" - 'Blackjack'")
        print(" - The HOMEPAGE")
        if "dna" or "dnareader" or "bio" or "black" or "jack" or "blackjack" or "hompage" in Choice_help.lower():
            print("Please notify Blaine somehow and I will fix the problem in the future Patch notes.")
            Spacer()
            print("If the code is still broken, please click 'Run' at the top of your screen again, and soft reset the HOMEPAGE")
            Spacer()
            print("Thank you for using H.L.N.A, and enjoy the HOMEPAGE")
            SpacerSS()
            Rebound = int(input("'INPUT' Type '1' to be returned back to the HOMEPAGE - "))
            if Rebound == 1:
                print("Sending You back to the HOMEPAGE")
                time.sleep(1)
                print("Connecting...")
                HOMEPAGE()
            else:
                print("Connection throttled...")
                print("Please type correctly next time")
                time.sleep(2)
                HOMEPAGE()
    if "3" in Choice_help.lower():
        SpacerB()
        print("Please notify me what parts are confusing.")
        SpacerSS()
        Rebound = int(input("'INPUT' Type '1' to be returned back to the HOMEPAGE - "))
        if Rebound == 1:
            print("Sending You back to the HOMEPAGE")
            time.sleep(1)
            print("Connecting...")
            HOMEPAGE()
        else:
            print("Connection throttled...")
            print("Please type correctly next time")
            time.sleep(2)
            HOMEPAGE()
    else:
        print("Sorry, Please use the desired numbers to locate the problem.")
        print("reclocating you back to H.L.N.A help...")
        time.sleep(2)
        HLNAHOMEPAGE_help()
def HOMEPAGE():
    time.sleep(2)
    SpacerSSS()
    SpacerSSS()
    print("WELCOME TO THE HOMEPAGE")
    Spacer()
    print("HOMEPAGE Patch Notes 1.0.1")
    print(" - Added H.L.N.A, an assitant Built for the HOMEPAGE")
    print(" - Working on New 'BlackJack' game (Estimated patch notes: 1.1.0)")
    Spacer()
    Spacer()
    print("Here is What is on HOMEPAGE currently:")
    SpacerB()
    print("- H.L.N.A Help - H.L.N.A is the HOMEPAGE's built in assistant to help with any concerns (Type 'Help')")
    Spacer()
    print("- Bio Dna Translator - Translate DNA Strands into mRNA and Amino Acids (Type 'Dna')")
    Spacer()
    print("- (Work In Progress) BlackJack - A card game based around getting to 21, without going over (Type 'BlackJack' to play)")
    Spacer()
    choice = input("'INPUT' Where do you want to go - ")
    if "dna" in choice.lower():
        print("Connecting...")
        time.sleep(2)
        print("Connection Complete...")
        DnaReader()
    if "help" in choice.lower():
        HLNAHOMEPAGE_help()
    if "blackjack" in choice.lower():
        print("This is a work in progress.")
        print("Estimated patch notes: 1.1.0")
    else:
        print("Connection throttled...")
        print("Please type correctly next time")
        time.sleep(2)
        HOMEPAGE()
def start():
    print("DISCLAIMER: PLEASE ONLY TYPE WHEN IT SAYS 'INPUT'")
    time.sleep(1)
    print("SYN Complete...")
    time.sleep(1)
    print("Server Booting up...")
    time.sleep(1)
    print("Connection Complete...")
    time.sleep(1)
    print("Release 1.0")
    time.sleep(1)
    HOMEPAGE()
start()
