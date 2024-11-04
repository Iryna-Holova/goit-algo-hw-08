import heapq


def merge_k_lists(lists: list) -> list:
    """
    Merges k sorted lists into one sorted list using a min heap.

    Args:
        lists (list of list of int): A list of sorted lists to merge.

    Returns:
        list: A single merged sorted list.
    """
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))
    result = []
    while heap:
        value, i, j = heapq.heappop(heap)
        result.append(value)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return result


# Example usage
if __name__ == "__main__":
    lists_test = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists_test)
    print("Merged list:", merged_list)
