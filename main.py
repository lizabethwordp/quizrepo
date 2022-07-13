import question_data

# Ascii art for the quiz 
quiz_ascii = '''
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_|  
'''
print(quiz_ascii)
#points = len(question_data.questions)
points = 0
# questions=[]
# # print(questions)
# a = question_data.questions('question')

current_number = 0

while current_number < 10:
  print(question_data.questions[current_number]['question'])
  user_input= input("True or False: ").lower().strip()
  if user_input == question_data.questions[current_number]['correct_answer'].lower():
    print("Correct")
    points += 1
  else:
    print("incorrect, you got 0 points")
  print(f"Current point is: {points}/{current_number+1} ")
  print("\n")
  current_number += 1

