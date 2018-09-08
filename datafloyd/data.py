import matplotlib.pyplot as plt
import numpy as np


def generate_noisy_line(a=0.5, b=5, y_noise=5, random_seed=[], x=np.linspace(-10, 50, 100)):
    """
    generates line y=ax+b and adds noise based on y and x
    :param a: "a" parameter of the line
    :param b: "b" parameter of the line
    :param y_noise: y noise
    :param random_seed: random seed
    :param x: x values
    :return: x,y

    """
    if(random_seed):
        # Hep aynı değerleri oluşturması için seed değerini sabitleyelim
        np.random.seed(42)
    else:
        pass

    # y noktaları lineer bir doğrunun üzerine rastgele gürültü eklenmesi ile
    y = (a * x + b) + np.random.rand(len(x)) * y_noise

    return x,y