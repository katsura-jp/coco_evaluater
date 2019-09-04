

def mean_average_precision(gt_boxes, pr_boxes, gt_labels, pr_boxes, scores,  threshold=0.5, score_threshold=0.):
    ap_score = 0.0


    print(f'mAP@{int(threshold*100)} : {ap_score}')
    pass

def mean_average_recall(gt_boxes, pr_boxes, gt_labels, pr_boxes, scores,  threshold=0.5, score_threshold=0.):
    ar_score = 0.0

    print(f'mAR@{int(threshold*100)} : {ap_score}')
    pass