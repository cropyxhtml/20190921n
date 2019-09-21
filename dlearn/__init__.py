from dlearn.iris import IrisModel
from dlearn.lena import Lena
from dlearn.fashion import Fashion
from dlearn.img_editor import ImgEditor

import matplotlib.pyplot as plt
if __name__ == '__main__':
    def print_menu():
        print('0 EXIT')
        print('1 IRIS DATA')
        print('2 IRIS SCATTER')
        print('3 IRIS 결정border')
        print('4 LENA perception')
        print('5 Fashion')
        print('6 Image Editor')
        print('')
    while True:
        print_menu()
        menu = int(input())
        if menu == 0:
            print('EXIT Done')
            break
        elif menu == 1:
            print('<1>')
            m = IrisModel()
            print('RESULT :%s'% m.get_iris())
        elif menu == 2 :
            print('<2>')
            m = IrisModel()
            m.draw_scatter()
        elif menu == 3 :
            print('<3>')
            m = IrisModel()
            m.plot_decision_regions()
        elif menu == 4 :
            print('<4>')
            m = Lena()
            m.execute()
        elif menu == 5 :
            print('<5>')
            m = Fashion()
            arr = m.create_model()
            predictions = arr[0]
            test_labels =arr[1]
            img = arr[2]
            i = 20
            plt.figure(figsize=(6,3))
            plt.subplot(1,2,1)
            m.plot_image(i,predictions,test_labels,img)
            plt.subplot(1,2,2)
            m.plot_value_array(i, predictions, test_labels)
            plt.show()
            break
        elif menu == 6 :
            print('<6>')
            m = ImgEditor()
            m.execute()
            break