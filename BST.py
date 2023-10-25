# Python code to implement the iterative approach

# Definition of a BST node


class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Function to insert a new node in BST


def insert(root, key):
	# If the tree is empty, return a new node
	if root is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < root.data:
		root.left = insert(root.left, key)
	elif key > root.data:
		root.right = insert(root.right, key)

	# Return the (unchanged) node pointer
	return root

# Function to find the k-th smallest
# element in BST


def kthSmallest(root, k):
	# Create an empty stack
	stack = []

	# Loop until stack is empty or
	# k becomes zero
	while root is not None or len(stack) > 0:

		# Push all the left subtree
		# nodes onto the stack
		while root is not None:
			stack.append(root)
			root = root.left

		# Pop the top node from the
		# stack and check if it is
		# the k-th element
		root = stack.pop()
		k -= 1

		if k == 0:
			return root.data

		# Set root to the right child
		# and continue with the traversal
		root = root.right

	# If k is greater than the number
	# of nodes in BST, return -1
	return -1


# Driver Code
if __name__ == '__main__':
	root = None
	keys = [20, 8, 22, 4, 12, 10, 14]

	# Insert all the keys into BST
	for x in keys:
		root = insert(root, x)

	k = 4

	# Find the k-th smallest element in BST
	kth_smallest = kthSmallest(root, k)
	if kth_smallest != -1:
		print("K-th smallest element in BST is:", kth_smallest)
	else:
		print("Invalid input")
