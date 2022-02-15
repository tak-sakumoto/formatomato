# formatomato
## Introduction

This repository provides modules for converting an image dataset to CSV filess.

## Usage
1. Install Python packages by pipenv
```
$ pipenv install
```
2. Run the below command with file path arguments
```
$ pipenv run main.py \
--input_dataset_path=/path/to/dataset \
--dataset_name=<dataset_name>
```
### Arguments
| Argument | Explanation |
|-|-|
| --config_path /path/to/config.yaml | A path to an yaml file for configuration instead of giving the following arguments |
| --input_dataset_path /path/to/dataset |  A path to an input dataset |
| --dataset_name {coco, imagenet} |  A path to the input dataset  |
| --output_csv_path /path/to/annotations.csv | (optional) A path to an output CSV file for annotations |
| --output_image_csv_path /path/to/image.csv | (optional) A path to an output CSV file for images |
| --output_classes_csv_path | (optional) A path to an output CSV file for classes |
| --normalize | (optional) A flag for normalizing coordinate values of bbox |

### Input dataset
Check `--input_dataset_path`  for given `--dataset_name` 
#### `--dataset_name coco` 
Give `--input_dataset_path /path/to/coco2017/annotations_trainval2017/annotations/instances_val2017.json`

####  `--dataset_name imagenet`
Give `--input_dataset_path /path/to/ILSVRC2012/ILSVRC2012_img_train/train`

```
/path/to/ILSVRC2012/ILSVRC2012_img_train/train
    - n01440764
        - n01440764_10026.JPEG
        - n01440764_10027.JPEG
        ...
    - n01443537
        - n01443537_10007.JPEG
        - n01443537_10014.JPEG
    ...
```

### Output
The following 3 files:

| File | Explanation |
|-|-|
| out.csv | Annotations |
| out_image.csv | Image infos |
| out_classes | Defined classes |

Each file consists of the following columns.
#### out.csv
| Column | Explanation |
|-|-|
| IMAGE_ID | Image IDs |
| IMAGE_NAME | Image names |
| CLASS | Annotated class names denoting labels for each images in a classification dataset or for each bbox in a detection dataset |
| X_MIN, Y_MIN | (detection) Upper-left coordinates for each bbox |
|X_MAX, Y_MAX| (detection) Lower-right coordinates for each bbox |
|WIDTH, HEIGHT| (detection) Widths and heights for each bbox |

#### out_image.csv
| Column | Explanation |
|-|-|
| IMAGE_ID | Image IDs |
| IMAGE_NAME | Image names |
|WIDTH, HEIGHT| Widths and heights for each images |

#### out_classes
| Column | Explanation |
|-|-|
| CLASS_ID | Class IDs |
| SUPERCLASS | Superclass names |
| CLASS | Class names |


