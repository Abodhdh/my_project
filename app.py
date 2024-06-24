names = {111:'ali',222:'ahmed',333:'hssan'}
def your_number(num):
    for i in names.keys():
        if i == num:
            print(names[i])
            break
        else:
            print('sorry')
your_number(333)

x = 2