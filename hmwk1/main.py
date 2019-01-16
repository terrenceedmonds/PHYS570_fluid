import numpy as np
import matplotlib.pyplot as plt

def atmosphere():
    T = 300
    R = 8.314
    gamma = 7/5
    g = 9.81
    mu = 28.97*np.power(10.0,-3)

    scale_height = R*T/(g*mu)

    print(scale_height)

    z = np.linspace(start=0,stop=10000,num=10001)



    press_iso = np.exp(-z/scale_height)

    press_adi = np.exp(-z/(scale_height*gamma))

    #print(press_iso)


    plt.plot(z,press_iso)
    plt.plot(z,press_adi)
    plt.savefig('atmosphere.pdf')
    plt.show()

    return

atmosphere()