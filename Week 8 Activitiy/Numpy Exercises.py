import numpy as np

print("\n" + "="*40)
print("         NumPy Exercises")
print("="*40)

# 1. Import NumPy
print("\n✅ 1. Importing NumPy")
import numpy as np

# 2. Create an array of 10 zeros
print("\n✅ 2. Create an array of 10 zeros:")
arr_zeros = np.zeros(10)
print(arr_zeros)

# 3. Create an array of 10 ones
print("\n✅ 3. Create an array of 10 ones:")
arr_ones = np.ones(10)
print(arr_ones)

# 4. Create an array of 10 fives
print("\n✅ 4. Create an array of 10 fives:")
arr_fives = np.full(10, 5)
print(arr_fives)

# 5. Create an array of integers from 10 to 50
print("\n✅ 5. Create an array of integers from 10 to 50:")
arr_range = np.arange(10, 51)
print(arr_range)

# 6. Create an array of even integers from 10 to 50
print("\n✅ 6. Create an array of all even integers from 10 to 50:")
arr_even = np.arange(10, 51, 2)
print(arr_even)

# 7. Create a 3x3 matrix with values ranging from 0 to 8
print("\n✅ 7. Create a 3x3 matrix with values ranging from 0 to 8:")
arr_matrix = np.arange(9).reshape(3, 3)
print(arr_matrix)

# 8. Create a 3x3 identity matrix
print("\n✅ 8. Create a 3x3 identity matrix:")
arr_identity = np.eye(3)
print(arr_identity)

# 9. Generate a random number between 0 and 1
print("\n✅ 9. Generate a random number between 0 and 1:")
random_num = np.random.rand(1)
print(random_num)

# 10. Generate an array of 25 random numbers from a standard normal distribution
print("\n✅ 10. Generate an array of 25 random numbers (Standard Normal Distribution):")
random_array = np.random.randn(25)
print(random_array)

# 11. Create a 10x10 matrix with values from 0.01 to 1, spaced linearly
print("\n✅ 11. Create a 10x10 matrix with values from 0.01 to 1:")
arr_linspace = np.linspace(0.01, 1, 100).reshape(10, 10)
print(arr_linspace)

# 12. Create an array of 20 linearly spaced points between 0 and 1
print("\n✅ 12. Create an array of 20 linearly spaced points between 0 and 1:")
arr_linspace_20 = np.linspace(0, 1, 20)
print(arr_linspace_20)

# Matrix operations
print("\n" + "="*40)
print("        Matrix Operations")
print("="*40)

# 13. Given matrix for slicing & calculations
print("\n✅ 13. Given 5x5 matrix for operations:")
mat = np.arange(1, 26).reshape(5, 5)
print(mat)

# 14. Slice out the sub-matrix (row 3 to 5, column 2 to 5)
print("\n✅ 14. Slice out sub-matrix (row 3 to 5, column 2 to 5):")
sub_matrix = mat[2:, 1:]
print(sub_matrix)

# 15. Get the element at row index 4, column index 5
print("\n✅ 15. Get the element at row index 4, column index 5:")
element = mat[3, 4]
print(element)

# 16. Get column 2 of the matrix
print("\n✅ 16. Get column 2 of the matrix:")
column_2 = mat[:, 1:2]
print(column_2)

# 17. Get the first row of the matrix
print("\n✅ 17. Get the first row of the matrix:")
row_1 = mat[0]
print(row_1)

# 18. Sum all the values in mat
print("\n✅ 18. Sum of all values in matrix:")
sum_all = mat.sum()
print(sum_all)

# 19. Get the standard deviation of mat
print("\n✅ 19. Standard deviation of matrix:")
std_dev = mat.std()
print(std_dev)

# 20. Get the sum of each column in mat
print("\n✅ 20. Sum of each column in matrix:")
sum_columns = mat.sum(axis=0)
print(sum_columns)

print("\n" + "="*40)
print("       🎉 NumPy Exercises Completed! 🎉")
print("="*40)
