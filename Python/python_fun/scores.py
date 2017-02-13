import random
def grade_machine():
    for i in range(10):
        score = random.randint(60,101)
        if score >= 60 and score <= 69:
            print "Score: " + str(score) + "; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: " + str(score) + "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: " + str(score) + "; Your grade is B"
        else:
            print "Score: " + str(score) + "; Your grade is A"
grade_machine()
