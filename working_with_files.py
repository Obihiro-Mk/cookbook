dict_num = {}
def new_file(list_files, result_file):
    for files in list_files:
        with open(files, 'r', encoding='utf-8') as file:
            len_file = len(file.readlines())
            dict_num[files] = len_file
    sorted_val = sorted(dict_num.values())
    sorted_dict = {}
    for i in sorted_val:
        for key in dict_num.keys():
            if dict_num[key] == i:
                sorted_dict[key] = dict_num[key]
                break
    sorted_key = []
    sorted_value = []
    for k, v in sorted_dict.items():
        sorted_key.append(k)
        sorted_value.append(v)
    with open(result_file, 'w', encoding='utf-8') as file_1:
        file_1.write(str(sorted_key[0]) + '\n')
        file_1.write(str(sorted_value[0]) + '\n')
        with open(sorted_key[0], 'r', encoding='utf-8') as f_1:
            lines = f_1.read()
        file_1.write(lines + '\n')
    with open(result_file, 'a', encoding='utf-8') as file_2:
        file_2.write(str(sorted_key[1]) + '\n')
        file_2.write(str(sorted_value[1]) + '\n')
        with open(sorted_key[1], 'r', encoding='utf-8') as f_2:
            lines = f_2.read()
        file_2.write(lines + '\n')
    with open(result_file, 'a', encoding='utf-8') as file_3:
        file_3.write(str(sorted_key[2]) + '\n')
        file_3.write(str(sorted_value[2]) + '\n')
        with open(sorted_key[2], 'r', encoding='utf-8') as f_3:
            lines = f_3.read()
        file_3.write(lines)

    # print(sorted_list)
list_file = ['1.txt', '2.txt', '3.txt']
new_file(list_file, 'final result.txt')
# with open('1.txt', encoding='utf-8') as file_1:
#     len_file_1 = len(file_1.readlines())
#     dict_num['1.txt'] = len_file_1
# with open('2.txt', encoding='utf-8') as file_2:
#     len_file_2 = len(file_2.readlines())
#     dict_num['2.txt'] = len_file_2
# with open('3.txt', encoding='utf-8') as file_3:
#     len_file_3 = len(file_3.readlines())
#     dict_num['3.txt'] = len_file_3
# print(dict_num)