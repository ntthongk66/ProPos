import matplotlib.pyplot as plt 


def plot_num_of_error_each_cluster(dict_num_of_error_clust: dict, width: int, height: int, dpi: int,save_figure_path: str):
    
    cluster = list(dict_num_of_error_clust.keys())
    num_of_error = list(dict_num_of_error_clust.values())

    title_name = 'error_clust_folder'
    # Create a bar chart
    plt.figure(figsize=(width, height))
    plt.bar(cluster, num_of_error, label = 'error')
    
    for i, value in enumerate(num_of_error):
        plt.text(i, value, str(value), ha='center', va='bottom', rotation = 90)
    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart from Dictionary Data')
    plt.savefig(f'{save_figure_path}/{title_name}.png', dpi=dpi)
    # Show the chart
    # plt.show()

def plot_num_of_train_test_each_cluster(CLuster_list: list, dict_clust_trains: dict, dict_clust_tests: dict, dict_cluster_total_image: dict, width: int, height: int, dpi: int,save_figure_path: str, Model_name: str, Num_of_cluster: int):
# Create a stacked bar chart
    trains = [value for value in dict_clust_trains.values()]
    tests = [value for value in dict_clust_tests.values()]
    plt.figure(figsize=(width, height))
    plt.bar(CLuster_list, trains, label='Train')
    plt.bar(CLuster_list, tests, bottom=trains, label='Public test')
    for i, (key ,value) in enumerate(dict_cluster_total_image.items()):
        plt.text(i, value, str(value), ha='center', va='bottom', rotation = 90)

    title_name = f'Train-Test Proportion each Cluster-{Model_name}_{Num_of_cluster}'
    plt.xlabel('Cluster')
    plt.ylabel('Images')
    plt.title(title_name)
    plt.legend()
    plt.savefig(f'{save_figure_path}/{title_name}.png', dpi=dpi)
    # plt.show()
    
def plot_percentage_of_test(CLuster_list: list, dict_tests_percentage: dict, name: str,  width: int, height: int, dpi: int,save_figure_path: str, Model_name: str, Num_of_cluster: int):
    
    tests_percentage = [value for value in dict_tests_percentage.values()]
    
    plt.figure(figsize=(width, height))
    plt.bar(CLuster_list, tests_percentage, label='Percentage (%)')
    # plt.bar(CLuster_list, tests, bottom=trains, label='Public test')
    title_name = f'{name} Proportion each Cluster in {Model_name}_{Num_of_cluster}'
    for i, (key, value) in enumerate(dict_tests_percentage.items()):
        plt.text(i, value, str(value) +'%', ha='center', va='bottom', rotation = 90)
    plt.xlabel('Cluster')
    plt.ylabel('Percentage (%)')
    # plt.ylim(0,100)
    plt.title(title_name)
    plt.legend()
    plt.savefig(f'{save_figure_path}/{title_name}.png', dpi=dpi)