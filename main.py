import cv2
import numpy as np
import argparse
import cv2 as cv
from matplotlib import pyplot as plt
from numpy import double


def print_list():
    print("-------------------------------------------------------")
    print(" Click on o to showing the image ")
    print(" Click on g to convert the image to gray-scale ")
    print(" Click on + to increase brightness ")
    print(" Click on - to decrease brightness ")
    print(" Click on c to improve the contrast ")
    print(" Click on t to convert the image to thresholding ")
    print(" Click on s to save processed image ")
    print(" Click on e to exit ")
    return

while(1):

    img=cv2.imread('alaqsamousq.jpeg')
    gnew=0
    print_list()
    value = input("enter")


    

    if value == "o":
        cv2.imshow('sample image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif value=="t":
        grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        retval2, threshold2 = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow('original', img)
        cv2.imshow('Otsu threshold', threshold2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif value=="g":
        cv2.imshow('Original', img)
        cv2.waitKey(0)


        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Grayscale', gray_image)
        cv2.waitKey(0)


        cv2.destroyAllWindows()



    elif value=="s":

        img = cv2.imread('alaqsamousq.jpeg')
        cv2.imwrite('savedimage.jpeg', img)


    elif value=="+":

        parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
        parser.add_argument('--input', help='test.png', default='test.png')
        args = parser.parse_args()
        image = cv.imread(cv.samples.findFile(args.input))
        if image is None:
            print('Could not open or find the image: ', args.input)
            exit(0)
        new_image = np.zeros(image.shape, image.dtype)
        alpha = 1.0  # Simple contrast control
        beta = 0  # Simple brightness control
        # Initialize values
        print(' Basic Linear Transforms ')
        print('-------------------------')
        try:
            alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
            beta = int(input('* Enter the beta value [0-100]: '))
        except ValueError:
            print('Error, not a number')

        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                for c in range(image.shape[2]):
                    new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)
        cv.imshow('Original Image', image)
        cv.imshow('New Image', new_image)
        # Wait until user press some key
        cv.waitKey()
        img = cv2.imread('test.png')
        cv2.imwrite('test221.jpeg', new_image)

    elif value=="c":
        from PIL import Image, ImageEnhance

        # read the image
        im = Image.open("test.png")

        # image brightness enhancer
        enhancer = ImageEnhance.Contrast(im)

        factor = 1  # gives original image
        im_output = enhancer.enhance(factor)
        im_output.save('original21-image.png')

        factor = 0.5  # decrease constrast
        im_output = enhancer.enhance(factor)
        im_output.save('less21-contrast-image.png')

        factor = 1.5  # increase contrast
        im_output = enhancer.enhance(factor)
        im_output.save('more21-contrast-image.png')
    elif value=="-":

        parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
        parser.add_argument('--input', help='test.png', default='test.png')
        args = parser.parse_args()
        image = cv.imread(cv.samples.findFile(args.input))
        if image is None:
            print('Could not open or find the image: ', args.input)
            exit(0)
        new_image = np.zeros(image.shape, image.dtype)
        alpha = 1.0  # Simple contrast control
        beta = 0  # Simple brightness control
        # Initialize values
        print(' Basic Linear Transforms ')
        print('-------------------------')
        try:
            alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
            beta = int(input('* Enter the beta value [0-100]: '))
        except ValueError:
            print('Error, not a number')

        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                for c in range(image.shape[2]):
                    new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)
        cv.imshow('Original Image', image)
        cv.imshow('New Image', new_image)
        # Wait until user press some key
        cv.waitKey()
        img = cv2.imread('test.png')
        cv2.imwrite('test22.jpeg', new_image)

    elif value == "e":
        break













