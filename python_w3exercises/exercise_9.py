# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

d = exam_st_date[0]
m = exam_st_date[1]
y = exam_st_date[2]

print(f"The examination will start from: {d} / {m} / {y}")
print("The examination will start from: %i / %i / %i" % exam_st_date)
