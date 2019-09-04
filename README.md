# coco_evaluater
Object Detection Metrics for COCO format

## Metrics
- Average Precision
  - $AP$ : Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ]
  - $AP_{50}$ : Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ]
  - $AP_{75}$ : Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ]
  - $AP_{S}$ : Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ]
  - $AP_{M}$ : Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ]
  - $AP_{L}$ : Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ]
- Average Recall
  - $AR^{1}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ]
  - $AR^{10}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ]
  - $AR^{100}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ]
  - $AR_{S}^{100}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ]
  - $AR_{M}^{100}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ]
  - $AR_{L}^{100}$ : Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ]

## Usage
```python
import evaluate.CocoEvaluator as CocoEvaluator

# ...

# creat instance of evaluator
coco_evaluator = CocoEvaluator(coco_api, ["bbox"]) # coco_api is explained below.

# evaluation step (example for pytorch)
model.eval()
coco_evaluator.reflesh()
with torch.no_grad():
  for inputs, targets in dataloader:
    outputs = model(inputs)
    # outputs is dict("boxes", "labels", "scores")
    outputs = [{k: v.to('cpu') for k, v in t.items()} for t in outputs]
    res = {idx.item(): output for idx, output in zip(ids, outputs)}
    coco_evaluator.update(res)
coco_evaluator.synchronize_between_processes()
coco_evaluator.accumulate()
# print log
coco_evaluator.summarize()
```


## Creat COCO API Dataset
```python
from pycocotools.coco import COCO
coco_ds = COCO()
ann_id = 0
dataset = {'images': [], 'categories': [], 'annotations': []}
categories = set()
for index in range(len(dataset)):
  image, bboxes, area, iscrowd = dataset[index]
  image_id = index
  
  # -- images --
  img_dict = {}
  img_dict['id'] = image_id # index of image (int)
  img_dict['height'] = img.shape[-2] # height size of image (int)
  img_dict['width'] = img.shape[-1] # width size of image (int)

  dataset['images'].append(img_dict)

  # -- categories and annotations --
  bboxes[:, 2:] -= bboxes[:, :2] # (x1, y1, x2, y2) ---> (x1, y1, w, h)
  
  # convert torch.tensor to list
  bboxes = bboxes.tolist()
  labels = labels.tolist()
  areas = area.tolist()
  iscrowd = iscrowd.tolist()
  
  num_objs = len(bboxes)
  for i in range(num_objs):
    ann = dict(image_id=image_id, # image index : int
               bbox=bboxes[i], # bounding box : list(x1, y1, w, h)
               category_id=labels[i], # label index : int
               area=areas[i], # area : int
               iscrowd=iscrowd[i], # iscrowd : 0 or 1(bool)
               id=ann_id # annotation index : int
               )
    categories.add(labels[i])
    dataset['annotations'].append(ann)
    # increment annotation index
    ann_id += 1

dataset['categories'] = [{'id': i} for i in sorted(categories)]
coco_ds.dataset = dataset
coco_ds.createIndex()

# coco_ds is COCO API Dataset
```

