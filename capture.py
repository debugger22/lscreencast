import time
import numpy
import pickle
import pyscreenshot

def capture(number):
    #pyscreenshot.grab_to_file("temp/temp"+`number`+".png")
    i = pyscreenshot.grab()
    f = open("temp/temp"+`number`+".png","w")
    f.write(numpy.asarray(i))


if __name__ == '__main__':
    a = time.time()
    for i in range(30):
        capture(i)
    print time.time() - a
