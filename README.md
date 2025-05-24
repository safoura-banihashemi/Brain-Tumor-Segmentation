# Brain-Tumor-Segmentation

This project presents a deep learning-based pipeline for brain tumor segmentation using MRI scans. Leveraging a U-Net architecture, the model is trained to accurately detect tumor regions within brain images. The performance of the model is evaluated using Dice coefficient and loss metrics, ensuring reliable segmentation results.

Interactive demo live 👉 https://t.co/8WimhfZKKn

<p align="left"> <img src="images/GrdyWe8XAAAfHaK.png" width="400">


## Database (BraTS2020 Dataset)


<img src="https://production-media.paperswithcode.com/datasets/f8984c79-9923-41af-9d18-18510cd1ae82.png" width="400"/>


The dataset contains 3D MRI images in NIfTI format (.nii.gz). Each patient record includes four MRI modalities and one segmentation mask:

T1: Native Scan

T1ce: Contrast-Enhanced T1 Scan

T2: T2-Weighted Scan

FLAIR: Fluid-Attenuated Inversion Recovery Scan

Segmentation masks represent labeled regions as follows:

0: Background (no tumor)

1: Non-Enhancing Tumor Core

2: Peritumoral Edema (swelling around the tumor)

3: Missing label

4: Enhancing Tumor

## U-Net Architecture

## Loss

## Results 

 Model evaluation on the test set:
Loss : 0.0272
MeanIOU : 0.8153
Dice coefficient : 0.7609
Precision : 0.9943
Sensitivity : 0.9942
Specificity : 0.9981
Dice coef Necrotic : 0.6286
Dice coef Edema : 0.7101
Dice coef Enhancing : 0.7049

