import cv2
import numpy as np


class Image:
    name = ''
    path = ''
    extension = ''
    pixels = []
    rowSize = 0
    lookUpTable = []

    def __init__(self, file_name):
        self.name = file_name
        self.path = 'common/files/input/' + file_name
        self.extension = self.path.split('.')[1]
        self.pixels = self.readGrayImage()
        self.rowSize, self.colSize = self.pixels.shape
        self.convertPixelValuesToOpposite()

    def readGrayImage(self):
        image = cv2.imread(self.path)
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def convertPixelValuesToOpposite(self):
        for i in range(256):
            self.lookUpTable.append(255 - i)

        self.setPixelValuesByLookUpTable()

    def setPixelValuesByLookUpTable(self):
        lookUpTable = np.array(self.lookUpTable, dtype=np.uint8)
        self.pixels = lookUpTable[self.pixels]
        self.lookUpTable = []

    def isEqualTo(self, image):
        if not self.isEqualInSize(image):
            raise Exception('Image sizes are not equal!')

        if np.bitwise_xor(self.pixels, image.pixels).any():
            return False
        return True

    def isEqualInSize(self, image):
        if self.pixels.shape != image.pixels.shape:
            return False
        return True

    def save(self):
        self.convertPixelValuesToOpposite()
        cv2.imwrite('common/files/output/' + self.name, self.pixels)
