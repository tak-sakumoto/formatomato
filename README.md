# formatomato
## Introduction

This repository provides modules for converting an image dataset to a CSV file.

## Usage
1. Install Python packages by pipenv
```
$ pipenv install
```
2. Run the below command with file path arguments
```
$ pipenv run main.py \
--input_coco_path=/path/to/coco_annotations.json \
--output_csv_path=/path/to/annotations.csv \
--output_class_csv_path=/path/to/classes.csv
```
