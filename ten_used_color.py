import numpy as np
# import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from PIL import Image

# Openning Image
img = Image.open('static/img/sample.jpg')

# color_dict = {}  # initial color list
# sorted_dict = {}  # initial sorted color list


def ten_color(img):

    color_dict = {}  # initial color list
    sorted_dict = {}  # initial sorted color list
    # Converting image to numpy array
    n_img = np.asarray(img)
    # print(n_img)
    # Converting numpy array to 0->1 value array for color conversion
    f_n_img = n_img / 255

    # iterating through whole array and converting rgb colors to hex
    # and storing color counts to color_dict
    for i in range(f_n_img.shape[0]):
        for j in range(f_n_img.shape[1]):
            c = (f_n_img[i, j, 0], f_n_img[i, j, 1], f_n_img[i, j, 2])
            h_color = rgb2hex(c)
            if h_color in color_dict.keys():
                color_dict[h_color] = color_dict[h_color] + 1
            else:
                color_dict[h_color] = 1

    # sorting based on color counts
    sorted_keys = sorted(color_dict, key=color_dict.get, reverse=True)

    # calling hex code colors based on sorted aounts and storing in sorted_dict
    for w in sorted_keys[:10]:
        sorted_dict[w] = color_dict[w]

    return sorted_dict
# print(sorted_dict)
# print(f_n_img[0,0,:])
# print(n_img.shape)
# print(n_img.ndim)
# print(n_img[1][0])
# i_hex = rgb2hex((1,1,1))


# print(i_hex)
if __name__ == '__main__':
    print(ten_color(img))
