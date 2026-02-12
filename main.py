import matplotlib.pyplot as plt
import sys

def plotData(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        x = []
        y = []
        for line in lines[38:]:
            data = line.split()
            if len(data) == 2:
                x.append(float(data[0]))
                y.append(float(data[1]))
    plt.plot(x, y)


    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Data from File')

    plt.grid()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python help.py <filename>")
        sys.exit(1)
    filename = sys.argv[1] + ".txt"
    plotData(filename)



# def validateFile(filename):

# def validateFileName(filename):




