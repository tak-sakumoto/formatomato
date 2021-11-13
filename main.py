import pandas as pd
from pycocotools.coco import COCO

from parse_args import parse_args
from get_categories import get_categories
from load_imgs import load_imgs
from load_anns import load_anns
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

    coco = COCO(input_coco_path)

    # Getting category infomations from a COCO dataset
    cat_names, supercat_names, cat_ids\
        = get_categories(coco)

    # Making a dictionary of category names with category ID keys
    cat_names = {
        cat_id: cat_name 
        for cat_id, cat_name in zip(cat_ids, cat_names)
    }
    
    # Loading image informations
    images = load_imgs(coco)
    # Loading annotations
    anns = load_anns(coco)

    # Making a Pandas Dataframe of image infomation
    images = make_image_df(images)

    # Making a dictionary of the extracted data lists
    df = make_df(anns, images, cat_names)
    # Making a dictionary of class lists
    class_df = make_class_df(cat_names, supercat_names, cat_ids)

    # Writing CSVs based on Pandas Dataframe
    write_df_csv(
        df, images, class_df,
        output_csv_path, output_image_csv_path,
        output_class_csv_path
    )

if __name__ == '__main__':
    main()