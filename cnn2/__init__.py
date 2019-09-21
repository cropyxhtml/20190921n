import matplotlib.pyplot as plt
from cnn2.face_detect import FaceDetect
from cnn2.cat_mosaic import CatMosaic
from cnn2.face_mosaic import FaceMosaic
if __name__ == '__main__':
    def print_menu():
        print('0 EXIT')
        print('1 얼굴인식')
        print('2 고양이 모자이크') #xml 파일이 없으면 얼굴 특정 실패
        print('3 얼굴 모자이크')
        print('')
        return int(input('Choose one\n'))
    while True:
        menu = print_menu()
        print('MENU : %s'% menu)
        if menu == 0:
            print('EXIT')
            break
        elif menu == 1:
            m = FaceDetect
            m.read_file()
            break
        elif menu == 2:
            m = CatMosaic()
            m.mosaic()
            break
        elif menu == 3:
            m = FaceMosaic()
            m.face_mosaic()
            # m.read()
            break
        elif menu == '':

            break
