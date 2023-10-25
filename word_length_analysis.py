from DATA.utils import txt2dict

txt_new_gt_file = 'DATA/new_gt.txt'

dict_new_gt = txt2dict(txt_new_gt_file, split_char=' ')

dict_single_char = {}

for image_name in dict_new_gt:
    if len(dict_new_gt[image_name]) == 1:
        dict_single_char[image_name] = dict_new_gt[image_name]
    

print(len(dict_single_char))

list_single_word_char = [value for value in dict_single_char.values()]

combined_string = ''.join(list_single_word_char)

capital_characters = [char for char in combined_string if char.isupper()]
non_capital_characters = [char for char in combined_string if char.islower()]

print(len(capital_characters))
print(len(non_capital_characters))

assert len(dict_single_char) == len(capital_characters) + len(non_capital_characters)

# print(dict_single_char)