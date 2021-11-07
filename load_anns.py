from pycocotools.coco import COCO

def load_anns(coco):
    """
    Loading annotations
    """
    ann_ids = coco.getAnnIds()
    anns = coco.loadAnns(ann_ids)
    # Sorting annotations in ascending order by image IDs
    anns = sorted(anns, key=lambda x: x['image_id'])

    return anns