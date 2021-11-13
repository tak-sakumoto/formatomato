import pandas as pd

def write_df_csv(
    ann_df, image_df, class_df,
    output_csv_path, output_image_csv_path,
    output_class_csv_path
):
    """
    Writing CSVs based on Pandas Dataframe 
    """
    # Saving the Pandas Dataframe for classes to a CSV file
    ann_df.to_csv(output_csv_path)
    # Saving the Pandas Dataframe to a CSV file
    image_df.to_csv(output_image_csv_path)
    # Saving the Pandas Dataframe for classes to a CSV file
    class_df.to_csv(output_class_csv_path)