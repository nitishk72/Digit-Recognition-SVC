from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc


def img2array(image):
    # Reading image
    img = misc.imread(image)
    # Resizing image to 8 * 8 = 64
    img = misc.imresize(img, (8, 8))
    # Updating type from unsigned int 8 to signed float 64
    img = img.astype(digits.images.dtype)
    # We have data set image of integer pixels in the range 0..16.
    img = misc.bytescale(img, high=16, low=0)

    array = []
    # Converting out 3D array to 1D Array
    for each_row in img:
        for each_pixel in each_row:
            array.append(((sum(each_pixel)) / 3.0))

    return array


# Loading Data
digits = datasets.load_digits()
# Extracting data from data set
features = digits.data
# Extracting output corresponding to data set
labels = digits.target

# Training
clf = SVC(gamma=0.001)
clf.fit(features, labels)

x_test = img2array("images_test/.jpg")

# Predicting output from our Trained Classifier
print(clf.predict([x_test]))


# Digit-Recognition-SVC


