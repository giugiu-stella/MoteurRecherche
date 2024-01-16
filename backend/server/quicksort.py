# Function to find the partition position
def partition(nodes, low, high):
	pivot = nodes[high].json["download_count"]

	i = low - 1

	for j in range(low, high):
		if nodes[j].json["download_count"] <= pivot:
			i = i + 1

			(nodes[i], nodes[j]) = (nodes[j], nodes[i])

	
	(nodes[i + 1], nodes[high]) = (nodes[high], nodes[i + 1])

	return i + 1


def quicksort(nodes, low, high):
	if low < high:
		pivot_indice = partition(nodes, low, high)
		quicksort(nodes, low, pivot_indice - 1)
		quicksort(nodes, pivot_indice + 1, high)

