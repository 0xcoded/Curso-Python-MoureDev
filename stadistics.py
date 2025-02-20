def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]