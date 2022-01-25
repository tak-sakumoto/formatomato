import pandas as pd
from PIL import Image
from pathlib import Path

def make_df_imagenet(dataset):
    """
    Making Pandas Dataframes of the extracted data
    """
    # Making lists of class columns
    classes = list(Path(dataset).iterdir())
    classes = [p.stem for p in classes if p.is_dir()]
    class_ids = [i for i in range(len(classes))]

    class_df_dict = {
        'CLASS_ID': class_ids,
        'CLASS': classes
    }

    # Making a Pandas Dataframe
    class_df = pd.DataFrame(class_df_dict)

    # Set IMAGE_ID as index
    class_df = class_df.set_index('CLASS_ID')

    image_ids = []
    file_names = []
    widths = []
    heights = []
    img_classes = []
    
    # Making lists of image information columns
    for _class in classes:
        img_path_list = list((Path(dataset) / _class).glob('*.JPEG'))

        for img_path in img_path_list:
            img = Image.open(img_path)
            file_names.append(img_path.name)
            widths.append(img.width)
            heights.append(img.height)
            img_classes.append(_class)
    
    image_ids = [i for i in range(len(file_names))]

    image_df_dict = {
        'IMAGE_ID': image_ids,
        'FILE_NAME': file_names,
        'WIDTH': widths,
        'HEIGHT': heights
    }
    
    # Making a Pandas Dataframe
    image_df = pd.DataFrame(image_df_dict)
    # Set IMAGE_ID as index
    image_df = image_df.set_index('IMAGE_ID')

    df_dict = {
        'IMAGE_ID': image_ids,
        'IMAGE_NAME': file_names,
        'CLASS': img_classes
    }

    # Making a Pandas Dataframe
    df = pd.DataFrame(df_dict)

    # Set IMAGE_ID as index
    df = df.set_index('IMAGE_ID')

    return df, image_df, class_df 
