import random

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QSizePolicy
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from sklearn import cluster
import numpy as np


class MyFigureCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100, method="Not selected"):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        # We want the axes cleared every time plot() is called
        # self.axes.hold(False)

        # self.build(method)

        self.canvas = FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def period(x):
        return {
            0: '0.5 months',
            1: '1 month',
            2: '3 months',
            3: '24 months',
        }[x]


    def rebuildKMeans(self):
            # Import Data
            datfile = r'TablData01.txt'
            data = np.loadtxt(datfile)

            # Using K-Means method

            k = 4  # Presumed number of clusters
            column = 3;  # Period of time/number of column (0 - 0.5months ; 1 - 1month ; 2 - 3months ; 3 - 24months)

            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_

            for i in range(k):
                # select only data observations with cluster label == i
                ds = data[np.where(labels == i)]
                # plot the data observations
                self.axes.plot(ds[:, 0], ds[:, 1], 'o')
                # plot the centroids
                lines = self.axes.plot(centroids[i, column], centroids[i, column + 4], 'kx')
                # make the centroid x's bigger
                pyplot.setp(lines, ms=15.0)
                pyplot.setp(lines, mew=2.0)
            pyplot.xlabel('Skin fibroblasts')
            pyplot.ylabel('Lungs fibroblasts')
            pyplot.title('K-Mean method for ' + MyFigureCanvas.period(column) + ' with k = ' + str(k))
            self.draw()


