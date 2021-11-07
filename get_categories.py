from pycocotools.coco import COCO

def get_categories(coco):
    """
    Getting category infomations from a COCO dataset
    """
    cats = coco.loadCats(coco.getCatIds())
    cat_names = [cat['name'] for cat in cats]
    supercat_names = [cat['supercategory'] for cat in cats]
    
    cat_ids = coco.getCatIds()

    return cat_names, supercat_names, cat_ids