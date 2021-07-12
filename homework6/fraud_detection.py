import matplotlib.pyplot as plt
import random
import csv


def extract_election_vote_counts(filename, column_names):
    votes_csv = open(filename)
    in_file = csv.DictReader(votes_csv)
    votes = []
    for line in in_file:
        for key in column_names:
            vote = line[key].replace(",", "")

            votes.append(int(vote))
    return votes
    votes_csv.close()


def ones_and_tens_digit_histogram(numbers):
    li = list(range(10))
    counts = dict()
    frequency = []
    for i in li:
        counts.setdefault(i, 0)
    for k in range(2):
        for i in range(len(numbers)):
            counts[numbers[i] % 10] += 1
            numbers[i] = int(numbers[i] / 10)
    for key in counts.keys():
        frequency.append(counts[key] / (len(numbers) * 2.0))
    return frequency


def plot_iranian_least_digits_histogram(histogram):
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    x = list(range(10))
    ideal = [0.1] * 10
    y = histogram
    plt.plot(x, ideal, color='blue', label='ideal')
    plt.plot(x, y, color='orange', label='iran')
    plt.savefig("iran-digits.png")
    plt.legend(loc='upper left')
    plt.title('Distribution of last two digits in Iranian dataset')
    plt.show()

    plt.plot(x, y)
    return None


def plot_distribution_by_sample_size():
    sizes = [0, 10, 50, 100, 1000, 10000]
    lines = dict()
    for k in range(1, 6):
        lines.setdefault(k, [])

    for i in range(1, 6):
        for j in range(sizes[i]):
            lines[i].append(random.randint(0, 99))
    histograms = dict()
    # key should be a number
    for each in lines.keys():
        histograms[each] = ones_and_tens_digit_histogram(lines[each])
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    x = list(range(10))
    ideal = [0.1] * 10

    plt.plot(x, ideal, color='blue', label='ideal')
    plt.plot(x, histograms[1], color='orange', label='10 random numbers')
    plt.plot(x, histograms[2], label='50 random numbers')
    plt.plot(x, histograms[3], label='100 random numbers')
    plt.plot(x, histograms[4], label='1000 random numbers')
    plt.plot(x, histograms[5], label='10000 random numbers')
    plt.savefig("random-digits.png")
    plt.legend(loc='best')
    plt.title('Distribution of last two digits in randomly generated samples')
    plt.show()
    return None


"""
The code in this function is executed when this file is run as a Python
program.0
"""


def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    k = extract_election_vote_counts("election-iran-2009.csv",
                ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    j = ones_and_tens_digit_histogram(k)
    plot_iranian_least_digits_histogram(j)
    plot_distribution_by_sample_size()


if __name__ == "__main__":
    main()
