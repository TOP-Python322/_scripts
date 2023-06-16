try:
    1 / 0
    1 / 1

except ZeroDivisionError as exception:
    print(exception)
    1 / 0

else:
    print('выполнено успешно')

finally:
    print('завершение')



try:
    1 / 0
finally:
    print('завершение')
