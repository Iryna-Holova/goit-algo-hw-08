import heapq


def connect_cables(cables: list) -> tuple:
    """
    Connects the given list of cables with the least cost.

    Args:
        cables (list): List of cables to connect.

    Returns:
        tuple: The total cost of the connection and the length of the final
        cable.
    """
    heapq.heapify(cables)
    cost = 0
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        new_cable = cable1 + cable2
        cost += new_cable
        heapq.heappush(cables, new_cable)
    return cost, cables[0]


def main() -> None:
    """
    Main function.
    """
    while True:
        try:
            cables = list(map(int, input("Enter cable lengths: ").split()))
            break
        except ValueError:
            print("Invalid input. Please enter a list of integers separated by"
                  " spaces.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            exit(1)

    print("Cables:", cables)
    print("Connecting cables...")
    cost, length = connect_cables(cables)
    print("Minimum cost:", cost)
    print("Final cable length:", length)


if __name__ == "__main__":
    main()
