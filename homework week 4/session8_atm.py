def checkpin(user_pin):
    if user_pin == '1234':
        print('correct pin')
        return True
    else:
        return False

def user_authentication():
    tries = 0
    while tries < 3:
        user_pin =input('Please enter your pin: ')
        if checkpin(user_pin):
            print('Pin Sucess')
            return True
        else:
            print('Incorrect pin')
            tries = tries + 1
    raise ValueError('Too many incorrect attempts')
    return False

def withrawl_amount(balance):
    while True:
        withdrawl = int(input('Choose withdrawl amount:'))
        try:
            if withdrawl > balance:
                raise Exception
            balance = balance - withdrawl
            print("new balance " + str(balance))
            return balance
        except:
            raise Exception('Your balance is too low')
        finally:
            print('Removing your card')
    return

balance = 100

def atm(user_pin):
    if user_authentication():
        withrawl_amount(balance)

def main():
    print(atm('1234'))

if __name__ == '__main__':
    main()