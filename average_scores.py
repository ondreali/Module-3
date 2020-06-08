"""
program: average_scores.py
Author: Ondrea
Last date modfied: 06/07/20

The purpose of this program is to read in one person's names,
first and last, their age and three scores out of 100.
The program wants to take the three scores and find the average,
storing into a variable.
"""


def average(score1, score2, score3):
    # Get input for scores
    # declare variables, use score1, score2, score3 in calculation
    average_score = (score1 + score2 + score3)/3
    print ("the average score is: ", average_score)
    return average_score


 #declare variables, use score1, score2, score3 in calculation
if __name__ == '__main__':
   score1 = int(input("What is score1?"))
   score2 = int(input("What is score2?"))
   score3 = int(input("What is score3?"))

   #calculate average scores
   average_score = average(score1, score2, score3)

   #user will input last name and first name
   last_name = input("last name:")
   first_name = input("first name:")

   #user will input age here
   age = input("age:")

   #Print output
   #lastname, firstname, age, average grade with .2 precision
   print(f'{last_name}, {first_name} age:{age:} average grade: {average_score}')

#Example output: Rodriguez, Linda age: 21 average grade: 92.50
#Program output: Li, Ondrea age:17 average grade:95.33



