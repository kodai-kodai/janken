
from random import randint
loop_flag = True
count = 0
cnt_user = 0
cnt_cpu = 0

def CPU_rand():
    cpu =  randint(1, 3) 
    if cpu == 1:
        print('CPU：グー')
    elif cpu == 2:
        print('CPU：チョキ')
    else:
        print('CPU：パー')   
    return  cpu



loop_flag = True
def user():
    input_flag = True
    print("1,グー")
    print("2,チョキ")
    print("3,パー")
    user_hand = int(input("あなたの手を数値で入力してください>"))
    if user_hand in [1, 2, 3]:
        if user_hand == 1:
            print('あなた：グー')
        elif user_hand == 2:
            print('あなた：チョキ')
        else:
            print('CPU：パー')
        return user_hand
    else:
        while input_flag == True:
            user_hand = int(input("1,2,3の数字を半角英数字で入力してください>"))
            if user_hand in [1, 2, 3]:
                input_flag = True
                return user_hand
            
def judge_winner(user, cpu):
    if user == cpu:
        return "same"
    elif (user == 1 and cpu == 2) or (user == 2 and cpu == 3) or (user == 3 and cpu == 1):
        return "win"
    else:
        return "lose" 



