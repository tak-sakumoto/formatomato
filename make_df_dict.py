def make_df_dict(anns, file_names, cat_names):
    """
    Making a dictionary of the extracted data lists
    """

    # Making lists of extracted data columns
    img_ids = [ann['image_id'] for ann in anns]
    img_names = [file_names[img_id] for img_id in img_ids]
    class_ids = [ann['category_id'] for ann in anns]
    classes = [cat_names[class_id] for class_id in class_ids]
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

    return df_dict