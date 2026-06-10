# ============================================================
# NumPy Basics - Complete Reference
# ============================================================

import numpy as np


def print_array_info(name, arr):
    """Utility to print common array metadata."""
    print(f"  Name      : {name}")
    print(f"  Array     : \n{arr}")
    print(f"  Dimensions: {arr.ndim}")
    print(f"  Shape     : {arr.shape}")
    print(f"  Size      : {arr.size}")
    print(f"  Dtype     : {arr.dtype}")
    print(f"  Itemsize  : {arr.itemsize} bytes")
    print(f"  Python Type: {type(arr)}")
    print()


# ============================================================
# 1. Array Creation
# ============================================================
print("=" * 50)
print("1. ARRAY CREATION")
print("=" * 50)

# 1D array
a = np.array([1, 2, 3])
print_array_info("1D Array", a)

# 2D array
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print_array_info("2D Array", b)

# 3D array (2 blocks x 2 rows x 3 cols)
c = np.array([[[1,  2,  3],
               [4,  5,  6]],
              [[7,  8,  9],
               [10, 11, 12]]])
print_array_info("3D Array", c)


# ============================================================
# 2. Array Creation Functions
# ============================================================
print("=" * 50)
print("2. ARRAY CREATION FUNCTIONS")
print("=" * 50)

print("  zeros(2,3)    :", np.zeros((2, 3)))
print("  ones(2,3)     :", np.ones((2, 3)))
print("  full(2,3) = 7 :", np.full((2, 3), 7))
print("  eye(3)        :\n", np.eye(3))
print("  arange(0,10,2):", np.arange(0, 10, 2))
print("  linspace(0,1,5):", np.linspace(0, 1, 5))
print("  random(2,3)   :\n", np.random.rand(2, 3))
print()


# ============================================================
# 3. Data Types
# ============================================================
print("=" * 50)
print("3. DATA TYPES")
print("=" * 50)

print("  int32  :", np.array([1, 2, 3], dtype=np.int32).dtype)
print("  float64:", np.array([1, 2, 3], dtype=np.float64).dtype)
print("  bool   :", np.array([1, 0, 1], dtype=bool).dtype)
print("  complex:", np.array([1+2j, 3+4j]).dtype)
print()


# ============================================================
# 4. Indexing & Slicing
# ============================================================
print("=" * 50)
print("4. INDEXING & SLICING")
print("=" * 50)

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16]])

print("  Array:\n", arr)

# Basic access
print("  arr[0, 2]        :", arr[0, 2])          # single element
print("  arr[1, :]        :", arr[1, :])           # entire row
print("  arr[:, 2]        :", arr[:, 2])           # entire column

# Slicing with step
print("  arr[0, 1:6]      :", arr[0, 1:6])         # start:end
print("  arr[0, 1:6:2]    :", arr[0, 1:6:2])       # start:end:step

# Negative indexing
print("  arr[-1, -1]      :", arr[-1, -1])          # last row, last col
print("  arr[1, -3:]      :", arr[1, -3:])          # last 3 of row 1

# Sub-matrix
print("  arr[0:2, 1:4]    :\n", arr[0:2, 1:4])     # sub-matrix

# Boolean indexing
print("  arr[arr > 10]    :", arr[arr > 10])

# 3D indexing
d = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print("  3D arr[1,0,1]    :", d[1, 0, 1])           # → 6

# Changing single element
arr[1, 5] = 20
print("  After arr[1,5]=20:\n", arr)

# Changing entire row / column
arr[0, :] = 0
print("  After arr[0,:]=0 :\n", arr)

arr[:, 2] = [99, 99]
print("  After arr[:,2]=99:\n", arr)
print()


# ============================================================
# 5. Copy vs View
# ============================================================
print("=" * 50)
print("5. COPY VS VIEW")
print("=" * 50)

original = np.array([1, 2, 3, 4, 5])

# View — shares memory, changes affect original
view = original[1:4]
view[0] = 99
print("  After modifying view[0]=99:")
print("  view     :", view)
print("  original :", original)   # original also changed!

# Reset
original = np.array([1, 2, 3, 4, 5])

# Copy — independent, safe
copy = original[1:4].copy()
copy[0] = 99
print("  After modifying copy[0]=99:")
print("  copy     :", copy)
print("  original :", original)   # original unchanged
print()


# ============================================================
# 6. Type Casting
# ============================================================
print("=" * 50)
print("6. TYPE CASTING")
print("=" * 50)

t = np.array([1.7, 2.5, 3.9])
print("  Original (float64)  :", t, "dtype:", t.dtype)
print("  astype(int32)       :", t.astype(np.int32), "dtype:", t.astype(np.int32).dtype)
print("  astype(float32)     :", t.astype(np.float32), "dtype:", t.astype(np.float32).dtype)
print("  astype(bool)        :", t.astype(bool), "dtype:", t.astype(bool).dtype)

i = np.array([0, 1, 255], dtype=np.int32)
print("  int → float64       :", i.astype(np.float64))
print("  int → bool          :", i.astype(bool))   # 0=False, non-zero=True
print()


# ============================================================
# 7. Reshaping & Transpose
# ============================================================
print("=" * 50)
print("7. RESHAPING & TRANSPOSE")
print("=" * 50)

r = np.arange(1, 13)
print("  Original (1D) :", r)
print("  reshape(3,4)  :\n", r.reshape(3, 4))
print("  reshape(2,2,3):\n", r.reshape(2, 2, 3))
print("  flatten()     :", r.reshape(3, 4).flatten())
print("  Transpose     :\n", r.reshape(3, 4).T)
print()


# ============================================================
# 8. Math Operations
# ============================================================
print("=" * 50)
print("8. MATH OPERATIONS")
print("=" * 50)

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print("  x         :", x)
print("  y         :", y)
print("  x + y     :", x + y)
print("  x * y     :", x * y)
print("  x ** 2    :", x ** 2)
print("  x + 10    :", x + 10)      # broadcasting scalar
print("  sqrt(x)   :", np.sqrt(x))
print("  exp(x)    :", np.exp(x))
print("  log(x)    :", np.log(x))
print()


# ============================================================
# 9. Aggregate Functions
# ============================================================
print("=" * 50)
print("9. AGGREGATE FUNCTIONS")
print("=" * 50)

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("  Array:\n", m)
print("  sum()       :", m.sum())
print("  sum(axis=0) :", m.sum(axis=0))    # column-wise
print("  sum(axis=1) :", m.sum(axis=1))    # row-wise
print("  min()       :", m.min())
print("  max()       :", m.max())
print("  mean()      :", m.mean())
print("  std()       :", m.std())
print("  cumsum()    :", m.cumsum())
print()


# ============================================================
# 10. Broadcasting
# ============================================================
print("=" * 50)
print("10. BROADCASTING")
print("=" * 50)

base = np.array([[1, 2, 3],
                 [4, 5, 6]])
row_vec = np.array([10, 20, 30])   # shape (3,) broadcasts over rows

print("  base array:\n", base)
print("  row vector :", row_vec)
print("  base + row :\n", base + row_vec)
print()


# ============================================================
# 11. Stack & Concatenate
# ============================================================
print("=" * 50)
print("11. STACK & CONCATENATE")
print("=" * 50)

p = np.array([1, 2, 3])
q = np.array([4, 5, 6])

print("  vstack:\n", np.vstack((p, q)))
print("  hstack:", np.hstack((p, q)))
print("  concatenate axis=0:\n", np.concatenate((p.reshape(1,-1), q.reshape(1,-1)), axis=0))
print()


# ============================================================
# 12. Useful Utility Functions
# ============================================================
print("=" * 50)
print("12. UTILITY FUNCTIONS")
print("=" * 50)

u = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("  Array       :", u)
print("  sort()      :", np.sort(u))
print("  argsort()   :", np.argsort(u))
print("  unique()    :", np.unique(u))
print("  where(>4)   :", np.where(u > 4))
print("  any(>8)     :", np.any(u > 8))
print("  all(>0)     :", np.all(u > 0))
print("  argmin/max  :", np.argmin(u), "/", np.argmax(u))