import numpy as np

# 1. Memory optimization
# Task: Reduce memory for a dataset of 1 million integers (range 0-100)
# Default int64 (8 bytes) vs int8 (1 byte)
data = np.arange(1000000)

# Optimization 1: Downcasting dtypes
arr_optimized = np.array(data, dtype=np.int8) 

# Optimization 2: In-place operations (avoids temporary array copies)
# Instead of: arr = arr * 2 (creates a new array)
np.multiply(arr_optimized, 2, out=arr_optimized) 

print(f"Default Memory: {data.nbytes / 1024:.2f} KB")
print(f"Optimized Memory: {arr_optimized.nbytes / 1024:.2f} KB") # ~87.5% reduction

# 2. String operations
# Task: Clean a list of names and check for numeric codes
names = np.array(['  Alice ', 'BOB', '123_Code', '  Charlie '])

# Remove whitespace and convert to title case
clean_names = np.char.title(np.char.strip(names))

# Identify strings that contain only numbers
is_numeric = np.char.isnumeric(clean_names)

print(f"Cleaned Names: {clean_names}")
print(f"Is Numeric Mask: {is_numeric}")

# 3. Contiguous array
# Task: Compare row-major (C) vs column-major (F) layouts
c_arr = np.ones((1000, 1000), order='C') # Row-major
f_arr = np.ones((1000, 1000), order='F') # Column-major

# Check flags
print(f"C-Contiguous: {c_arr.flags['C_CONTIGUOUS']}")
print(f"F-Contiguous: {f_arr.flags['F_CONTIGUOUS']}")


