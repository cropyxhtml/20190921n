import matplotlib.pyplot as plt
from digits.hand_writing import HandWriting
if __name__ == '__main__':
    def print_menu():
        print('0 EXIT')
        print('1 손글씨 인식')
        print('2 learning')
        print('3 테스트')
        print('')
        return int(input('Choose one\n'))
    while True:
        menu = print_menu()
        print('MENU : %s'% menu)
        if menu == 0:
            print('EXIT')
            break
        elif menu == 1:
            m = HandWriting()
            # m.read_file()
            # m.read_nums()
            m.read_file()
            break
        elif menu == 2:
            m = HandWriting()
            m.learning()
            break
        elif menu == 3:
            m = HandWriting()
            file_name = './data/my9.png'
            print('테스트')

            print(m.test(file_name))
            break
        elif menu == 4:

            break