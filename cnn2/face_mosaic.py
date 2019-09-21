import cv2

class FaceMosaic:
    def __init__(self):
        self._load_file_cascade = './data/haarcascade_frontalface_alt.xml'
        self._load_file_girl = './data/girl.jpg'
    '''Just Read'''
    def read(self):
        load_img = cv2.imread(self._load_file_girl)
        cv2.imshow('hello', load_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    ''''''
    def face_mosaic(self):
        cascade = cv2.CascadeClassifier(self._load_file_cascade)
        img = cv2.imread(self._load_file_girl)
        face = cascade.detectMultiScale(img, minSize=(150,150))
        if len(face) ==0:
            print('얼굴인식 fail')
            quit()
        for (x, y, w, h) in face:
            print('얼굴의 좌표 =', x, y, w, h)
            img = self.mosaic_execute(img, (x, y, x+w, y+h), 10)
        cv2.imwrite('girl-mosaic.png',img)
        cv2.imshow('girl-mosaic',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def mosaic_execute(img, rect, size):
        (x1, y1, x2, y2) = rect
        w = x2 - x1
        h = y2 = y1
        i_rect = img[y1:y2, x1:x2]
        i_small = cv2.resize(i_rect, (size, size))
        i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
        img2 = img.copy()
        img2[y1:y2, x1:x2] = i_mos
        return img2