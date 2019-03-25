# func name: calc_average
# arguments: five integers representing the user's test scores
# return: 1 float representing average of the test scores
# descriptions: calculating the average

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5

    return average
    
# func name: determine_grade
# arguments: 1 number reptesenting the average of the test scores
# return: 1 string representing the letter grade
# description: determine the letter grade based on the test score average

def determine_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        letter_grade = 'A'
    elif test_score >= 80 and test_score <= 89:
        letter_grade = 'B'
    elif test_score >= 70 and test_score <= 79:
        letter_grade = 'C'
    elif test_score >= 60 and test_score <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade

# func name: main
# arguments: none
# return: none
# descriptionL asks thes user for five text scores and handles calls to other functions

def main():
    test1 = input("Enter your first test score: ")
    test2 = input("Enter your second test score: ")
    test3 = input("Enter your third test score: ")
    test4 = input("Enter your fourth test score: ")
    test5 = input("Enter your fifth test score: ")

    if test1.isdigit() and test2.isdigit() and test3.isdigit() and test4.isdigit() and test5.isdigit():
        test1 = int(test1)
        test2 = int(test2)
        test3 = int(test3)
        test4 = int(test4)
        test5 = int(test5)

        avg = calc_average(test1, test2, test3, test4, test5)

        grade = determine_grade(avg)

        print("Your average test score is: " + str(avg) + ".")
        print("Your letter grade is: " + grade + ".")
    else:
        print("You did not enter input with all digits!")
    

    return

# call the main function to run the program
main()
    
