import numpy as np
students=np.array([
    [201,19,85],
    [202,20,90],
    [203,18,78],
    [204,21,92],
    [205,20,88]
])

# Insert a second student [206,22,95] at the second position
new_arr_students=np.insert(students,1,[206,22,95],axis=0)
print("After inserting new student info :\n",new_arr_students)

# Delete the student with id 203
index_to_remove = np.where(new_arr_students[:,0] == 203)[0][0]
new_arr_students1 = np.delete(new_arr_students, index_to_remove, axis=0)
print("After deleting the student with id 203:\n",new_arr_students1)

# Append a new column for attadance [80,85,88,90,95]
attandance=np.array([80,85,88,90,95]).reshape(-1,1)
new_arr_students2=np.append(new_arr_students1,attandance,axis=1)
print("After appending new info :\n",new_arr_students2)

# select only students with marks>85
marks=new_arr_students2[:,2]
print("Marks column :\n",marks)
high_scores=new_arr_students2[marks>85]
print("Students with high score :\n",high_scores)

# Split the dataset into IDs and other data
ids,age,marks,attendance=np.hsplit(new_arr_students2,4)
print("After spliting Datasets :\n")
print("ID :\n",ids)
print("Age :\n",age)
print("Marks :\n",marks)
print("Attandance :\n",attendance)

# Stack the datasets into one dataset
final_dataset=np.hstack((ids,age,marks,attendance)) 
print("stacked dataset:\n",final_dataset)

# Reshape the final dataset into 1D array
reshaped_dataset=final_dataset.ravel()
print("After reshaping the final array :\n",reshaped_dataset)

# Reverse the 1D array
revers_arr=reshaped_dataset[::-1]
print("Reversed array :\n",revers_arr)