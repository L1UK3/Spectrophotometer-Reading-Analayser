
"""Spectrometer data plotting script

Initial python script to read data from the file and plot it using matplotlib.

This script assumes 'filename' is a text file where each line contains two numbers 
(x and y values) separated by whitespace.
The script reads the data, stores it in two lists, and then plots it using matplotlib.

This script requires the matplotlib library to be installed. 
You can install it using pip if you don't have it already:
pip install matplotlib

This file can be imported as a module and contains the following functions:
- retrieveData: Reads data from a file and returns two lists of x and y values.
"""

import matplotlib.pyplot as plt

def retrieveData(filename: str) -> tuple[list[float], list[float]]:
    """Opens a file, reads its contents, and extracts x and y values from it. 
    The function expects each line of the file to contain two numbers 
    (x and y) separated by whitespace. 
    
    :param filename: The name of the file to read data from in the active directory.
    :type filename: str
    
    :returns: A tuple containing two lists of floats: the first list contains x values and the second list contains y values.
    :rtype: tuple[list[float], list[float]]
    
    """

    with open(filename, "r") as file:
        lines = file.readlines()
        x = []
        y = []

        for line in lines[::-1]:
            data = line.split()

            if len(data) == 2:
                print(data) # Just for testing
                try:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
                except ValueError:
                    return (x, y)
        
        return (x, y)
                
if __name__ == "__main__":
    coorinates = retrieveData("test.TXT")
    plt.plot(coorinates[0], coorinates[1])
    plt.grid()
    plt.show()
