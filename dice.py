#Importing packages
import random
import matplotlib.pyplot as plt

def roll():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    
    if dice_1 == dice_2:
        same_num = True
    else:
        same_num = False
    return same_num

sims = 10000
max_num_rolls = 1000
bet = 1

win_prob = []
end_balance = []

graph = plt.figure()
plt.xlabel("Roll number")
plt.ylabel("Balance [$]")
plt.title("Monte Carlo simulation")
plt.xlim([0, max_num_rolls])

for i in range(sims):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0
    
    while num_rolls[-1] < max_num_rolls:
        same = roll()
        
        if same:
            balance.append(balance[-1] + 4*bet)
            num_wins += 1
        else:
            balance.append(balance[-1] - bet)
            
        num_rolls.append(num_rolls[-1] + 1)
        
    win_prob.append(num_wins/num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)
    
plt.show()
overall_win_prob = sum(win_prob)/len(win_prob)
overall_end_bal = sum(end_balance)/len(end_balance)
print(overall_win_prob, ": overall win prob")
print(overall_end_bal, ": overall end balance (avg.)")
