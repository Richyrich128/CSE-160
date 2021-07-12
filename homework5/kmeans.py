import os
import math
from utils import converged, plot_2d, plot_centroids, read_data, \
    load_centroids, write_centroids_tofile
import matplotlib.pyplot as plt


# problem for students
def euclidean_distance(dp1, dp2):
    """Calculate the Euclidean distance between two data points.

    Arguments:
        dp1: a list of floats representing a data point
        dp2: a list of floats representing a data point

    Returns: the Euclidean distance between two data points
    """
    inside = 0.0
    length = len(dp1)
    for i in range(length):
        inside += (dp2[i] - dp1[i])**2
    return math.sqrt(inside)


# problem for students
def assign_data(data_point, centroids):
    """Assign a single data point to the closest centroid. You should use
    the euclidean_distance function (that you previously implemented).

    Arguments:
        data_point: a list of floats representing a data point
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a string as the key name of the closest centroid to the data point
    """
    centroid = list(centroids.keys())[0]
    for i in centroids.keys():
        if euclidean_distance(centroids[i], data_point) \
           < euclidean_distance(centroids.get(centroid), data_point):

            centroid = i
    return centroid


# problem for students
def update_assignment(data, centroids):
    """Assign all data points to the closest centroids. You should use
    the assign_data function (that you previously implemented).

    Arguments:
        data: a list of lists representing all data points
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary.
    """
    dic = dict()
    for i in data:
        if assign_data(i, centroids) not in dic.keys():
            dic.setdefault(assign_data(i, centroids), [])
        dic[assign_data(i, centroids)].append(i)
    return dic


# problem for students
def mean_of_points(data):
    """Calculate the mean of a given group of data points. You should NOT
    hard-code the dimensionality of the data points).

    Arguments:
        data: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points
    """
    mean = [0]*len(data[0])
    for i in range(len(data)):
        for j in range(len(data[0])):
            mean[j] += data[i][j]
    for k in range(len(mean)):
        mean[k] = mean[k] / len(data)
    return mean


# problem for students
def update_centroids(assignment_dict):
    """Update centroid locations as the mean of all data points that belong
    to the cluster. You should use the mean_of_points function (that you
    previously implemented).

    Arguments:
        assignment_dict: the dictionary returned by update_assignment function

    Returns: A new dictionary representing the updated centroids
    """
    new_dict = dict()
    for each in assignment_dict.keys():
        new_dict[each] = mean_of_points(assignment_dict.get(each))
    return new_dict


def main_2d(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        # plot centroid
        fig = plot_2d(assignment_dict, centroids)
        plt.title(f"step{step}")
        fig.savefig(os.path.join("results", "2D", f"step{step}.png"))
        plt.clf()
        step += 1
    print(f"K-means converged after {step} steps.")
    return centroids


def main_mnist(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    # plot initial centroids
    plot_centroids(centroids, "init")
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1
    print(f"K-means converged after {step} steps.")
    # plot final centroids
    plot_centroids(centroids, "final")
    return centroids


if __name__ == '__main__':
    data, label = read_data("data/mnist.csv")
    init_c = load_centroids("data/mnist_init_centroids.csv")
    final_c = main_mnist(data, init_c)
    write_centroids_tofile("mnist_final_centroids.csv", final_c)
