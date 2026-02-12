import matplotlib.pyplot as plt
import sys

def plotData(filename):

    xLabel = "X-axis"
    yLabel = "Y-axis"

    with open(filename, "r") as file:
        lines = file.readlines()
        x = []
        y = []

        for line in lines[::-1]:
            data = line.split()

            if len(data) == 2:
                try:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
                except ValueError:
                    continue


    plt.plot(x, y)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(filename)

    plt.grid()
    plt.show()


# def validateFile(filename):

# def validateFileName(filename):


"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python help.py <filename>")
        sys.exit(1)
    filename = sys.argv[1] + ".txt"
    plotData(filename)
"""




plotData("files/blank_02-02.txt")

