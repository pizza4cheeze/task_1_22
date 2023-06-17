def find_longest_sublist(input):
    max_list = []
    curr_list = []

    for i in range(len(input) - 1):
        if input[i + 1] - input[i] == 1:
            if not curr_list:
                curr_list.append(input[i])
            curr_list.append(input[i + 1])

            if len(curr_list) > len(max_list):
                max_list = curr_list.copy()
        else:
            curr_list = []

    if len(curr_list) > len(max_list):
        max_list = curr_list.copy()

    return max_list


file_output = open('output.txt', 'w')

with open('input.txt', 'r') as file_input:
    lines = file_input.readlines()
    for line in lines:
        input_list = list(map(int, line.split(', ')))
        input_sorted = input_list.copy()
        input_sorted.sort()
        print(input_list, input_sorted[0])
        sublist = find_longest_sublist(input_sorted)
        print(input_sorted, sublist)
        print()
        file_output.write(str(sublist) + '\n')
