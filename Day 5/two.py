# --- Part Two ---

# The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

# Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

# Your computer is only missing a few opcodes:

#     Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
#     Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
#     Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
#     Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

# Like all instructions, these instructions need to support parameter modes as described above.

# Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

# For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

#     3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#     3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
#     3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#     3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).

# Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

#     3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
#     3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)

# Here's a larger example:

# 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99

# The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

# This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

# What is the diagnostic code for system ID 5?


data = [int(v) for v in open('input').readline().split(',')]
i = 0
while data[i] != 99:
    instruction = data[i]
    opcode = data[i] % 100
    if opcode in [1, 2, 7, 8]:
        arg1 = data[i + 1] if instruction // 100 % 10 else data[data[i + 1]]
        arg2 = data[i + 2] if instruction // 1000 % 10 else data[data[i + 2]]
        out_id = i + 3 if instruction // 10000 % 10 else data[i + 3]
        i += 4
    elif opcode in [5, 6]:
        arg1 = data[i + 1] if instruction // 100 % 10 else data[data[i + 1]]
        arg2 = data[i + 2] if instruction // 1000 % 10 else data[data[i + 2]]
        out_id = None
        i += 3
    elif opcode in [3, 4]:
        arg1 = None
        arg2 = None
        out_id = i + 1 if instruction // 1000 else data[i + 1]
        i += 2
    else:
        raise Exception('Incorrect opcode raised : %s' % opcode)

    if opcode == 1:
        data[out_id] = arg1 + arg2
    elif opcode == 2:
        data[out_id] = arg1 * arg2
    elif opcode == 3:
        data[out_id] = input('Input : ')
    elif opcode == 4:
        print('Output of instruction "%d" in position %d : %d' % (data[i - 2], i, data[out_id]))
    elif opcode == 5:
        if arg1:
            i = arg2
    elif opcode == 6:
        if not arg1:
            i = arg2
    elif opcode == 7:
        if arg1 < arg2:
            data[out_id] = 1
        else:
            data[out_id] = 0
    elif opcode == 8:
        if arg1 == arg2:
            data[out_id] = 1
        else:
            data[out_id] = 0
