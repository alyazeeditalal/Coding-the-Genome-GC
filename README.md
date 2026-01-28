# Coding the Genome (CG)

[![Deploy to GitHub Pages](https://github.com/alyazeeditalal/bioinformatics_training/actions/workflows/deploy.yml/badge.svg)](https://github.com/alyazeeditalal/bioinformatics_training/actions/workflows/deploy.yml)

A dual English and Arabic language course to train the next generation of bioinformatics scientists.

**Live Course:** [https://alyazeeditalal.github.io/bioinformatics_training/](https://alyazeeditalal.github.io/bioinformatics_training/)

## About

This course is designed to provide foundational knowledge and practical skills for working with large-scale genomic data. It is developed and delivered by **Dr. Talal Al-Yazeedi** under the supervision of **Professor Khalid Amiri** at the Khalifa Centre for Genetic Engineering & Biotechnology (KCGEB), UAE University.

## Course Sessions

| Session | Topic |
|---------|-------|
| 1 | Bioinformatics File Types (FASTA, FASTQ, SAM/BAM, VCF, BED, GFF) |
| 2 | Linux Command Line Essentials |
| 3 | Navigating NCBI and UCSC Databases |
| 4 | Organising Bioinformatics Projects |

## Training Data

The `trining_datasets/` folder contains sample data files for hands-on exercises:

- `SRR10532784_1.fastq.gz` - RNA-seq reads (truncated)
- `u9_liver_100.bam` - Sheep liver aligned reads
- `sheep.snp.vcf.gz` - Sheep population SNP data (~300 samples)

## Building Locally

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/alyazeeditalal/bioinformatics_training.git
cd bioinformatics_training

# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Build the documentation

```bash
# Build HTML
sphinx-build -b html . _build/html

# Or use the Makefile
make html
```

### View locally

Open `_build/html/index.html` in your browser, or serve it locally:

```bash
python -m http.server -d _build/html 8000
```

Then visit [http://localhost:8000](http://localhost:8000)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Licence

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Authors

- **Dr. Talal Al-Yazeedi** - Course Creator - [GitHub](https://github.com/alyazeeditalal)
- **Professor Khalid Amiri** - Supervisor - [UAEU Profile](https://research.uaeu.ac.ae/en/persons/khaled-amiri/)

## Acknowledgements

- Khalifa Centre for Genetic Engineering & Biotechnology (KCGEB)
- United Arab Emirates University (UAEU)
