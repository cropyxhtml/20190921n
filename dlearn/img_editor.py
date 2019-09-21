import cv2

class ImgEditor:
    def __init__(self):
        self._file_load_name = './data/test.jpg'

    def execute(self):
        img = cv2.imread(self._file_load_name)
        '''img1'''
        img1 = 255-img
        '''img2'''
        img2 = -img
        '''img3 cvtColor'''
        img3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        th = 90
        img3[img3>th] = 255
        img3[img3<th] = 0
        '''img4 resize'''
        im2 = img[150:450, 150:450]
        im2 = cv2.resize(im2, (400, 400))
        # 크기 변경한 이미지 지정 저장
        cv2.imwrite('img_small.png', im2)
        '''imshow'''
        cv2.imshow('-img',img2)
        cv2.imshow('255-img',img1)
        cv2.imshow('cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)',img3)
        cv2.imshow('cv2.resize(img[150:450, 150:450],(400,400))', im2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

