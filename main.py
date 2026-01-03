# Завдання 1
import numpy as np

print("Завдання 1")
arr = np.array([10, 20])

print('Масив', arr)
print('Сума', np.sum(arr))
print('Середнє', np.mean(arr))
print('Мінімальне', np.min(arr))
print('Маскимальне', np.max(arr))


# Завдання 2
print("Завдання 2")
arr = np.random.rand(1000)

print("Сума", arr.sum())
print("Середнє", arr.mean())
print("Мінімум", arr.min())
print("Максимум", arr.max())

# Завдання 3
print("Завдання 3")
arr = np.random.randint(0, 100, size=(5, 5))

print("Масив\n", arr)
second_column = arr[:, 1]
print("Другий стовпець", second_column)
second_row = arr[1, :]
print("Другий рядок", second_row)
flattend = arr.flatten()
print("Flatten", flattend)

# Завдання 4
print("Завдання 4")
arr = np.random.rand(500_000)

print("Сума", arr.sum())
print("Середнє", arr.mean())
print("Мінімум", arr.min())
print("Максимум", arr.max())
