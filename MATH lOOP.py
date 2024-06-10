correct_answer = 20
question_1_answered = False
answer_count = 0
answer_limit = 3
out_of_answers = False
trys_count = 0
trys_limit = 3
out_of_trys = False
questtion = print("10+10")
answer=0

while answer != correct_answer and not out_of_answers:
    if answer_count != answer_limit:
       answer = float(input(">>"))
       answer_count +=1
       if trys_count != trys_limit and not out_of_trys:
           if answer != correct_answer:
            print("try again")
            trys_count+=1
           if answer == correct_answer:
              if answer_count == 1:
                    print("***")
              elif answer_count == 2:
                    print("**")
              elif answer_count == 3:
                    print("*")
       else:
            out_of_answers =True
            break
if out_of_answers:
    print("you Loose")
else:
    print("you win")
