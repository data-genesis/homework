my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
while index < len(my_list):
    if my_list[index] == 0:
        index += 1
    elif my_list[index] >= 1:
      print(my_list[index])
      index += 1
    # elif my_list[index] <= 1:  // Позволяет не останавливаться на 0
    #   index += 1  // и отрицательных числах
    else:
        break


  