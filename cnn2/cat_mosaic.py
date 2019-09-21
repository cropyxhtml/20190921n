import cv2
class CatMosaic:
    def __init__(self):
        self._file_load_name = './data/cat.jpg'

    def mosaic(self):
        load_img = cv2.imread(self._file_load_name)
        ''' start to mosaic '''
        mos = self.mosaic_execute(load_img,(50,50,450,450),10)
        cv2.imwrite('cat-mosaic.png',mos)
        ''' Done '''
        cv2.imshow('hello',mos)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    @staticmethod
    def mosaic_execute(img, rect, size):
        (x1, y1, x2, y2) = rect
        w = x2 - x1
        h = y2 = y1
        i_rect = img[y1:y2, x1:x2]
        i_small = cv2.resize(i_rect, (size, size))
        i_mos = cv2.resize(i_small, (w,h), interpolation=cv2.INTER_AREA)
        img2 = img.copy()
        img2[y1:y2, x1:x2] = i_mos
        return img2
