import time
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker  # Import the ticker module
import numpy as np


def calculate_histogram(no_tries, no_teams, no_advancing_teams, round_no):
    # Declaring and assigning vars
    t0 = time.time()
    max_points = no_teams*2
    points = np.arange(1, max_points + 1)
    last_place_to_advance = no_teams - no_advancing_teams

    hist_plot = np.zeros(max_points * 2 + 1, dtype=float)
    hist_cumulative = np.zeros(max_points * 2 + 1, dtype=float)

    # Simulate the lowest points needed to advance and count via hist_plot list
    for _ in range(no_tries):
        np.random.shuffle(points)
        points_team_list = points[::2] + points[1::2]
        points_team_list.sort()
        hist_plot[points_team_list[last_place_to_advance - 1]] += 1

    # Translate to percentages and fill cumulative histogram
    for i in range(max_points*2 + 1):
        hist_plot[i] = hist_plot[i] / no_tries * 100
        hist_cumulative[i] = sum(hist_plot[:i + 1])

    # Get non-zero indexes for better plotting
    non_zero_indexes = np.nonzero(hist_plot)[0]

    # Make plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.bar(non_zero_indexes + 1, hist_plot[non_zero_indexes])
    ax1.set_title('histogram')
    ax1.set_xlabel('points')
    ax1.set_ylabel('frequency of lowest points needed to advance')

    ax2.bar(non_zero_indexes + 1, hist_cumulative[non_zero_indexes], color='orange')
    ax2.set_title("cumulative_probability's")
    ax2.set_xlabel('points')
    ax2.set_ylabel('probability to advance')  # Update the y-axis label

    # Add main title
    main_title = f"Round {round_no}"
    fig.suptitle(main_title, fontsize=16)

    # Set y-axis formatter to show percentages
    ax1.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))

    plt.tight_layout()

    # Save the plot to a PNG file with high DPI
    plt.savefig(f'histograms_round_{round_no}_{no_tries}_tries.png', dpi=300)

    # Print time needed for sim
    t1 = time.time()
    print(f"Round {round_no} done. Total Time: {t1 - t0} s")


def main():
    no_tries = 10 ** 7
    calculate_histogram(no_tries, 20, 14, 1)
    calculate_histogram(no_tries, 14, 11, 2)
    calculate_histogram(no_tries, 11, 7, 3)
    calculate_histogram(no_tries, 7, 4, 4)


if __name__ == '__main__':
    main()
