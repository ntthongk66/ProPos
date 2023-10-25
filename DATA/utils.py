import json
import os
import shutil

def txt2dict(txt_file: str, split_char: str):
    img_text_dict = {}
    with open(txt_file, 'r') as file:
        for line in file:
            line = line.rstrip()
            image_file_name = line.split(split_char)[0]
            word = line.split(split_char)[1]
            img_text_dict[image_file_name] = word
            
    return img_text_dict

def json2dict(json_file: str):
    with open(json_file, 'r') as file:
        dict_ = json.load(file)
    return dict_

def dict2txt(dict_: dict, name_txt_file: str):
    with open(name_txt_file, 'w') as file:
        for key, value in dict_.items():
            file.write(f'{key} {value}\n')

def txt2list(txt_file: str):
    List_lines = []
    with open(txt_file, 'r') as file:
        for line in file:
            line = line.rstrip()
            List_lines.append(line)
    
    return List_lines

def change(old_: dict, refer_: dict):
    for key_ in refer_:
        if refer_[key_] != old_[key_]:
            old_[key_] = refer_[key_]


def create_dir(directory_name: str):
    if not os.path.exists(directory_name):
    # Create the directory
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

def create_dirs(directory_path: str):
    

    # Create the directory structure
    os.makedirs(directory_path, exist_ok=True)

    print(f"Directory structure '{directory_path}' created successfully.")

def dict_train_valid_error(dict_gt: dict, dict_pred: dict, clust_folder: dict):
    list_predict_train_error = []
    for image_name in dict_pred:
        if dict_gt[image_name] != dict_pred[image_name]:
            list_predict_train_error.append(image_name)

    # print(len(list_predict_train_error))
    dict_error_clust_folder = {}
    Cluster_list = list(clust_folder.keys())
    for cluster in Cluster_list:
        # print(cluster)
        cluster = str(cluster)
        dict_error_clust_folder[cluster] = []
        
        for error in list_predict_train_error:
            if error in clust_folder[cluster]:
                dict_error_clust_folder[cluster].append(error)
                # list_predict_train_error.remove(error)

    dict_num_of_error_clust = {}
    for cluster in Cluster_list:
        dict_num_of_error_clust[cluster] = len(dict_error_clust_folder[cluster])

    return dict_num_of_error_clust, dict_error_clust_folder



def copy_image_to_folder(src_folder: str,  target_path: str, Specify_Clusters: list, epoch: int, Num_of_cluster: int, clust_folder: dict, dict_error_clust_folder:dict, dict_image_text_gt: dict, dict_image_text_pred_train: dict, dict_percentage_error_clust: dict):
    
    target_path = target_path + f'/{epoch}_{Num_of_cluster}'
    # os.mkdir(target_path)
    
    
    for i in Specify_Clusters:
    #make folder
        # public_train_txt = '.txt'
        # public_test_txt = '.txt'
        
        # error_txt = '.txt'
        
        
        Class_folder = f'{target_path}_{dict_percentage_error_clust[str(i)]}_{i}' 
        Class_folder_train = Class_folder + '/' + 'train'
        Class_folder_test = Class_folder + '/' + 'test'
        Class_folder_error = Class_folder + '/' + 'error'
        if not os.path.exists(Class_folder):
            create_dir(Class_folder)
        
            create_dir(Class_folder_train)
            create_dir(Class_folder_test)
            create_dir(Class_folder_error)
            
            with open(Class_folder + '/' + 'train.txt', 'w') as train_file:
                for file_image_name in clust_folder[str(i)]:
                    if file_image_name[0:5] == 'train':
                        print(file_image_name, file= train_file)
                        shutil.copy(src_folder + file_image_name, Class_folder_train)
            
            with open(Class_folder + '/' + 'test.txt', 'w') as test_file:
                for file_image_name in clust_folder[str(i)]:
                    if file_image_name[7:11] == 'test':
                        print(file_image_name, file=test_file)
                        shutil.copy(src_folder + file_image_name, Class_folder_test)
            
            with open(Class_folder + '/' + 'error.txt', 'w') as error_file:
                for file_image_error in dict_error_clust_folder[str(i)]:    
                    print(file_image_name, file=error_file)
                    shutil.copy(src_folder + file_image_error, Class_folder_error)
                    current_file_name = f'{Class_folder_error}/{file_image_error}'
                    new_file_name = f'{Class_folder_error}/{file_image_error.split(".")[0]}_{dict_image_text_gt[file_image_error]}_{dict_image_text_pred_train[file_image_error]}.{file_image_error.split(".")[1]}'
                    os.rename(current_file_name, new_file_name)

if __name__=='__main__':
    
    # file_txt_gt = 'train_gt.txt'
    # file_txt_83k_correct_gt = 'train_correct_label.txt'
    
    # gt_dict = txt2dict(file_txt_gt, split_char='\t')
    # correct_gt_83K = txt2dict(txt_file=file_txt_83k_correct_gt, split_char=' ')
    
    # change(old_=gt_dict, refer_=correct_gt_83K)
    
    # dict2txt(dict_=gt_dict, name_txt_file='new_gt.txt')
    #------------------------------------------
    
    create_dirs('h/t/w')
    
    