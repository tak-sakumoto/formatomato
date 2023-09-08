import argparse

def parse_args():
    """
    Parsing arguments
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input_dataset_path", type=str, required=True)
    parser.add_argument("--input_csv_path", type=str, required=True)
    parser.add_argument("--input_image_csv_path",type=str, required=True)
    parser.add_argument("--input_class_csv_path",type=str, required=True)
    parser.add_argument("--bbox", type=str, required=True)
    parser.add_argument("--output_image_dir_path",type=str, default="./out")
    parser.add_argument("--normalize", action="store_true")

    args = parser.parse_args()

    return args