import pandas as pd

from load_anns import load_anns

def make_df(coco, images, class_df, normalize=False):
    """
    Making a Pandas Dataframe of the extracted data
    """
    # Loading annotations
    anns = load_anns(coco)

    # Making lists of extracted data columns
    img_ids = [ann['image_id'] for ann in anns]
    img_names = [images.loc[img_id, 'FILE_NAME'] for img_id in img_ids]
    class_ids = [ann['category_id'] for ann in anns]
    classes = [class_df.loc[class_id, 'CLASS'] for class_id in class_ids]
    if normalize:
        xmins = [
            ann['bbox'][0] / images.loc[ann['image_id'], 'WIDTH']
            for ann in anns
        ]
        ymins = [
            ann['bbox'][1] / images.loc[ann['image_id'], 'HEIGHT']
            for ann in anns
        ]
        xmaxs = [
            (ann['bbox'][0] + ann['bbox'][2])
            / images.loc[ann['image_id'], 'WIDTH']
            for ann in anns
        ]
        ymaxs = [
            (ann['bbox'][1] + ann['bbox'][3])
            / images.loc[ann['image_id'], 'HEIGHT']
            for ann in anns
        ]
    else:
        xmins = [ann['bbox'][0] for ann in anns]
        ymins = [ann['bbox'][1] for ann in anns]
        xmaxs = [ann['bbox'][0] + ann['bbox'][2] for ann in anns]
        ymaxs = [ann['bbox'][1] + ann['bbox'][3] for ann in anns]

    df_dict = {
        'IMAGE_ID': img_names,
        'CLASS': classes,
        'X_MIN': xmins,
        'Y_MIN': ymins,
        'X_MAX': xmaxs,
        'Y_NAX': ymaxs
    }

    # Making a Pandas Dataframe
    df = pd.DataFrame(df_dict)

    # Set IMAGE_ID as index
    df = df.set_index('IMAGE_ID')

    return df