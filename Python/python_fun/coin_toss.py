import random
def coin_toss():
    head_count = 0
    tail_count = 0
    for i in range(5001):
        toss = random.randint(1,3)
        if toss == 1:
            head_count += 1
            print "Attempt #" + str(i) + ":  Throwing a coin... It's a head! ... Got " + str(head_count) + " head(s) so far and" + str(tail_count) + "(s) so far"
        elif toss == 2:
            tail_count += 1
            print "Attempt #" + str(i) + ":  Throwing a coin... It's a tail! ... Got " + str(tail_count) + " tail(s) so far and" + str(head_count) + "(s) so far"
    print "Ending the program, thank you!"
coin_toss()
