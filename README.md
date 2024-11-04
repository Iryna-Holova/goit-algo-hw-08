# Heap Assignments

This repository contains solutions to two assignments related to heaps and their applications in Python. The tasks involve optimizing costs with minimal heap operations and efficiently merging sorted lists.

## Table of Contents

- [Task 1: Minimum Cost Cable Connection](#task-1-minimum-cost-cable-connection)
- [Task 2: Merging k Sorted Lists](#task-2-merging-k-sorted-lists)
- [How to Run](#how-to-run)
- [Requirements](#requirements)

## Task 1: Minimum Cost Cable Connection

The goal is to find the minimal cost required to connect a series of cables of varying lengths. Each connection costs a sum of the lengths of the two cables being connected, and the task is to determine the order that minimizes total connection cost.

- **Solution Approach**: We use a min-heap to repeatedly merge the two shortest cables, keeping the total cost as low as possible.
- **Functions**:
  - `connect_cables(cables: list) -> tuple`: Takes a list of cable lengths and returns the minimum connection cost and the length of the final combined cable.

### Example usage

```bash
python task_1.py
Enter cable lengths: 5 10 1 20 100 15 3 10 5 1 2 1 1
Cables: [5, 10, 1, 20, 100, 15, 3, 10, 5, 1, 2, 1, 1]
Connecting cables...
Minimum cost: 393
Final cable length: 174
```

## Assignment 2: Merging k Sorted Lists

The task is to merge `k` sorted lists into a single sorted list in an efficient manner. This is done using a min-heap to keep track of the smallest current element across all lists.

- **Solution Approach**: By using a min-heap, we maintain efficient access to the smallest element from the lists, ensuring a sorted merge.
- **Functions**:
  - `merge_k_lists(lists: list) -> list`: Takes a list of sorted lists and returns a single merged sorted list.

### Example usage

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Merged list:", merged_list)  # Output: Merged list: [1, 1, 2, 3, 4, 4, 5, 6]
```

## How to Run

1. Clone the repository and navigate to the directory.
2. Run the following command in the terminal:

```bash
python <filename>.py
```

Replace `<filename>` with the script name for each task.

## Requirements

- Python 3.6 or higher.
- `heapq` module (standard in Python).

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
