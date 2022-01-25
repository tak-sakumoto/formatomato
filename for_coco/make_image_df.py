import pandas as pd

from for_coco.load_imgs import load_imgs

def make_image_df(dataset):
    """
    Making a Pandas Dataframe of image information
    """
    # Loading image informations
    images = load_imgs(dataset)

    # Making lists of image information columns
    image_ids = [img['id'] for img in images]
    file_names = [img['file_name'] for img in images]
    widths = [img['width'] for img in images]
    heights = [img['height'] for img in images]

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

    return image_df
