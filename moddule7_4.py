
def win():
    global score1, score2, team1_time, team2_time
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        result = "Победа команды Мастера кода!"
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        result = "Победа команды Волшебники Данных!"
    else:
        result = "Ничья!"
    return result
# Использование %:
team1_num = 6
team2_num = 5
print("В команде Мастера кода участников: %s" % team1_num)
print("В команде Волшебники Данных участников: %s" % team2_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
# Использование format():
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print("Команда Мастера кода решила задач: {}".format(score1))
print("Команда Волшебники данных решила задач: {}".format(score2))
print("Мастера кода решили задачи за {} с!".format(team1_time))
print("Волшебники данных решили задачи за {} с!".format(team2_time))
# Использование f-строк:
tasks_total = 82
sum_score = score1 + score2
sum_time = team1_time + team2_time
time_avg = int(sum_score % sum_time)
print(f"Команды решили {score1} и {score2} задач.")
challenge_result = win()
print(challenge_result)
print(f"Сегодня было решено {score1 + score2} задач, в среднем по {time_avg} секунды на задачу!.")


