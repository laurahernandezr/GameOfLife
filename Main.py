import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
ON = 1
OFF = 0


def new_generation(frame_num, img, grid, N):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # mod used to calculate the toroidal shape, add values to get the total around for every single square
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]))
            # Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    # update data
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


def main():
    N = 100
    on_probability = 0.2
    off_probability = 0.8
    # Create an initial grid with random values but set probabilities
    grid = np.random.choice([ON, OFF], N * N, p=[on_probability, off_probability]).reshape(N, N)
    # set up the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, new_generation, fargs=(img, grid, N,),
                                  frames=10,
                                  interval=100,
                                  save_count=50)

    plt.show()


if __name__ == '__main__':
    main()
