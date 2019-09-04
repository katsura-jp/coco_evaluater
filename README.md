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



