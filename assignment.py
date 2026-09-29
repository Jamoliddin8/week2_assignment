number=int(input('Enter the number of cupcakes: '))
student=input('Are you a student? (yes/no): ')
money=int(input('Enter the money you have: '))
if student=="yes":
    if number>=6:
        price=3
        total=price*number
        print(f"Price per cupcake: {price}")
        print(f"Total cost: {total}")
        remaining=money-total
        if remaining>0:
            print(f"Money left: {remaining}")
        elif remaining==0:
            print('Exactly enough money')
        else:
            print(f"More money needed: {-remaining}")
    else:
        price=5
        total=price*number
        print(f"Price per cupcake: {price}")
        print(f"Total cost: {total}")
        remaining=money-total
        if remaining>0:
            print(f"Money left: {remaining}")
        elif remaining==0:
            print('Exactly enough money')
        else:
            print(f"More money needed: {-remaining}")
else:
    if number>=6:
        price=5
        total=price*number
        print(f"Price per cupcake: {price}")
        print(f"Total cost: {total}")
        remaining=money-total
        if remaining>0:
            print(f"Money left: {remaining}")
        elif remaining==0:
            print('Exactly enough money')
        else:
            print(f"More money needed: {-remaining}")
    else:
        price=7
        total=price*number
        print(f"Price per cupcake: {price}")
        print(f"Total cost: {total}")
        remaining=money-total
        if remaining>0:
            print(f"Money left: {remaining}")
        elif remaining==0:
            print('Exactly enough money')
        else:
            print(f"More money needed: {-remaining}")