from sklearn import datasets
from sklearn.svm import SVC
from image2array import img2array

# Loading Data
digits = datasets.load_digits()
# Extracting data from data set
features = digits.data
# Extracting output corresponding to data set
labels = digits.target

# Training
clf = SVC(gamma=0.001)
clf.fit(features, labels)

# Converting image to array
x_test = img2array("images_test/1.jpg", digits.images.dtype)

# Predicting output from our Trained Classifier
print(clf.predict([x_test]))

