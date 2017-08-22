from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from sklearn import cluster
import numpy as np


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

    def period(x):
        return {
            0: '0.5 months',
            1: '1 month',
            2: '3 months',
            3: '24 months',
        }[x]

    def rebuildKMeans(self, NumberOfClusters, xAxisRaw, yAxisRaw, normalizationStatus, filePath):
        # Import Data
        datfile = filePath
        data = np.loadtxt(datfile)
        if normalizationStatus :
            mData = np.max(data, axis=0)
            data = data / mData;
        # Using K-Means method
        k = int(NumberOfClusters)  # Presumed number of clusters
        xAxis = int(xAxisRaw) - 1
        yAxis = int(yAxisRaw) - 1
        kmeans = cluster.KMeans(n_clusters=k)
        kmeans.fit(data)
        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_
        self.axes.cla()
        for i in range(k):
            # select only data observations with cluster label == i
            ds = data[np.where(labels == i)]
            # plot the data observations
            self.axes.plot(ds[:, 0], ds[:, 1], 'o')
            # plot the centroids
            self.axes.plot(centroids[i, xAxis], centroids[i, yAxis], 'kx')


        # self.axes.set_xlabel(xAxisRaw + ' column')
        # self.axes.set_ylabel(yAxisRaw + ' column')
        # self.axes.set_title('K-Means method for ' + xAxisRaw + ' and ' + yAxisRaw + ' columns' + ' and  with ' + str(k) + ' clusters')
        self.draw()

