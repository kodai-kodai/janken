

while count <= 3:
    user = int(input('数を入力して下さい。'))
    cpu = CPU_rand()
    if judge_winner() == "same":
        print('あいこです。再度入力してください。')
        continue
    elif judge_winner() == "win" :
        cnt_user+=1
        count+= 1
    else:
        cnt_cpu+=1
        count+=1
        

print(f'あなた：{cnt_user}勝')
print(f'コンピューター：{cnt_cpu}勝')
if cnt_user > cnt_cpu:
    print('あなたの総合勝利です！')
else:
    print('CPUの総合勝利です！')
#キー入力の受付
    
