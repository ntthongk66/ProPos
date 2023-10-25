from DATA.utils import *
from DATA.draw_chart import *
#*==================CONFIG====================

txt_new_gt = 'DATA/new_gt.txt'
config_predict_train_valid = 'resnet_seq2seq_ema_train'
txt_predict_train_valid = f'/home/ntthong/NTT/OCR/ProPos/Predict/Predict_train/After_private/{config_predict_train_valid}.txt'
txt_predict_33k_test = ''

# json_cluster_folder = ''

ckpt = 64  # 19, 29, 49, 50, 56, 64
Num_of_cluster = 150 # 20, 50, 70, 100, 120, 150, 170, 200
Model_name = f'byol_{ckpt}'

# Chart
width = 80
height = 8
dpi = 250

json_cluster_folder = f'/home/ntthong/NTT/OCR/ProPos/Cluster_folder/ProNos_resnet50_v2/{Model_name}/clust_folder_{Model_name}_{Num_of_cluster}.json'

path_visual_save = f'Visualize/{config_predict_train_valid}/{Model_name}/{Num_of_cluster}' # or maybe test_predict

#* Create folder to save cluster image and chart
create_dirs(path_visual_save)

clust_folder = json2dict(json_file=json_cluster_folder)

#sort key '1', '2', ...
clust_folder = dict(sorted(clust_folder.items(), key=lambda item: int(item[0])))

#txt2dict
dict_gt = txt2dict(txt_file=txt_new_gt, split_char=' ')
dict_pred_train_valid = txt2dict(txt_file=txt_predict_train_valid, split_char=' ')



Cluster_list = list(clust_folder.keys())
dict_cluster_total_images = {}
dict_cluster_trains = {}
dict_cluster_tests = {}
dict_percentages_of_test_in_cluster = {}
for cluster in clust_folder: 
    dict_cluster_total_images[cluster] = len(clust_folder[cluster])



    n_test = 0
    n_train = 0
    for file_name in clust_folder[cluster]:
        
        if file_name[7:11] == 'test':
            n_test += 1
        if file_name[0:5] == 'train':
            n_train += 1
        
    dict_cluster_trains[cluster] = n_train
    dict_cluster_tests[cluster] = n_test
    percentage_test = (n_test / dict_cluster_total_images[cluster]) *100
    dict_percentages_of_test_in_cluster[cluster] = (round(percentage_test, 2))


dict_num_of_error_clust, dict_error_clust_folder = dict_train_valid_error(dict_gt=dict_gt, dict_pred=dict_pred_train_valid, clust_folder=clust_folder)

dict_percentage_error_clust = {}

for clust in Cluster_list:
    dict_percentage_error_clust[clust] = round((dict_num_of_error_clust[clust] / dict_cluster_trains[clust]) * 100.0, 2)
    

plot_num_of_error_each_cluster(dict_num_of_error_clust=dict_num_of_error_clust, width=width, height=height, dpi=dpi, save_figure_path=path_visual_save)
print(cluster)

plot_num_of_train_test_each_cluster(Cluster_list, dict_cluster_trains, dict_cluster_tests, dict_cluster_total_images, width, height, dpi, path_visual_save, Model_name, Num_of_cluster)

plot_percentage_of_test(Cluster_list, dict_percentages_of_test_in_cluster, 'Test', width, height, dpi, path_visual_save, Model_name, Num_of_cluster)

sorted_dict_percentage_error_clust = dict(sorted(dict_percentage_error_clust.items(), key=lambda item: item[1], reverse=True))

plot_percentage_of_test(Cluster_list, sorted_dict_percentage_error_clust, 'Error', width, height, dpi, path_visual_save, Model_name, Num_of_cluster)


src_folder = '/home/ntthong/NTT/OCR/ProPos/DATA/ocr_dataset/new_train/'


Top_n = 20
# sorted_dict_percentage_error_clust = dict(sorted(dict_percentage_error_clust.items(), key=lambda item: item[1], reverse=True))


copy_image_to_folder(src_folder, path_visual_save, list(sorted_dict_percentage_error_clust.keys())[:Top_n], ckpt, Num_of_cluster, clust_folder, dict_error_clust_folder, dict_gt, dict_pred_train_valid, dict_percentage_error_clust)