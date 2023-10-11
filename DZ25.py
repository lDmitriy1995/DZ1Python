class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_treasure_path(root):
    if not root:
        return (0, [])

    left_sum, left_path = find_max_treasure_path(root.left)
    right_sum, right_path = find_max_treasure_path(root.right)

    if left_sum > right_sum:
        return (left_sum + root.value, [root.value] + left_path)
    else:
        return (right_sum + root.value, [root.value] + right_path)

# Пример использования
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

max_sum, path = find_max_treasure_path(root)
print("Максимальная сумма:", max_sum)
print("Путь:", " -> ".join(map(str, path)))
