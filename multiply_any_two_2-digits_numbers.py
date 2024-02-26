# Description of the logic I am attempting to code down. For more details about the source, refer to README file.
# it includes a mind map of how the logic works.

# 1. Get any two 2-digits numbers from the user. For this breakdown here, we'll use 78 and 79 as examples.
# 1b. multiply the 7 from 78 to the 7 from 79, giving 49.
# 1c. store it in a string list: first_number --> [4, 9]
# 1d. multiply the 8 from 78 to the 9 from 79, giving 72
# 1e. store it in a string list: last_number --> [7, 2]
# 2. multiply the 7 from 78 to the 9 from 79, giving 63
# 2b. multiply the 8 from 78 to the 7 from 79, giving 56
# 2c. add both results together, 63 + 56 = 119
# 2d. store the result in a string list: center_number --> [1, 1, 9]
# 3. the 2nd digit of last_number (the 2 from 72, in 1e.) is appended to the list of the final number. So it is its last digit:
# list_f_result = [2]
# 3b. the 1st digit of last_number (the 7 from 72, in 1e.) is added to the last digit of the center_number (the 9 from 119, in 2c.).
# the result is: 7 + 9 = 16, we store the result in a string list: wz --> [1, 6].
# 3c. the 2nd digit of wz (the 6 from 16) is .insert(0) to list_f_result --> [6, 2]
# 3d. we add the 2nd digit of center_number (the 1 from 119, in 2d.) to the 2nd digit of first_number (the 9 from 49, in 1c.) --> 1 + 9 = 10
# and we add to that result the 1 from 16 (from wz, in 3b.) --> 10 + 1 = 11
# 3e. we store it in a string list: op --> [1, 1]
# 3f. the 2nd digit of op (the 1 from 11) is.insert(0) to list_f_result --> [1, 6, 2]
# 3g. we add the 1st digit of first_number (the 4 from 49, in 1c.) to the 1st digit of op (the 1 from 11, in 3e.) --> 4 + 1 = 5
# and we add to that result the 1st digit of center_number (1 from 119, in 2d.) --> 5 + 1 = 6
# 3h. we .insert(0) to list_f_result --> [6, 1, 6, 2]

# print(f"{78 * 79}")

# -----------------------------------------------------------------------------
