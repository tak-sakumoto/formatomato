import re

from parse_args import parse_args
from get_dataset import get_dataset
from for_coco.make_image_df import make_image_df
from for_coco.make_df import make_df
from for_coco.make_class_df import make_class_df
from for_imagenet.make_df_imagenet import make_df_imagenet
from write_df_csv import write_df_csv

def main():
    # Parsing arguments
    args = parse_args()
    input_dataset_path = args.input_dataset_path
    dataset_name = args.dataset_name
    output_csv_path = args.output_csv_path
    output_image_csv_path = args.output_image_csv_path
    output_class_csv_path = args.output_class_csv_path
    normalize = args.normalize

    # Getting a given dataset
    try:
        dataset = get_dataset(dataset_name, input_dataset_path)
    except ValueError as err:
        print(err)
        return 1        
    
    if re.search('coco', dataset_name, flags=re.IGNORECASE):
        # Making a Pandas Dataframe of image infomation
        images_df = make_image_df(dataset)
        # Making a dictionary of class lists
        class_df = make_class_df(dataset)
        # Making a dictionary of the extracted data lists
        df = make_df(dataset, images_df, class_df, normalize)
    elif re.search('imagenet', dataset_name, flags=re.IGNORECASE):
        df, images_df, class_df = make_df_imagenet(dataset)
    
    # Writing CSVs based on Pandas Dataframe
    write_df_csv(
        df, images_df, class_df,
        output_csv_path, output_image_csv_path,
        output_class_csv_path
    )

    return 0

if __name__ == '__main__':
    exit(main())