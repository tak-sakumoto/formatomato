import pandas as pd

def make_class_df(cat_names, supercat_names, cat_ids):
    """
    Making a dictionary of the class lists
    """

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