user_pin1 = '0000'
def checkpin1(user_pin1):
    if user_pin1 == '1234':
        print('correct pin')
        return 'correct'
    else:
        print('wrong code')
        return 'incorrect'


def main():
    print(checkpin1(user_pin1))

if __name__ == '__main__':
    main()

