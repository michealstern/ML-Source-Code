questions = [
["Q.1 Which language was used to creat fb?", "python","french","javaScript","Php","None",4],
["Q.2 In C++, a function contained within a class is called?", "a method","a class function","member function","None of these",3],
["Q.3 The && and || operators compare two?", "boolean values","boolean value","numeric values","numeric value",2],
["Q.4 What is python?", "C++ library","web browser","IDE","Programming language",3],
["Q.5 Who created python?", "Denis Ritchie","Tom Cruise","Guido Van Rossum","james Gosling",3],
["Q.6 In python which keyword is used to start function?", "import","def","function","try",2],
["Q.7 Python was released publicly in which year?", "1991","1981","1961","1971",1],
["Q.8 In python which is the correct method to load a module?", "include math","#include math.h","using math","import math",4],
["Q.9 Python is said to be easily?", "Bug-able Language","Script-able Language","Writable Language","Reaable Language",4],
["Q.10 Which the following function convert a string to a frozen set in python?", "frozenset(s)","set(x)","chr(x)","dict(d)",1],
["Q.11 Which one of the following is the correct extension of the python file?", ".py",".python",".p","none of these",1],
["Q.12 Which of the following is an invalid variable?", "my_string_1","1st_string","foo","_",2],       
]
ques = [
   "Q.1 Which language was used to creat fb?",
   "Q.2 In C++, a function contained within a class is called?",
   "Q.3 The && and || operators compare two?",
   "Q.4 What is python?",
   "Q.5 Who created python?",
   "Q.6 In python which keyword is used to start function?",
   "Q.7 Python was released publicly in which year?",
   "Q.8 In python which is the correct method to load a module?",
   "Q.9 Python is said to be easily?",
   "Q.10 Which the following function convert a string to a frozen set in python?",
   "Q.11 Which one of the following is the correct extension of the python file?",
   "Q.12 Which of the following is an invalid variable?",
]
levels = [1000,3000,5000,10000,20000,40000,80000,16000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):   #This loop runs for each question.
 question = questions[i]            #Here, the question of the current criteria is stored in the question variable.
 print(f"\n\nQuestion for Rs.{levels[i]}\n")
 print(ques[i])
 print(f"a. {question[1]}         b. {question[2]} ")
 print(f"c. {question[3]}         d. {question[4]} ")
 reply = int(input("Enter your answer (1-4) "))
 if(reply == 0 ):    #If the user enters 0 then it means he has quit the game and his winning amount will be determined according to the last level.
    money = levels[i-1]
    break
 if(reply == question[-1]):
     print(f"Correct answer , you have won Rs. {levels[i]}")
     if(i == 3):
        money = 10000
     elif(i == 9):
        money = 320000
     elif(i == 14):
       money = 10000000
 else:
   print("\nWrong answer!")
   break
print(f"your take home money is {money}")
