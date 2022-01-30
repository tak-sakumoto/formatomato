import pandas as pd
from PIL import Image
from pathlib import Path

from parse_args import parse_args

def main():
    # Parsing arguments
    args = parse_args()
    input_dataset_path = args.input_dataset_path
    input_csv_path = args.input_csv_path
    input_image_csv_path = args.input_image_csv_path
    input_class_csv_path = args.input_class_csv_path
    output_image_dir_path = Path(args.output_image_dir_path)
    normalize = args.normalize

    # Get a Pandas Dataframe of the extracted data lists
    df = pd.read_csv(input_csv_path)
    # Get a Pandas Dataframe of image infomation
    image_df = pd.read_csv(input_image_csv_path)
    # Get a Pandas Dataframe of class infomation
    class_df = pd.read_csv(input_class_csv_path)

    output_image_dir_path.mkdir(exist_ok=True)

    # Loop for images
    for idx, row in image_df.iterrows():
        img_path = Path(input_dataset_path) / row['FILE_NAME']
        img_stem = img_path.stem
        img = Image.open(img_path)
        width = img.width
        height = img.height
        anns_df = df.loc[df['IMAGE_NAME'] == row['FILE_NAME']]

        # Loop for annotations in the image
        for idx_ann, ann in anns_df.iterrows():
            # Get the coordinate values of bbox
            x_min, y_min, x_max, y_max\
                = ann['X_MIN'], ann['Y_MIN'], ann['X_MAX'], ann['Y_MAX']
            # Get the label ID
            label = class_df.loc[class_df['CLASS'] == ann['CLASS']].values[0][0]

            # Cropping the image by the bbox
            img_cropped = img.crop((x_min, y_min, x_max, y_max))
            # Saving the cropped image
            img_cropped.save(
                Path(output_image_dir_path) / '{}_bbox_{:04d}_label_{:04d}.jpg'.format(img_stem, idx_ann, label),
                quality=100, subsampling=0)
    
    return 0

if __name__ == '__main__':
    exit(main())