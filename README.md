# Numpy_Fun_Projects
Collection of NumPy array manipulation challenges and solutions

# NumPy Fun Challenge - Student Dataset Manipulation

This project is a NumPy-based data manipulation challenge designed to practice **array creation, insertion, deletion, appending, boolean masking, splitting, stacking, reshaping, and reversing**.

##  Problem Statement

We have a dataset representing student information:

| ID   | Age | Marks |
|------|-----|-------|
| 201  | 19  | 85    |
| 202  | 20  | 90    |
| 203  | 18  | 78    |
| 204  | 21  | 92    |
| 205  | 20  | 88    |

**Tasks:**
1. **Insert** a new student `[206, 22, 95]` at the **second position**.
2. **Delete** the student with **ID 203**.
3. **Append** a new column for **Attendance %** = `[80, 85, 88, 90, 95]`.
4. **Select** only students with **Marks > 85** using Boolean Masking.
5. **Split** the dataset into `IDs` and other columns (Age, Marks, Attendance).
6. **Stack** the split parts back into a single dataset.
7. **Reshape** the dataset into a **1D array**.
8. **Reverse** the 1D array.


##  Technologies Used
- **Python 3**
- **NumPy** (for array manipulation)


##  File Structure

##  How to Run the Code
1. Install NumPy if not already installed:
   ```bash
   pip install numpy

Run the Python script: Numpy_Array_Manipulate.py

Sample Output:
After inserting new student info :
 [[ 201   19   85]
 [ 206   22   95]
 [ 202   20   90]
 [ 203   18   78]
 [ 204   21   92]
 [ 205   20   88]]

After deleting the student info :
 [[ 201   19   85]
 [ 206   22   95]
 [ 202   20   90]
 [ 204   21   92]
 [ 205   20   88]]

After appending new info :
 [[ 201   19   85   80]
 [ 206   22   95   85]
 [ 202   20   90   88]
 [ 204   21   92   90]
 [ 205   20   88   95]]

Students with high score :
 [[ 206   22   95   85]
 [ 202   20   90   88]
 [ 204   21   92   90]
 [ 205   20   88   95]]

After reshaping the final array :
 [201  19  85  80 206  22  95  85 202  20  90  88 204  21  92  90 205  20  88  95]

Reversed array :
 [ 95  88  20 205  90  92  21 204  88  90  20 202  85  95  22 206  80  85  19 201]
