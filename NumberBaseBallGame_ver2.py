def MakeAnswer():
    import random
    lenAns = 3
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = random.sample(numlist, lenAns)
    print ('answer is :', answer)
    return answer

def CheckInputValid(answer):
    namePass = False
    while not namePass:
        num = input('put 3 of sequential numbers \nInput :');
        try: int(num); namePass = True
        except: print('please input integer')
        if len(num) == len(answer) & len(set(num)) == len(answer): pass
        else: namePass = False; print('please input 3 of different numbers')
        if namePass == True: pass
    return namePass, num

def CountStrikeAndBall(num, answer):
    S = 0
    B = 0
    for i in range(len(num)):
        if int(num[i]) in answer and int(num[i]) == answer[i]: S = S + 1
        elif int(num[i]) in answer and int(num[i]) != answer[i]: B = B + 1
    return S, B

def Evaluation(S, B):
    if S == 3:
        print("=== Correct! Game Over ===")
        Play = False
    elif B == 0 and S == 0:
        Play = True
        print('Out, Try something different.')
    else:
        Play = True
        print('%dS %dB' %(S, B))
    return Play

def NumberBaseBallGame():
    answer = MakeAnswer()
    Play = True
    while Play:
        namePass, num = CheckInputValid(answer)
        if namePass == True:
            S, B = CountStrikeAndBall(num, answer)
            Play = Evaluation(S, B)

#Let's do the game!!
NumberBaseBallGame()