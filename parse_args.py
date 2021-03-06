import argparse

def parse_args():
    """
    Parsing arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_dataset_path", default=None, type=str)
    parser.add_argument("--dataset_name", default=None, type=str)
    parser.add_argument("--config_path", default=None, type=str)    
    parser.add_argument("--output_csv_path", default='./out.csv', type=str)
    parser.add_argument("--output_image_csv_path", default='./out_image.csv', type=str)
    parser.add_argument("--output_class_csv_path", default='./out_classes.csv', type=str)
    parser.add_argument("--normalize", action='store_true')

    args = parser.parse_args()

    return args