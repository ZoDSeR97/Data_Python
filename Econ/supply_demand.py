"""
    Given 3 list of price, demand, supply
    Plot a graph to illustrate supply and demand graph
    Input:
        [list of price point] 
        [list of supply at each price point]
        [list of demand at each price point]
"""
import sys
import re
import matplotlib.pyplot as plt

def main(argv: list):
    plt.plot(argv[1], argv[0], label=f"Supply")
    plt.plot(argv[2], argv[0], label=f"Demand")
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.legend()
    plt.title('Supply & Demand')
    plt.show()

if __name__ == "__main__":
    argv, args = sys.argv, []
    if re.search(".py", argv[0]):
        argv = sys.argv[1::]
        print(argv)
    
    if len(argv) != 3:
        print("Missing argument!!!")
        print("Enter 3 list: budget, supply quantity, demand quantity")
        print("Example: [10,20,30,40,50] [0,20,40,60,80] [80,60,40,20,0]")
        print("Note space is only used for separate input")
    else:
        for i in argv:
            args.append(list(map(str, re.sub("[\[+\] \,]", ' ', i).split())))
        if len(args[0]) != len(args[1]) != len(args[3]):
            print("Missing data!!!")
        else:
            main(args)
