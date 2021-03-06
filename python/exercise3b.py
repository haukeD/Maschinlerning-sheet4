"""
============================
A demo of K-Means clustering 
============================

"""
print __doc__

from time import time
import numpy as np
import pylab as pl

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

np.random.seed() # an integer (e.g. 42) FIXES the seed!

# load data; NOTE: it is IMPORTANT to use FLOAT values; with INT values the result will be wrong!
data = np.array([ [2.0,10.0], [2.0,5.0], [8.0,4.0], [5.0,8.0], [7.0,5.0], [6.0,4.0], [1.0,2.0], [4.0,9.0] ] ) # training data

n_samples, n_features = data.shape

# specify parameters of kmeans
init_cluster = np.array([ [2.0,10.0], [5.0,8.0], [1.0,2.0] ]) # initialization
max_iter  = 4

print "number of features: %d" % n_features
print "number of samples: %d" % n_samples
print


# kmeans
#for i in range(1,max_iter):
kmeans = KMeans(init=init_cluster, max_iter=max_iter, n_init=1).fit(data) # (n_init=1 not necessary)

print
#print "Iteration:", i
print "cluster center: "
print kmeans.cluster_centers_
print
print "labels of training patterns: "
print kmeans.labels_
print
print "max_iter"
print kmeans.max_iter

# For plotting of the decision boundaries: define mesh
# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.set_cmap(pl.cm.Paired)
pl.pcolormesh(xx, yy, Z)

# Plot the cluster center as a white X
centroids = kmeans.cluster_centers_
pl.scatter(centroids[:, 0], centroids[:, 1],
           marker='x', s=169, linewidths=3,
           color='w')

# plot the initial cluster center 
pl.scatter(init_cluster[:, 0], init_cluster[:, 1],
           marker='o', s=169, linewidths=3,
           color='r')


#plot also the training points
pl.scatter(data[:,0], data[:,1], c=kmeans.labels_)
           
           
pl.title('K-means clustering algorithm\n'
         'Initial cluster center are marked with big red circle\n'
         'Final cluster center are marked with white cross')
pl.axis('tight')
pl.savefig('../3b.pdf')
pl.show()
