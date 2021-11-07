import pandas as pd
from pycocotools.coco import COCO
from parse_args import parse_args
from get_categories import get_categories
from  load_imgs import load_imgs
from  load_anns import load_anns
from  make_df_dict import make_df_dict
from  make_class_df_dict import make_class_df_dict

def main():
    # Parsing arguments
    args = parse_args()
    input_coco_path = args.input_coco_path
    output_csv_path = args.output_csv_path
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
    print(supercat_names)
    # Loading annotations
    anns = load_anns(coco)

    # Making a dictionary of file names with image ID keys
    file_names = {img['id']: img['file_name'] for img in images}

    # Making a dictionary of the extracted data lists
    df_dict = make_df_dict(anns, file_names, cat_names)

    # Making a Pandas Dataframe
    df = pd.DataFrame(df_dict)

    # Saving the Pandas Dataframe to a CSV file
    df.to_csv(output_csv_path, index=False)

    # Making a dictionary of class lists
    class_df_dict = make_class_df_dict(cat_names, supercat_names, cat_ids)

    # Making a Pandas Dataframe for classes
    class_df = pd.DataFrame(class_df_dict)

    # Saving the Pandas Dataframe for classes to a CSV file
    class_df.to_csv(output_class_csv_path, index=False)

if __name__ == '__main__':
    main()