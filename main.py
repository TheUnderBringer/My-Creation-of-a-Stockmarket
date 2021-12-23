from random import randint

def status():
    global status, profit
    status = 'Online'
    if current == 'Profit':
        profit = 'Yes'
    elif current == 'Non-Profit':
        profit = 'No'
    else:
        profit = 'Error'

def currency_credits():
    global current_credits, starting_credits, total_credits_gained, credits_gained, timer, random_credit_counter
    timer = randint(1,100000)
    random_credit_counter = randint(1,10000)
    current_credits = 0
    starting_credits = 2700
    credits_gained = randint(1,random_credit_counter)
    total_credits_gained = credits_gained + current_credits
    current_credits = total_credits_gained

def calculate_credits():
    global current_credits, total_credits_gained, loop, average, mininum, current, percentage, avg
    mininum = timer / current_credits
    average = credits_gained / mininum
    for loop in range(randint(1,timer)):
        total_credits_gained = credits_gained + current_credits
        current_credits = total_credits_gained
        percentage = current_credits / random_credit_counter / 1000
        if percentage > 100:
            avg = 'Error'
        elif percentage < 100:
            avg = 'Working'
        if average > mininum:
            current = 'Profit'
        elif average < mininum:
            current = 'Non-Profit'

def display():
    print('\t\t\t\tOmega Co. Stockmarket \t\t\t\tStatus: '+status+'\t\t\t\tProfit: '+profit)
    print('\t\tRounds \t\t\tTotal Credits \t\t\tAverage Credits \t\tMinimum Credits')
    print('\t\t',loop,'\t\t\t £',current_credits,'\t\t\t £',round(average,5),'\t\t\t\t £',round(mininum,5))
    print('Current Value: '+current)
    print('Percentage: %',round(percentage,1))
    print('Status: '+avg)

currency_credits()
calculate_credits()
status()
display()