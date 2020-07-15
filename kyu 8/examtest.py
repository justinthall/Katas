"""Takes a list of answers and compares them to a list of correct answers, and assigns points based on being right,
wrong, or not answering. """

def check_exam(arr1,arr2):
    correct_test=arr1
    to_be_checked=arr2
    score=0
    for question in zip(correct_test,to_be_checked):
        if question[1]==question[0]:
            score =score+4
            continue
        elif question[1] == '':
            score=score
            continue
        elif question[1] != question[0]:
            score =score-1
            continue
    if score<0:
        score=0
        return score
    else:
        return score