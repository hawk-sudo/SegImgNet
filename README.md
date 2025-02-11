# SegImgNet

# SegImgNet-Retinal-disease-Classification
<p align="justify">
SegImgNet: Segmentation-Guided Dual-Branch Network for Retinal Disease Diagnoses
</p>
Project Status: [inprocessing]

### Objective
<p align="justify">
This project aims to detect disease using retinal images.
</p>

### Partner
<p align="justify">
Xinwei Luo, Songlin Zhao, Yun Zong, Yong Chen, Gui-shuang Ying, Lifang He
</p>

### Methods Used
* Deep Learning
* Machine Learning
* Unet
* ConvNeXt

### Technologies
* Python
* Jupyter
* Numpy
* OpenCV
* Pytorch

### Needs of this project
* Data Augmentation
* Data Processing
* Deep Learning Modeling
* Evaluation and Reporting

### Project Description
* Pretraining segmentation module for retinal structures segmentation.
* Labeling image data according to the class (Normal or Disease).
* Dividing data into train, validation, and test set.
* ROSE oversampling to generate the minority class images to handle class imbalance issues in the trainset.
* Data preparation includes changing images to arrays, resizing, and normalizing.
* Implementing SegImgNet to classify Retinal images.
* Train models and provide evaluation reports.

### Getting Started
1. Prepare the Pytorch >=2.0 version and Python >=3.6. Download and install this repo.
```
git clone https://github.com/hawk-sudo/SegImgNet.git
```
2. Move to this repo and install the environment.
```
conda env create -f SegImgNet.yaml
```
You may need to install conda first.

3. Pretrain the Unet on segmentation dataset. The pretrain code will provided later.

4. Organizing the dataset for classification task. The dataset should be organized into the following format. We do not provide the dataset for privacy reasons.
```
root_directory/fold_indix/train_set
root_directory/fold_indix/val_set
root_directory/fold_indix/test_set

For each set:
├── class1/
│   ├── img1.jpg
│   ├── img2.png
│   ├── ...
├── class2/
│   ├── img1.jpg
│   ├── img2.png
│   ├── ...
├── class3/
│   ├── img1.jpg
│   ├── img2.png
│   ├── ...
└── ...

```
5. Launch the Jupyter Notebook SegImgNet.ipynb and change the param according to your settings. 

### Acknowledgements
This codebase is built based on the (https://github.com/huggingface/pytorch-image-models). Thank you!
