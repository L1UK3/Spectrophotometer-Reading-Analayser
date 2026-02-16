import matplotlib.pyplot as plt

def retrieveData(filename):

    with open(filename, "r") as file:
        lines = file.readlines()
        x = []
        y = []

        for line in lines[::-1]:
            data = line.split()

            if len(data) == 2:
                print(data)
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




