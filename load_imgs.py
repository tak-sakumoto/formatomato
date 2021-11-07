from pycocotools.coco import COCO

def load_imgs(coco):
    """
    Loading image informations
    """
    img_ids = coco.getImgIds()
    imgs = coco.loadImgs(img_ids)
    # Sorting images in ascending order by image IDs
    imgs = sorted(imgs, key=lambda x: x['id'])

    return imgs