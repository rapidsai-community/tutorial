# RAPIDS Tutorial - PyData VT 2025

This repository contains materials for the tutorial:
**GPU-Accelerated Data Science for PyData Users**

## Running the tutorial

### Brev 

For the in-person version of this tutorial we will use [NVIDIA Brev](https://brev.nvidia.com/)

### Google Colab
You can run this tutorial on Google Colab. With a basic free account, you'll have access to:
- An interactive Python environment with GPU support
- Pre-installed RAPIDS libraries (cuDF and cuML)

To run each notebook:
1. Click on the corresponding link below to open it in Google Colab
2. Change the runtime type to `T4 GPU`
3. Save your changes

#### Notebooks

| Notebook    | Link |
| ----------- | ----------- |
| 0 Welcome and Setup  | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/0.Welcome_and_Setup.ipynb) |
| 1 Intro to cuDF      | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/1.Intro_to_cuDF.ipynb) |
| 2 cudf.pandas        | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/2.cudf_pandas.ipynb) |
| 3 Intro to cuML      | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/4.Intro_to_cuML.ipynb) |
| 4 cuml.accel         | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/5.cuml_accel.ipynb) |

#### Extra content: 

| Notebook    | Link |
| ----------- | ----------- |
| cudf polars engine    | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/extras/cudf_polars_engine.ipynb) |
| cuml clustering models   | [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rapidsai-community/tutorial/blob/main/extras/cuml_clustering_models.ipynb) |

### Local 

If you have access to a GPU you can run this locally:

#### Get Notebooks and Setup Environment

In a terminal:

```bash
git clone https://github.com/rapidsai-community/tutorial
```

Once inside the repository: 

```bash
conda env create -f local-env.yaml
conda activate rapids-tutorial
```

### Get the data
During this tutorial we will use different datasets, you can get them all by 
running the cell below. 

```bash
python data_setup.py --pydata-vt
```