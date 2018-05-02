from scipy import misc


def img2array(image, type):
    # Reading image
    img = misc.imread(image)
    # Resizing image to 8 * 8 = 64
    img = misc.imresize(img, (8, 8))
    # Updating type from unsigned int 8 to signed float 64
    img = img.astype(type)
    # We have data set image of integer pixels in the range 0..16.
    img = misc.bytescale(img, high=16, low=0)

    array = []
    # Converting out 3D array to 1D Array
    for each_row in img:
        for each_pixel in each_row:
            array.append(((sum(each_pixel)) / 3.0))

    return array

