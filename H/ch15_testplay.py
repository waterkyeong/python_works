import matplotlib.pyplot as plt

from ch15_play import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, edgecolors='none', s=1)
    ax.set_aspect('equal')
    
    ax.scatter(0,0,c='Pink', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolor='none',s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_runnig = input("make another?: ")
    if keep_runnig == 'n':
        break