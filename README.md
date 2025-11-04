# GraphMining_Amalzen

An academic graph mining project analyzing collaboration patterns among researchers using **arXiv data**. This notebook integrates preprocessing, graph construction, centrality analysis, community detection, and network visualizations.

**GitHub Repository:** [GraphMining_Amalzen](https://github.com/Eyyyron/GraphMining_Amalzen)

---

## Resources

### Kaggle Dataset
**Source:** [arXiv Metadata — Cornell University](https://www.kaggle.com/datasets/Cornell-University/arxiv/data)  
Contains the official arXiv metadata used for this project.  

**Included files:**
- **OAI snapshot** — full raw metadata dump (large-scale version)
- **Derived subsets** used for experimentation and analysis

**Note:** The OAI snapshot file from Kaggle was converted into a CSV format using a Python script included in the GitHub repository. The script processes the JSON metadata file, extracts relevant fields, and writes them into a structured CSV file. This conversion ensures compatibility with the tools and workflows used in this project.

---

### Google Drive — Consolidated Datasets
**Folder:** [Drive Link](https://drive.google.com/drive/folders/1CIJmyuIlEqcsBHCT4kxDlWHS6oXzZSrf?usp=sharing)  

Contains preprocessed and reduced datasets used throughout this project:

| Dataset Type | Description | Filename |
|---------------|-------------|-----------|
| Full raw dataset | Complete unprocessed arXiv metadata | `raw_dataset(full).csv` |
| Sample raw dataset | Small subset for testing and debugging | `raw_dataset(sample).csv` |
| Cleaned dataset | Preprocessed and cleaned version | `cleaned_dataset.csv` |
| Trimmed dataset | Reduced-size dataset for fast experiments | `trimmed_dataset.csv` |

> **Note:** Local copies of the sample, cleaned, and trimmed datasets are included in this repository for convenience.

---