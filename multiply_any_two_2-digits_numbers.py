# Description of the logic I am attempting to code down. For more details about the source, refer to README file.
# it includes a mind map of how the logic works.

# 1. Get any two 2-digits numbers from the user. For this breakdown here, we'll use
# 78 and 79 as examples, total = 6162
# store the 1st input un var:                                           xy --> 78
# the @nd input in var:                                                  ab --> 79
# 1b. multiply the 7 from 78 to the 7 from 79, giving 49.
# 1c. store it in a var:                                                      first_num --> 49
# 1d. multiply the 8 from 78 to the 9 from 79, giving 72
# 1e. store it in a var:                                                      last_num --> 7, 2
# 2. multiply the 7 from 78 to the 9 from 79, giving 63
# 2b. multiply the 8 from 78 to the 7 from 79, giving 56
# 2c. add both results together, 63 + 56 = 119
# 2d. store the result in a var:                                        center_num --> 119
# 3. the 2nd digit of last_num (the 2 from 72, in 1e.) is appended to the list of the final number. So it is its last digit:                                                                                 list_f_result = [_, _, _, 2]
# 3b. the 1st digit of last_num (the 7 from 72, in 1e.) is added to the last digit of the center_num (the 9 from 119, in 2c.).
# the result is: 7 + 9 = 16, we store the result in var:      wz --> 16
# 3c. the 2nd digit of wz (the 6 from 16) is .insert(0) to list_f_result = [_, _, 6, 2]
# 3d. we add the 2nd digit of center_num (the 2nd 1 from 119, in 2d.) to the 2nd digit of first_num (the 9 from 49, in 1c.) --> 1 + 9 = 10
# and we add to that result the 1 from 16 (from wz, in 3b.) --> 10 + 1 = 11
# 3e. we store it in a var:                                                 op --> 11
# 3f. the 2nd digit of op (the 1 from 11) is.insert(0) to   list_f_result = [_, 1, 6, 2]
# 3g. we add the 1st digit of first_num (the 4 from 49, in 1c.) to the 1st digit of op (the 1 from 11, in 3e.) --> 4 + 1 = 5
# and we add to that result the 1st digit of center_num (1 from 119, in 2d.) --> 5 + 1 = 6
# 3h. we .insert(0) to                                                       list_f_result = [6, 1, 6, 2]

# print(f"{78 * 79}")

# -----------------------------------------------------------------------------
import time

# -----------------------------------------------------------------------------

CLEAR = "\033[H\033[2J"

while True:

    choice = input(
        "\nWould you like to:\n1. Calculate two 2-digits numbers.\n2. Exit.\n\nPlease enter your choice (1 or 2): --> "
    )

    if choice == "1":
        list_f_result = []
        xy = input("\nEnter the 1st 2-digits number > 9 and < 100: --> ")  # 1.
        ab = input("\nEnter the 2nd 2-digits number > 9 and < 100: --> ")

        # func to multiply x to a, then add u and list out
        def mult_and_add(x, a):
            x = int(x)
            a = int(a)
            mult = x * a
            return mult

        # All vars here are INT
        first_num = mult_and_add(xy[0], ab[0])  # 1b. + 1c.
        last_num = mult_and_add(xy[1], ab[1])  # 1d. + 1e.
        step_2 = mult_and_add(xy[0], ab[1])  # 2.
        step_2b = mult_and_add(xy[1], ab[0])  # 2b.
        center_num = step_2b + step_2  # 2c. + 2d.
        ###print(f"Center number = {center_num}")

        # function to insert a digit to the final result list according to the length of its number:
        def insert_last_digit(extract_from_this, insert_to_this):
            extract_from_this = str(extract_from_this)
            # index [-1] extracts the last digit, no matter the length of insert_to_this.
            insert_to_this.insert(0, extract_from_this[-1])
            return insert_to_this

        if len(str(first_num)) == 2 and len(str(last_num)) == 2:
            print(CLEAR)

            insert_last_digit(last_num, list_f_result)  # 3.
            ###print(f"Final result is now: [_, _, _, {list_f_result}]")
            print(f"\nCalculating {xy} x {ab} = ...")
            time.sleep(1.5)
            # storing the 1st digit of last_num (7 from 72, in 1e.) in var: first_of_lastnumber
            first_of_lastnumber = int(str(last_num)[0])
            last_of_centernumber = int(str(center_num)[-1])
            wz = first_of_lastnumber + last_of_centernumber  # 3b.
            ###print(f"wz is: {wz}")

            if len(str(wz)) == 2:
                insert_last_digit(wz, list_f_result)  # 3c.
            else:
                list_f_result.insert(0, str(wz)[0])  # 3c.
            ###print(f"Final result is now: [_, _, {list_f_result}]")

            def add_int_str_nums(num1, index1, num2, index2, num3, index3):
                num1 = int(str(num1)[index1])
                num2 = int(str(num2)[index2])
                num3 = int(str(num3)[index3])
                return num1 + num2 + num3

            # eg. 87 * 89 for xy and ab
            if len(str(center_num)) == 3 and len(str(wz)) == 2:
                op = add_int_str_nums(center_num, 1, first_num, 1, wz, 0)  # 3d. 3e.
            elif len(str(center_num)) == 3 and len(str(wz)) == 1:
                op = add_int_str_nums(center_num, 1, first_num, 1)  # 3d. 3e.
            elif len(str(center_num)) == 3:
                op = add_int_str_nums(center_num, 1, first_num, 1, wz, 0)  # 3d. 3e.
            elif len(str(center_num)) == 2 and len(str(wz)) == 1:
                op = add_int_str_nums(center_num, 0, first_num, 1)  # 3d. 3e.
            elif len(str(center_num)) == 2:
                op = add_int_str_nums(center_num, 0, first_num, 1, wz, 0)  # 3d. 3e.
            else:
                op = add_int_str_nums(center_num, 0, first_num, 0, wz, 0)  # 3d. 3e.
            ###print(f"op is: {op}")

            if len(str(op)) == 2:
                list_f_result.insert(0, str(op)[1])  # 3f.
                final_1st_digit = add_int_str_nums(
                    first_num, 0, center_num, 0, op, 0
                )  # 3g.
            else:
                list_f_result.insert(0, str(op)[0])  # 3f.
                final_1st_digit = add_int_str_nums(first_num, 0, center_num, 0)  # 3g.
            ###print(f"Final result is now: [_, {list_f_result}]")

            if len(str(center_num)) == 2:
                final_1st_digit = add_int_str_nums(first_num, 0, op, 0)  # 3g.
            elif len(str(center_num)) == 1:
                final_1st_digit = add_int_str_nums(first_num, 0, center_num, 0)  # 3g.

            list_f_result.insert(0, str(final_1st_digit))  # 3h.
            list_f_result = [
                str(i) for i in list_f_result
            ]  # conversion to a string list
            final_result = "".join(list_f_result)

            ###print(f"\n{xy} x {ab} = {final_result}\n")

        elif len(str(first_num)) == 1 and len(str(last_num)) == 2:
            print(CLEAR)
            list_f_result.insert(0, str(last_num)[1])  # 3.
            wz = add_int_str_nums(
                center_num,
                1,
                last_num,
                0,
            )  # 3b.
            ###print(f"wz is {wz}")

            if len(str(wz)) == 1:  # eg. 27 * 29 for xy and ab
                list_f_result.insert(0, str(wz)[0])  # 3c.
                final_1st_num = add_int_str_nums(first_num, 0, center_num, 0)  # 3d.
                list_f_result.insert(0, final_1st_num)  # 3h.
            else:  # eg. 37 * 39 for xy and ab
                list_f_result.insert(0, str(wz)[1])  # 3c.
                final_1st_num = add_int_str_nums(
                    first_num, 0, center_num, 0, wz, 0
                )  # 3d.
                list_f_result.insert(0, final_1st_num)  # 3h.

        else:  # eg. 11 * 10 for xy and ab
            list_f_result.insert(0, last_num)  # 3.
            list_f_result.insert(0, center_num)  # 3b.
            list_f_result.insert(0, first_num)  # 3c.

        list_f_result = [str(i) for i in list_f_result]  # conversion to a string list
        final_result = "".join(list_f_result)
        print(CLEAR)
        print(f"\n{xy} x {ab} = {final_result}\n")
        time.sleep(1.5)

        ###print(f"{int(xy) * int(ab)}")

    else:
        print(CLEAR)
        print("\nExiting...\n")
        time.sleep(1)
        print(CLEAR)
        quit()
