import pandas as pd

from get_categories import get_categories

def make_class_df(coco):
    """
    Making a Pandas Dataframe of classes
    """
    # Getting category infomations from a COCO dataset
    cat_names, supercat_names, cat_ids\
        = get_categories(coco)

    # Making a dictionary of category names with category ID keys
    cat_names = {
        cat_id: cat_name 
        for cat_id, cat_name in zip(cat_ids, cat_names)
    }
    
    # Making lists of class columns
    class_ids = [cat_id for cat_id in cat_ids]
    superclasses = [supercat_name for supercat_name in supercat_names]
    classes = [cat_names[class_id] for class_id in class_ids]

    class_df_dict = {
        'CLASS_ID': class_ids,
        'SUPERCLASS': superclasses,
        'CLASS': classes
    }

    # Making a Pandas Dataframe
    class_df = pd.DataFrame(class_df_dict)

    # Set IMAGE_ID as index
    class_df = class_df.set_index('CLASS_ID')

    return class_df