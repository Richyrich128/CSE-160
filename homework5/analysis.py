from kmeans import assign_data
from utils import load_centroids, read_data


def update_assignment(data, labels, centroids):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.
    """
    dic = dict()
    num = 0
    for i in data:
        if assign_data(i, centroids) not in dic.keys():
            dic.setdefault(assign_data(i, centroids), [])
        dic[assign_data(i, centroids)].append(labels[num])
        num += 1
    return dic


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list
    """
    label_count = dict()
    for num in labels:
        if num in label_count.keys():
            label_count[num] += 1
        else:
            label_count[num] = 1
    biggest = sorted(list(label_count.values()))

    return biggest[-1]


def accuracy(data, labels, centroids):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a float representing the accuracy of the algorithm
    """
    dic = update_assignment(data, labels, centroids)
    sum_majority_labels = 0.0
    total_num_of_labels = 0.0
    for each in dic.values():
        sum_majority_labels += majority_count(each)
        total_num_of_labels += len(each)
    return (sum_majority_labels / total_num_of_labels)


if __name__ == '__main__':
    centroids = load_centroids("mnist_final_centroids.csv")
    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))

# LEAVE YOUR ANSWERS HERE...
# 1. What happened to the centroids? Why are there fewer than 10?
# I think some just werent put into the dictionary because they weren't
# close enough to some points. THat would reduce the number of centroids
# 2. What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?
# I got 0.582 accuracy. I dount really get the second part of the question
