# https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html
import cv2
class Lena:
    def __init__(self):
        self.file_load_name = './data/lena.jpg'

    def execute(self):
        original =cv2.imread(self.file_load_name, cv2.IMREAD_COLOR)
        gray = cv2.imread(self.file_load_name, cv2.IMREAD_GRAYSCALE)
        unchanged = cv2.imread(self.file_load_name, cv2.IMREAD_UNCHANGED)
        '''
        이미지 읽기 3가지로  위 IMREAD_ 값대신에 1, 0 , -1 사용 가능
        '''
        cv2.imshow('Original',original)
        cv2.imshow('Gray',gray)
        cv2.imshow('Unchanged',unchanged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()