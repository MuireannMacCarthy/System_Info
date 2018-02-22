'''
Created on 22 February 2018

@author: mmacc
'''
import platform


def get_platform():
    s = "the platform is  " + platform.platform()
    return s

if __name__ == '__main__':
    print(get_platform())