print("Welcome to The Millionaire Game!!")
questions = [
    ["1.Who is Virat Kohli?","Actor","Singer","Cricketer","Teacher","3"],
    ["2.What is the colour of Mogra flower?","White","Green","Blue","Black","1"],
    ["3.What is the capital of India?","Bangalore","Pune","Mumbai","New Delhi","4"],
    ["4.Which planet is known as red planet?","Mars","Earth","Venus","Saturn","1"],
    ["5.Which is the largest ocean?","Indian Ocean","Pacific Ocean","Atlantic Ocean","Artic Ocean","2"],
    ["6.What is 2+3=?","3","6","7","5","4"],
    ["7.The english alphabets start from letter?","A","N","O","D","1"],
    ["8.What is the colour of a white-board?","Black","Green","Blue","White","4"],
    ["9.what is the capital of Maharashtra?","Pune","Nagpur","Mumbai","Satara","3"],
    ["10.What is the square of 6?","25","49","36","64","3"]
    ]
    
prices = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

i=0
for question in questions:
    print("Que. ",question[0])
    print("A. ",question[1])
    print("B. ",question[2])
    print("C. ",question[3])
    print("D. ",question[4])
    
    a=(input("Enter the answer for above question. 1 for option a, 2 for option b, 3 for option c and 4 for option d: "))
    if(question[5]==a):
        print(f"Correct answer!!. You won Rs.{prices[i]}")
    else:
        print("Sorry, wrong answer. Better luck next time.")
        break
        
    i=i+1
