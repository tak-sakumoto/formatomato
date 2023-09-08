import re
from pycocotools.coco import COCO

def get_dataset(dataset_name, input_dataset_path):
    if re.search('coco', dataset_name, flags=re.IGNORECASE):
        dataset = COCO(input_dataset_path)
        return dataset
    elif re.search('imagenet', dataset_name, flags=re.IGNORECASE):
        dataset = input_dataset_path
        return dataset
    else:
        raise ValueError(
            'ValueError: Cannot specify the dataset \'{}\''\
            .format(dataset_name)
        )