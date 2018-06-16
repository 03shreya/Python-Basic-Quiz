quiz_ques = ["Paulo Coelho  is a Brazilian lyricist and 1______. \nHe was born in 2 ______ on August 24, 1947.\nHis novel 3 ______ has been translated into 4____ languages.",
              "According to The Washington Post, Paulo Coelho has sold an estimated 1_____ million books. \nIn 2________, Paulo Coelho finished uploading around 3 _______ documents-manuscripts,  press clippings-and created a virtual Paulo Coelho Foundation, together with the physical foundation which is based in 4______."]


ans = [["novelist" , "brazil","the alchemist","81"] , ["350","noveber 2014","80,000","geneva"]]


def quiz (ques,ans) :
    #takes 2 inputs calls other funcs to show quiz and check ans and continue further
    display(ques)
    check_ans(ques,ans)
    moving_on()

def moving_on():
    #asks if move on further with quiz or not
    uinput = raw_input("Ready for the next challange? \n to continue press YES , to quit press NO .").lower()
    if uinput=='YES':
        play_it(quiz_ques,ans)
    else :
        print("\nThanks for playing the quiz. See you next time.\n")





def display(ques):
    print ques

def check_ans(ques,ans):
    #checks if ans is right or not
    for ans_index in xrange(0,4):
     questNo = ans_index + 1
    while(1):
        answer = input("\nEnter the answer for question " + str(questNo) + " is :  ").lower()
        if answer == ans[ans_index]:
            ques = right(ques,answer,questNo)
            display(ques)
            break
        else:
            wrong()
            display(ques)
print "\nCongratulations , the answer is correct:  \n"


def choose_level():
    print("Choose the level of the quiz : ")
    user_input=int(raw_input("Enter 1 for Level 1 \n" + "Enter 2 for Level 2  \n"  + "The level is :  "))
    print("\nLet the quiz begin : ")
    return user_input - 1



def right (ques,ans,i):
    #executes when correct ans,has got 3 inputs and prints some statement
    print("Good job , the ans is correct\n")
    change(ques,ans,i)
    return ques

def wrong(ques,ans,i):
    print("OOPS , the answer you entered is incorrect . TRY AGAIN.")

def change (ques,ans,i):
    #fills the blank with the right ans and displays.
    final_ans = []
    initial_ans = ques.split()
    for word in initial_ans:
        if word != str(index) + "_____":
            final_ans.append(word)
        else:
            final_ans.append(ans)
    ques=" ".join(final_ans)
    return ques

def play_it(quiz_ques,ans) :
    #takes two inputs and calls other functns to decide the level and play the quiz further
    print("WELCOME, to the quiz session.")
    level=choose_level()
    question=quiz_ques[level]
    answer=ans[level]
    quiz(question,answer)


play_it(quiz_ques,ans)
