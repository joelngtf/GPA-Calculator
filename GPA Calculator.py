# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:43:43 2019

@author: joeln
"""

grade_alpha = 0
grade_beta = 0
grade_charlie = 0
grade_delta = 0
grade_echo = 0
grade_foxtrot = 0
grade_golf = 0
grade_hotel = 0
grade_india = 0
grade_juliett = 0
au_alpha = 0
au_beta = 0
au_charlie = 0
au_delta = 0
au_echo = 0
au_foxtrot = 0
au_golf = 0
au_hotel = 0
au_india = 0
au_juliett = 0
loopa1 = 0
loopb1 = 0
loopc1 = 0
loopd1 = 0
loope1 = 0
loopf1 = 0
loopg1 = 0


print("Welcome to Joel's GPA Calculator!")
print("This software calculates up to 7 modules!")
print("For each line, key in the module's grade,")
print("followed by their respective academic units.")
print("If you have keyed in all your values and there are existing")
print("slots, key in 0 to skip to the end.")
previous_gpa = float(input("What is your previous GPA: "))
# Module Alpha #
inputgrade_alpha = str(input("Grade for 1st Module: "))
while loopa1 == 0:
    if inputgrade_alpha == "A+":
        grade_alpha = 5
        loopa1 = 1
    elif inputgrade_alpha == "A":
        grade_alpha = 5
        loopa1 = 1
    elif inputgrade_alpha == "A-":
        grade_alpha = 4.5
        loopa1 = 1
    elif inputgrade_alpha == "B+":
        grade_alpha = 4
        loopa1 = 1
    elif inputgrade_alpha == "B":
        grade_alpha = 3.5
        loopa1 = 1
    elif inputgrade_alpha == "B-":
        grade_alpha = 3
        loopa1 = 1
    elif inputgrade_alpha == "C+":
        grade_alpha = 2.5
        loopa1 = 1
    elif inputgrade_alpha == "C":
        grade_alpha = 2
        loopa1 = 1
    elif inputgrade_alpha == "D+":
        grade_alpha = 1.5
        loopa1 = 1
    elif inputgrade_alpha == "D":
        grade_alpha = 1
        loopa1 = 1
    elif inputgrade_alpha == "F":
        grade_alpha = 0
        loopa1 = 1
    elif inputgrade_alpha == "0":
        grade_alpha = 0
        loopa1 = 1    
    else:
        inputgrade_alpha = str(input("Please input a grade from A+ to F :"))
au_alpha = int(input("AUs for 1st Module: "))
# Module Beta #
inputgrade_beta = str(input("Grade for 2nd Module: "))
while loopb1 == 0:
    if inputgrade_beta == "A+":
        grade_beta = 5
        loopb1 = 1
    elif inputgrade_beta == "A":
        grade_beta = 5
        loopb1 = 1
    elif inputgrade_beta == "A-":
        grade_beta = 4.5
        loopb1 = 1
    elif inputgrade_beta == "B+":
        grade_beta = 4
        loopb1 = 1
    elif inputgrade_beta == "B":
        grade_beta = 3.5
        loopb1 = 1
    elif inputgrade_beta == "B-":
        grade_beta = 3
        loopb1 = 1
    elif inputgrade_beta == "C+":
        grade_beta = 2.5
        loopb1 = 1
    elif inputgrade_beta == "C":
        grade_beta = 2
        loopb1 = 1
    elif inputgrade_beta == "D+":
        grade_beta = 1.5
        loopb1 = 1
    elif inputgrade_beta == "D":
        grade_beta = 1
        loopb1 = 1
    elif inputgrade_beta == "F":
        grade_beta = 0
        loopb1 = 1
    elif inputgrade_beta == "0":
        grade_beta = 0
        loopb1 = 1
    elif inputgrade_beta == "x":
        break
    else:
        inputgrade_beta = str(input("Please input a grade from A+ to F :"))
au_beta = int(input("AUs for 2nd Module: "))

# Module Charlie #
inputgrade_charlie = str(input("Grade for 3rd Module: "))
while loopc1 == 0:
    if inputgrade_charlie == "A+":
        grade_charlie = 5
        loopc1 = 1
    elif inputgrade_charlie == "A":
        grade_charlie = 5
        loopc1 = 1
    elif inputgrade_charlie == "A-":
        grade_charlie = 4.5
        loopc1 = 1
    elif inputgrade_charlie == "B+":
        grade_charlie = 4
        loopc1 = 1
    elif inputgrade_charlie == "B":
        grade_charlie = 3.5
        loopc1 = 1
    elif inputgrade_charlie == "B-":
        grade_charlie = 3
        loopc1 = 1
    elif inputgrade_charlie == "C+":
        grade_charlie = 2.5
        loopc1 = 1
    elif inputgrade_charlie == "C":
        grade_charlie = 2
        loopc1 = 1
    elif inputgrade_charlie == "D+":
        grade_charlie = 1.5
        loopc1 = 1
    elif inputgrade_charlie == "D":
        grade_charlie = 1
        loopc1 = 1
    elif inputgrade_charlie == "F":
        grade_charlie = 0
        loopc1 = 1
    elif inputgrade_charlie == "0":
        grade_charlie = 0
        loopc1 = 1
    else:
        inputgrade_charlie = str(input("Please input a grade from A+ to F :"))
au_charlie = int(input("AUs for 3rd Module: "))

# Module Delta #
inputgrade_delta = str(input("Grade for 4th Module: "))
while loopd1 == 0:
    if inputgrade_delta == "A+":
        grade_delta = 5
        loopd1 = 1
    elif inputgrade_delta == "A":
        grade_delta = 5
        loopd1 = 1
    elif inputgrade_delta == "A-":
        grade_delta = 4.5
        loopd1 = 1
    elif inputgrade_delta == "B+":
        grade_delta = 4
        loopd1 = 1
    elif inputgrade_delta == "B":
        grade_delta = 3.5
        loopd1 = 1
    elif inputgrade_delta == "B-":
        grade_delta = 3
        loopd1 = 1
    elif inputgrade_delta == "C+":
        grade_delta = 2.5
        loopd1 = 1
    elif inputgrade_delta == "C":
        grade_delta = 2
        loopd1 = 1
    elif inputgrade_delta == "D+":
        grade_delta = 1.5
        loopd1 = 1
    elif inputgrade_delta == "D":
        grade_delta = 1
        loopd1 = 1
    elif inputgrade_delta == "F":
        grade_delta = 0
        loopd1 = 1
    elif inputgrade_delta == "0":
        grade_delta = 0
        loopd1 = 1
    else:
        inputgrade_delta = str(input("Please input a grade from A+ to F :"))
au_delta = int(input("AUs for 4th Module: "))

# Module Echo #
inputgrade_echo = str(input("Grade for 5th Module: "))
while loope1 == 0:
    if inputgrade_echo == "A+":
        grade_echo = 5
        loope1 = 1
    elif inputgrade_echo == "A":
        grade_echo = 5
        loope1 = 1
    elif inputgrade_echo == "A-":
        grade_echo = 4.5
        loope1 = 1
    elif inputgrade_echo == "B+":
        grade_echo = 4
        loope1 = 1
    elif inputgrade_echo == "B":
        grade_echo = 3.5
        loope1 = 1
    elif inputgrade_echo == "B-":
        grade_echo = 3
        loope1 = 1
    elif inputgrade_echo == "C+":
        grade_echo = 2.5
        loope1 = 1
    elif inputgrade_echo == "C":
        grade_echo = 2
        loope1 = 1
    elif inputgrade_echo == "D+":
        grade_echo = 1.5
        loope1 = 1
    elif inputgrade_echo == "D":
        grade_echo = 1
        loope1 = 1
    elif inputgrade_echo == "F":
        grade_echo = 0
        loope1 = 1
    elif inputgrade_echo == "0":
        grade_echo = 0
        loope1 = 1
    else:
        inputgrade_echo = str(input("Please input a grade from A+ to F :"))
au_echo = int(input("AUs for 5th Module: "))

# Module Foxtrot #
inputgrade_foxtrot = str(input("Grade for 6th Module: "))
while loopf1 == 0:
    if inputgrade_foxtrot == "A+":
        grade_foxtrot = 5
        loopf1 = 1
    elif inputgrade_foxtrot == "A":
        grade_foxtrot = 5
        loopf1 = 1
    elif inputgrade_foxtrot == "A-":
        grade_foxtrot = 4.5
        loopf1 = 1
    elif inputgrade_foxtrot == "B+":
        grade_foxtrot = 4
        loopf1 = 1
    elif inputgrade_foxtrot == "B":
        grade_foxtrot = 3.5
        loopf1 = 1
    elif inputgrade_foxtrot == "B-":
        grade_foxtrot = 3
        loopf1 = 1
    elif inputgrade_foxtrot == "C+":
        grade_foxtrot = 2.5
        loopf1 = 1
    elif inputgrade_foxtrot == "C":
        grade_foxtrot = 2
        loopf1 = 1
    elif inputgrade_foxtrot == "D+":
        grade_foxtrot = 1.5
        loopf1 = 1
    elif inputgrade_foxtrot == "D":
        grade_foxtrot = 1
        loopf1 = 1
    elif inputgrade_foxtrot == "F":
        grade_foxtrot = 0
        loopf1 = 1
    elif inputgrade_foxtrot == "0":
        grade_foxtrot = 0
        loopf1 = 1
    else:
        inputgrade_foxtrot = str(input("Please input a grade from A+ to F :"))
au_foxtrot = int(input("AUs for 6th Module: "))

# Module Golf #
inputgrade_golf = str(input("Grade for 7th Module: "))
while loopg1 == 0:
    if inputgrade_golf == "A+":
        grade_golf = 5
        loopg1 = 1
    elif inputgrade_golf == "A":
        grade_golf = 5
        loopg1 = 1
    elif inputgrade_golf == "A-":
        grade_golf = 4.5
        loopg1 = 1
    elif inputgrade_golf == "B+":
        grade_golf = 4
        loopg1 = 1
    elif inputgrade_golf == "B":
        grade_golf = 3.5
        loopg1 = 1
    elif inputgrade_golf == "B-":
        grade_golf = 3
        loopg1 = 1
    elif inputgrade_golf == "C+":
        grade_golf = 2.5
        loopg1 = 1
    elif inputgrade_golf == "C":
        grade_golf = 2
        loopg1 = 1
    elif inputgrade_golf == "D+":
        grade_golf = 1.5
        loopg1 = 1
    elif inputgrade_golf == "D":
        grade_golf = 1
        loopg1 = 1
    elif inputgrade_golf == "F":
        grade_golf = 0
        loopg1 = 1
    elif inputgrade_golf == "0":
        grade_golf = 0
        loopg1 = 1
    else:
        inputgrade_golf = str(input("Please input a grade from A+ to F :"))
au_golf = int(input("AUs for 7th Module: "))

# Results Calculator #
sumau = au_alpha + au_beta + au_charlie + au_delta+ au_echo + au_foxtrot + au_golf
sumgpa =(au_alpha * grade_alpha) + (au_beta * grade_beta) + (au_charlie * grade_charlie) + (au_delta * grade_delta) + (au_echo* grade_echo) + (au_foxtrot * grade_foxtrot) +(au_golf * grade_golf)
gpa = float(sumgpa / sumau)
print("Your total AUs for this semester is", sumau,"AUs.")
print("Your total score for this semester is", sumgpa,".")
print("Hence, your current GPA for this semester is", gpa,".")
if 4.5<=gpa<5:
    print("Congrats! This GPA is Honors (Highest Distinction) or First Class Honors!")
elif 4<=gpa<4.5:
    print("Congrats! This GPA is Honors (Distinction) or Second Class Upper Honors!")
elif 3.5<=gpa<4:
    print("Congrats! This GPA is Honors (Merit) or Second Class Lower Honors!")
elif 3<=gpa<3.5:
    print("Congrats! This GPA is Honors or Third Class Honors/Pass with Merit!")
elif 2<=gpa<3:
    print("Congrats! This GPA is a Pass!")
elif 0<=gpa<2:
    print("Warning! Your GPA does not meet the requirements to graduate. Try harder again!")
else:
    print("Impossible! Please check your values again")
goalgpa = int(input("What is your goal GPA: "))
nextgpa = (goalgpa * 2) - gpa
if nextgpa>= 0:
    print("For the next semester, you should be aiming for a GPA of", nextgpa,".")
else:
    print("Check your values or drop out, you cunt.")
