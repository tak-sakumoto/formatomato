import pandas as pd
from pycocotools.coco import COCO

from parse_args import parse_args
from make_image_df import make_image_df
from make_df import make_df
from make_class_df import make_class_df
from write_df_csv import write_df_csv


def main():
    # Parsing arguments
    args = parse_args()
    input_coco_path = args.input_coco_path
    output_csv_path = args.output_csv_path
    output_image_csv_path = args.output_image_csv_path
    output_class_csv_path = args.output_class_csv_path
    normalize = args.normalize

    coco = COCO(input_coco_path)
    
    # Making a Pandas Dataframe of image infomation
    images_df = make_image_df(coco)
    # Making a dictionary of class lists
    class_df = make_class_df(coco)
    # Making a dictionary of the extracted data lists
    df = make_df(coco, images_df, class_df, normalize)

    # Writing CSVs based on Pandas Dataframe
    write_df_csv(
        df, images_df, class_df,
        output_csv_path, output_image_csv_path,
        output_class_csv_path
    )

if __name__ == '__main__':
    main()