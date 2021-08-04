import cv2
import numpy as np


def interactiveThresholding(img):
    # Convert to array
    imgArray = np.array(img).astype(np.float32)

    # Set Threshold To The Mean Of The Image
    t = np.mean(img)

    # Partitions Input Image into Two groups
    ret1, r1 = cv2.threshold(img, 1, t - 1, cv2.THRESH_TRUNC)
    ret2, r2 = cv2.threshold(img, t, 255, cv2.THRESH_TRUNC)


    # Flag To Stop Loop Once Mean Values Do Not Change During Iteration
    flag = 0
    r1, r2 = imgArray.shape;

    # While to iterate till Threshold is equal to the average of m1 and m2
    while flag == 0:
        print("While Loop Starts")
        fGround = 0
        bGround = 0
        fNum = 0
        bNum = 0
        for i in range(1, r1):
            for j in range(1, r2):
                tmp = imgArray[i, j]
                if tmp >= t:
                    fGround = fGround + 1
                    fNum = fNum + float(tmp)
                else:
                    bGround = bGround + 1
                    bNum = bNum + float(tmp)

        # Calculate the average of foreground and background
        ma = float(fNum / fGround)
        mb = float(bNum / bGround)
        if t == float((ma + mb) / 2):
            print("Current Threshold is ", t)

            flag = 1
            print("T is equal to New Threshold")
            print("End of while Loop.")
            print("The Threshold for this image is ", t)

        else:
            t = float((ma + mb) / 2.0)
            print("Current Threshold is ", t)
            print("T is not equal, new T set")
    return t


img = cv2.imread("bldng.PNG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
t = np.mean(img)
ret2, r3 = cv2.threshold(img, 1, 255, cv2.THRESH_OTSU)
print("The OTSU Method yields a results of ", r3)

threshold = interactiveThresholding(img)
