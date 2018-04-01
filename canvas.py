from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from sklearn.cluster import AffinityPropagation, DBSCAN, KMeans
from sklearn.decomposition import PCA


class MyFigureCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.canvas = FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def KMeans(self, NumberOfClusters, filePath):
        # Import Data
        datfile = filePath
        df = pd.read_csv(filePath, sep='\t', header=None)
        X = np.array(df)
        # Normalization Data
        labels = X[:, 0];
        X = X[::, 1:X.size];
        print(X)
        print(labels)
        mX = np.max(X, axis=0)
        X = X / mX;

        # Using K-Means method
        k = int(NumberOfClusters)  # Presumed number of clusters
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_

        # We will project the data into 2 main components
        pca = PCA(n_components=2)
        Xt = pca.fit_transform(X)

        self.axes.cla()

        for i in range(k):
            # select only data observations with cluster label == i
            ds = Xt[np.where(labels == i)]
            # plot the data observations
            self.axes.plot(ds[:, 0], ds[:, 1], 'o')
            # plot the centroids
            self.axes.plot(centroids[i, 0], centroids[i, 1], 'kx')
        self.draw()

    def DBSCAN(self, eps_row, min_samples_row, filePath):
        # Import Data
        datfile = filePath
        X = np.loadtxt(datfile)
        # Normalization Data
        mX = np.max(X, axis=0)
        X = X / mX;

        # Compute DBSCAN
        db = DBSCAN(float(eps_row), int(min_samples_row)).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

        ##############################################################################
        # We will project the data into 2 main components
        pca = PCA(n_components=2)
        Xt = pca.fit_transform(X)

        # #############################################################################
        # Plot result
        self.axes.cla()
        # Black removed and is used for noise instead.
        unique_labels = set(labels)
        colors = [plt.cm.Spectral(each)
                  for each in np.linspace(0, 1, len(unique_labels))]
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = [0, 0, 0, 1]
            class_member_mask = (labels == k)
            xy = Xt[class_member_mask & core_samples_mask]
            self.axes.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                           markeredgecolor='k', markersize=14)
            xy = Xt[class_member_mask & ~core_samples_mask]
            self.axes.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                           markeredgecolor='k', markersize=6)
        # self.axes.title('Estimated number of clusters: %d' % n_clusters_)

        self.draw()

    def AffinityPropagation(self, filePath):

        # Import Data
        datfile = filePath
        X = np.loadtxt(datfile)

        ##############################################################################
        # Compute similarities
        X_norms = np.sum(X ** 2, axis=1)
        S = - X_norms[:, np.newaxis] - X_norms[np.newaxis, :] + 2 * np.dot(X, X.T)

        ##############################################################################
        # Compute Affinity Propagation
        af = AffinityPropagation().fit(S)
        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_
        n_clusters_ = len(cluster_centers_indices)

        ##############################################################################
        # We will project the data into 2 main components
        pca = PCA(n_components=2)
        Xt = pca.fit_transform(X)

        ##############################################################################
        # Plot result
        self.axes.cla()
        pl.close('all')
        pl.figure(1)
        pl.clf()

        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            class_members = labels == k
            cluster_center = Xt[cluster_centers_indices[k]]
            self.axes.plot(Xt[class_members, 0], Xt[class_members, 1], col + '.')
            self.axes.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                           markeredgecolor='k', markersize=10)
            for x in Xt[class_members]:
                self.axes.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

        self.draw()
        # pl.title('Estimated number of clusters: %d' % n_clusters_)
