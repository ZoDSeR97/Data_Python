"""
    Given a budget and two spending options price
    Plot a graph to illustrate spending possibility
    Input:
        [list of possible budget] 
        [name and price of option A]
        [name and price of option B]
"""
import sys
import re
import matplotlib.pyplot as plt

def main(argv: list):
    coordinates = []
    for i in argv[0]:
        coordinates.append([float(i)/float(argv[1][1]), 0])
        coordinates.append([0, float(i)/float(argv[2][1])])
    for i in range(len(coordinates)//2):
        plt.plot(coordinates.pop(0), coordinates.pop(0), label=f"budget contraints {i+1}")
    plt.xlabel(args[1][0])
    plt.ylabel(args[2][0])
    plt.legend()
    plt.title('Budget Constraint')
    plt.show()

if __name__ == "__main__":
    argv, args = sys.argv, []
    if re.search(".py", argv[0]):
        argv = sys.argv[1::]
        print(argv)
    if len(argv) != 3:
        print("Missing argument!!!")
        print("Enter 3 list: budget, option A name and price, option B name and price")
        print("Example: [500,300] [Bus_trips,30] [Train_Trips,150]")
        print("Note space is only used for separate input")
    else:
        for i in argv:
            args.append(list(map(str, re.sub("[\[+\] \,]", ' ', i).split())))
        main(args)
