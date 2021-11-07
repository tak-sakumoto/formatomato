import argparse

def parse_args():
    """
    Parsing arguments
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input_coco_path", type=str)
    parser.add_argument("--output_csv_path", default='./out.csv', type=str)
    parser.add_argument("--output_class_csv_path", default='./out_classes.csv', type=str)

    args = parser.parse_args()

    return args