<div align="center">

# Smoking Status Prediction

### Machine Learning Workflow for Classifying Smoking Status from Health Records

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

</div>

## Overview

This repository contains an end-to-end data science project for predicting a person's smoking status from health and lifestyle records. It documents the work in three complementary notebooks: exploratory analysis, explanatory analysis, and the final modeling workflow.

The project keeps the original data, a generated input sample, and the code used to create additional data for experimentation in one place.

## Contents

- [Project workflow](#project-workflow)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Data](#data)
- [Notes](#notes)

## Project Workflow

1. **Explore** - inspect distributions, missing values, and relationships in the health records.
2. **Explain** - turn the main findings into focused visual analysis.
3. **Model** - prepare features and train/evaluate a smoking-status classifier in the final notebook.
4. **Experiment** - use `generate_data.py` and `your_data.csv` for additional inputs.

## Repository Structure

```text
.
├── exploratory_notebook.ipynb       # Initial data exploration
├── explanatory_notebook.ipynb       # Communicated analysis and visualizations
├── Final_notebook.ipynb             # Final prediction workflow
├── Data.csv                          # Source health-record dataset
├── your_data.csv                     # Additional generated input data
├── generate_data.py                  # Data-generation helper
└── README.md                          # Project guide
```

## Getting Started

Create a Python environment and install the notebook dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then open the notebooks in the suggested order:

1. `exploratory_notebook.ipynb`
2. `explanatory_notebook.ipynb`
3. `Final_notebook.ipynb`

## Data

`Data.csv` is the project dataset used by the notebooks. `your_data.csv` is an additional generated data file. Keep both files beside the notebooks so their relative paths continue to work.

## Notes

Results depend on the available data and preprocessing choices, and should not be used as medical advice or a diagnostic tool.

## Author

**Youssef Mohamed Attia**  
[GitHub](https://github.com/YoussefMohAttia) · [LinkedIn](https://www.linkedin.com/in/youssefmohattia/)
