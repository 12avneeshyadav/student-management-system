print("today i created a mcq in Python\n")

questions = [
    {
        "question": "which language is used for web app??",
        "option": ['Python','JavaScript','Java','C language'],
        "answer": "JavaScript",
    },
    {
        "question": "which language syntax is easy to understand??",
        "option": ['Python','JavaScript','Java','C language'],
        "answer": "Python",
    },
    {
        "question": "How many coding language is present in india??",
        "option": ['3','100+','40','90'],
        "answer": "100+",
    },
    {
        "question": "which language is used for creating a website home page structure??",
        "option": ['Python','JavaScript','Java','HTML'],
        "answer": "HTML",
    },
    {
        "question": "how is the P.M of India??",
        "option": ['Narendra Modi','Akhilesh Bhaiya','Lalu(Bihari)','Yogi(Landchatt)'],
        "answer": "Akhilesh Bhaiya",
    }
]

score = 0

i = 1
for q in questions:
    print(f"{i}. {q['question']}")
    print(f"A. {q['option'][0]}")
    print(f"B. {q['option'][1]}")
    print(f"C. {q['option'][2]}")
    print(f"D. {q['option'][3]}")
    print()
    i+=1
    
    userInput = input("Enter User Answer: ").upper()
    
    if userInput == "A":
        selected = q['option'][0]
    
    elif userInput == "B":
        selected = q['option'][1]
    
    elif userInput == "C":
        selected = q['option'][2]
    
    elif userInput == "D":
        selected = q['option'][3]
    
    if selected == q['answer']:
        print("Write Answer !!\n")
        score+=1
    else:
        print(f"Wrong Answer !! and write answer is {q['answer']}\n")

print(f"Quiz finished !!\nYour final Score is {score}/{len(questions)}")