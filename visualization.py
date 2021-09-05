import matplotlib.pyplot as plt
import sys



def main(filename):
    #labels = 'power', 'water'
    sizes = [40, 60]
    explode = (0, 0.1)
    # can be more specific with colours
    colours = ['orange', 'blue']
    # Note: sizes and labels will be added separately in CSS
    plt.pie(sizes, explode=explode, colors=colours, shadow=True)
    plt.savefig(filename, transparent=True)
    plt.show()

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f"Usage: {sys.argv[0]} filename_of_result_image")