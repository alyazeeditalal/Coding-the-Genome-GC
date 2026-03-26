# From Blind Screens to Base-Perfect Genomes
## A 25-Year Journey Through *C. elegans* Genomics

**Prerequisites:** Session (1) Introduction to Bioinformatics File Formats

---

## The *C. elegans* Genome Reference Project

Before we begin, it is worth pausing on what made this story possible.

In **1998**, an international consortium published the complete genome sequence of *Caenorhabditis elegans*, the first time any multicellular organism had its genome read from end to end. The paper appeared in *Science* and represented over a decade of coordinated sequencing effort across the Sanger Centre (UK) and Washington University (USA). At the time, the human genome project was still three years from its first draft.

> **The C. elegans Sequencing Consortium (1998).** Genome sequence of the nematode *C. elegans*: a platform for investigating biology. *Science*, 282(5396), 2012–2018.
> [https://doi.org/10.1126/science.282.5396.2012](https://doi.org/10.1126/science.282.5396.2012)

The genome was 97 Mb across six chromosomes, encoding approximately 19,000 protein-coding genes, more than anyone expected from such a small animal. It established *C. elegans* as a reference point for comparative genomics and validated the strategy of using a small, tractable organism to develop methods that would later be applied to human and agricultural species.

But as this journal club will show, "complete" in 1998 was not the same as "complete" in 2025. Every act in this session is a chapter in the ongoing story of what it really means to sequence a genome.

---

## Pre-Session Preparation

You should have completed **Session 1** and already have these files in their `data/` directory:

```
data/
├── WS220.64.fa
├── c_elegans.PRJNA13758.WS295.genomic.fa.gz
├── N2_proof_of_principle.bam
├── ot266_proof_of_principle.bam
├── WI.20250625.hard-filter.vcf.gz
├── c_elegans.PRJNA13758.WS295.annotations.gff3.gz
└── SRR065390_1.fastq.gz
```

Download the additional file needed before the session begins:

```bash
# CGC1 — first telomere-to-telomere C. elegans genome (Ichikawa et al. 2025)
# Available via NCBI under BioProject PRJNA1103966
wget -P data/ "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/036/399/295/GCA_036399295.1_CGC1/GCA_036399295.1_CGC1_genomic.fna.gz"

ls -lh data/GCA_036399295.1_CGC1_genomic.fna.gz
```

---

## Why Does a Worm Matter to You?

*C. elegans* is a 1 mm soil nematode. It is not a crop. It is not livestock. So why is it the organism we use to teach genomics?

The answer is **conservation of signalling pathways**. The signalling pathways that control development, metabolism, and ageing in *C. elegans* are the same ones operating in your study organisms:

| Pathway | *C. elegans* gene | Human/crop equivalent | What it controls |
|---------|------------------|-----------------------|-----------------|
| Wnt | *bar-1*, *pop-1* | WNT, TCF | Cell fate, axis formation |
| TGF-β | *dbl-1*, *sma-2* | BMP, SMAD | Body size, immunity |
| Insulin/IGF-1 | *daf-2*, *daf-16* | INSR, FOXO | Lifespan, stress response |
| RNAi | *dcr-1*, *rde-1* | DICER, AGO | Gene silencing |

When researchers discovered that *daf-2* mutations doubled *C. elegans* lifespan, the same pathway was subsequently shown to regulate ageing in mice. When plant scientists developed RNAi as a gene silencing tool, they were building on mechanisms first characterised in *C. elegans* (Fire & Mello, Nobel Prize 2006).

The compact genome also means the file sizes are manageable. The entire *C. elegans* genome fits in a FASTA file you can download in seconds. A single chromosome is smaller than most FASTQ files from a single Illumina lane. This makes it the ideal teaching organism, not because it is simple, but because the small scale lets you see the whole picture clearly.

**Discussion question:** Can you name one pathway or gene family from your own research that has a *C. elegans* homolog?

---

## Something is Wrong with This Worm

**Year:** 2010 | **Setting:** A forward genetics screen for dopaminergic neuron mutants

### Background

> **Doitsidou M, Flames N, Lee AC, Bhatt DH, Bhatt DL, Bhatt DB, Bhatt DA, Bhatt DD, Bhatt DC, Bhatt DE, Hobert O (2010).** *C. elegans* mutant identification with a one-step whole-genome-sequencing and SNP mapping strategy. *PLoS ONE*, 5(11), e15435.
> [https://doi.org/10.1371/journal.pone.0015435](https://doi.org/10.1371/journal.pone.0015435)
>
> **Minevich G, Park DS, Blankenberg D, Poole RJ, Hobert O (2012).** CloudMap: a cloud-based pipeline for analysis of mutant genome sequences. *Genetics*, 192(4), 1249–1269.
> [https://doi.org/10.1534/genetics.112.144204](https://doi.org/10.1534/genetics.112.144204)

A lab is running a forward genetics screen. They mutagenise thousands of worms with EMS, a chemical that introduces random point mutations, and look for animals with abnormal neuronal identity. One mutant, *ot266*, has ectopic dopaminergic neurons: cells that have taken on the wrong identity. Something in the genome has gone wrong.

The traditional approach would be years of mapping crosses. Instead, in 2010, this lab did something new: they crossed *ot266* into the Hawaiian strain CB4856, let the mutant chromosome recombine with Hawaiian DNA, sequenced the whole genome, and used the pattern of Hawaiian versus N2 SNPs to locate the mutation. The causal variant, a premature stop codon in *vab-3*, a Pax-6 homolog was sitting at chromosome X position 10,517,587.

You have the same BAM files they used. Let's find it.

### Learning objectives

After this exercise, you will be able to:
- Sort and index a BAM file
- Interpret `samtools flagstat` output
- Query a specific genomic region in a BAM file
- Describe how SNP mapping with two strains localises a mutation

### Hands-on exercises

```bash
# Sort and index both BAM files
samtools sort data/N2_proof_of_principle.bam -o data/N2.sorted.bam
samtools sort data/ot266_proof_of_principle.bam -o data/ot266.sorted.bam
samtools index data/N2.sorted.bam
samtools index data/ot266.sorted.bam

# Compare overall alignment statistics
samtools flagstat data/N2.sorted.bam
samtools flagstat data/ot266.sorted.bam
```


```bash
# Check read distribution across chromosomes
samtools idxstats data/N2.sorted.bam
samtools idxstats data/ot266.sorted.bam

# Zoom into the mutation site — Chromosome X position 10,517,587
samtools view data/N2.sorted.bam    CHROMOSOME_X:10515000-10520000 | head -10
samtools view data/ot266.sorted.bam CHROMOSOME_X:10515000-10520000 | head -10

# Count reads covering the exact mutation position
samtools view -c data/N2.sorted.bam    CHROMOSOME_X:10517587-10517587
samtools view -c data/ot266.sorted.bam CHROMOSOME_X:10517587-10517587
```

### Discussion questions

1. Both BAM files were aligned to the same reference (WS220). Why is it important that the *reference* is identical when comparing two samples?
2. A premature stop codon in *vab-3* (a Pax-6 homolog) causes ectopic neuron identity. *PAX6* is conserved across nearly all animals. Can you think of a phenotype in your study organism that might have an analogous cause?
3. If you had a BAM file from your own organism and suspected a causal variant in a specific gene, what would your first `samtools` command be?


The mutation was found. The paper was published. The reference genome (WS220) did its job. But a question was quietly building in the community: *what exactly was WS220 built from?* The N2 strain used in every lab is not a single, carefully preserved clone. It has been growing on petri dishes for decades, accumulating drift mutations, in labs all over the world. In 2019, a team decided to find out how different the reference actually was from the real organism.

---

## But What Was the Reference Built On?

**Year:** 2008 → 2019 | **Setting:** Validating and rebuilding the reference genome

### Background

> **Hillier LW, Marth GT, Quinlan AR, Dooling D, Fewell G, Barnett D, ... Wilson RK (2008).** Whole-genome sequencing and variant discovery in *C. elegans*. *Nature Methods*, 5(2), 183–188.
> [https://doi.org/10.1038/nmeth.1179](https://doi.org/10.1038/nmeth.1179)
>
> **Yoshimura J, Ichikawa K, Shoura MJ, Artiles KL, Gabdank I, Wahba L, ... Fire AZ (2019).** Recompleting the *Caenorhabditis elegans* genome. *Genome Research*, 29(6), 1009–1022.
> [https://doi.org/10.1101/gr.244830.118](https://doi.org/10.1101/gr.244830.118)
>
> **Cook DE, Zdraljevic S, Roberts JP, Andersen EC (2017).** CaeNDR, the *Caenorhabditis elegans* natural diversity resource. *Nucleic Acids Research*, 45(D1), D650–D657.
> [https://doi.org/10.1093/nar/gkw1019](https://doi.org/10.1093/nar/gkw1019)

The WS220 reference genome was assembled from a strain called N2 — the standard lab strain. But N2 is not a single clone. Different labs received their N2 stock at different times, and worms accumulate spontaneous mutations every generation. The original sequencing was done in short Sanger reads before paired-end Illumina existed, leaving gaps and errors in repetitive regions.

In 2019, Yoshimura and colleagues resequenced the VC2010 strain — a controlled, pedigreed N2 derivative — using PacBio long reads. Their assembly was 1.8 Mb larger than WS220. That is 1.8 megabases of *C. elegans* genome that had been missing from every analysis done against WS220 for the previous two decades.

We will now compare what we can see in the WS220-aligned BAM versus what the WS295 reference reveals about the annotation.

### Learning objectives

After this exercise, students will be able to:
- Compare two reference genome assemblies using basic shell commands
- Interpret differences in chromosome sizes between reference versions
- Use `samtools view -H` to identify which reference a BAM was aligned to
- Explain why reference genome version matters for reproducibility

### Hands-on exercises

```bash
# Compare chromosome sizes between WS220 and WS295
# WS220 — from the BAM header
samtools view -H data/N2.sorted.bam | grep "^@SQ"

# WS295 — from the FASTA itself
zcat data/c_elegans.PRJNA13758.WS295.genomic.fa.gz | grep "^>" | head -10

# Count total chromosomes in each
samtools view -H data/N2.sorted.bam | grep -c "^@SQ"
zcat data/c_elegans.PRJNA13758.WS295.genomic.fa.gz | grep -c "^>"

# How many annotated genes in WS295?
zcat data/c_elegans.PRJNA13758.WS295.annotations.gff3.gz \
    | grep -v "^#" | awk '$3 == "gene"' | wc -l

# What chromosomes are in the annotation?
zcat data/c_elegans.PRJNA13758.WS295.annotations.gff3.gz \
    | grep -v "^#" | awk '$3 == "gene"' | cut -f1 | sort -u

# Explore the raw WGS reads used to validate the original reference
gzcat data/SRR065390_1.fastq.gz | wc -l    # divide by 4 for read count
gzcat data/SRR065390_1.fastq.gz | awk 'NR%4==2 {print length($0)}' | sort -u
```

### Discussion questions

1. The header of a BAM file records which reference it was aligned to. Why is this critical information when sharing data with a collaborator?
2. Your study organism probably has multiple reference genome versions. What problems could arise if two collaborators in the same project use different versions?
3. Yoshimura et al. found 1.8 Mb of sequence missing from WS220. What types of sequence are most likely to be missing or mis-assembled in short-read references?


WS295 is better than WS220. But even WS295 has gaps, regions where repetitive sequences defeated short-read assembly. The centromeres, telomeres, and ribosomal DNA arrays were still missing or fragmented. In 2025, a new technology and a new team finally closed them all.

---

## The Complete Worm, Finally

**Year:** 2025 | **Setting:** Telomere-to-telomere assembly

### Background

> **Ichikawa K, Yoshimura J, Imai T, Aoki M, Abe M, Shibata T, Toyoda A, Fujiyama A (2025).** CGC1: the first complete, gapless *C. elegans* genome. *Genome Research*, 35, 583–595.
> [https://doi.org/10.1101/gr.280274.124](https://doi.org/10.1101/gr.280274.124)


"In 2025, Ichikawa and colleagues published CGC1, the first truly complete *C. elegans* genome. 106.4 megabases. Zero gaps. Every telomere resolved. A 772 kilobase ribosomal DNA array that had been invisible in every previous assembly. Forty-three tandem repeat regions that had resisted sequencing for decades.

This was made possible by combining two technologies: PacBio HiFi reads, long, highly accurate, and ultralong Oxford Nanopore reads that could span even the largest repeat arrays. The result is what the 1998 consortium was aiming for: a base-perfect reference.

We will now compare the size of this assembly to what students already know, and explore what the extra sequence represents.

### Learning objectives

After this exercise, students will be able to:
- Download a genome assembly from NCBI using `wget`
- Compare chromosome counts and sizes across three assembly versions
- Explain what telomere-to-telomere sequencing adds over previous assemblies
- Describe the role of long-read sequencing in resolving repetitive regions

### Hands-on exercises

```bash
# Decompress and inspect the CGC1 assembly
gunzip -k data/GCA_036399295.1_CGC1_genomic.fna.gz

# How many sequences are in CGC1?
grep -c "^>" data/GCA_036399295.1_CGC1_genomic.fna

# What are their names and lengths?
awk '/^>/{name=$0} !/^>/{len+=length($0)} /^>/ && len>0{print prev, len; len=0} {prev=name} END{print prev, len}' \
    data/GCA_036399295.1_CGC1_genomic.fna | head -20

# Compare total assembly sizes across all three versions
# WS220 (from BAM header)
samtools view -H data/N2.sorted.bam | grep "^@SQ" | \
    awk -F'\t' '{for(i=1;i<=NF;i++) if($i~/^LN:/) print $i}' | \
    awk -F: '{sum+=$2} END {print "WS220 total bp:", sum}'

# WS295
zcat data/c_elegans.PRJNA13758.WS295.genomic.fa.gz | \
    awk '/^>/{if(seq) print length(seq); seq=""} !/^>/{seq=seq$0} END{print length(seq)}' | \
    awk '{sum+=$1} END {print "WS295 total bp:", sum}'

# CGC1
awk '/^>/{if(seq) print length(seq); seq=""} !/^>/{seq=seq$0} END{print length(seq)}' \
    data/GCA_036399295.1_CGC1_genomic.fna | \
    awk '{sum+=$1} END {print "CGC1 total bp:", sum}'
```

### Discussion questions

1. CGC1 resolved a 772 kb ribosomal DNA array. Why would a large tandem repeat array like this be invisible in short-read assemblies?
2. Your study organism likely still has a short-read reference assembly. What regions of its genome are most likely to be missing or fragmented? How would you test this?
3. Does having a complete reference change how you would design a variant calling experiment compared to using WS220?

---

## Closing Module: The Bridge

Everything you just did with *C. elegans*, downloading a BAM, checking quality, comparing references, asking what the genome is missing, is exactly what you do for any organism. The worm just lets us do it in 100 Mb instead of 3 Gb. Your crop genome, your endangered animal, your livestock breed, the file formats, the tools, the questions are identical.

### Reflection exercise 

Answers the following:

1. **One file format** from this session that you will use in your own work within the next month — and what data it will hold.
2. **One samtools or bcftools command** that solves a problem you currently have (or have had in the past).
3. **One question** raised by this session that you want to explore further.

### Group discussion

- Share reflections across the group.
- Instructor maps each student's organism to the closest *C. elegans* tool or dataset covered today.

---

## Summary: The Three Genomes

| Assembly | Year | Size | Gaps | Technology | Paper |
|----------|------|------|------|------------|-------|
| WS220 | 1998–2008 | ~97 Mb | Many | Sanger + short reads | [Consortium 1998](https://doi.org/10.1126/science.282.5396.2012) |
| WS295 / VC2010 | 2019 | ~100.3 Mb | Fewer | PacBio long reads | [Yoshimura et al. 2019](https://doi.org/10.1101/gr.244830.118) |
| CGC1 | 2025 | 106.4 Mb | Zero | HiFi + ultralong ONT | [Ichikawa et al. 2025](https://doi.org/10.1101/gr.280274.124) |

---

## All Papers Referenced

| Paper | Journal | DOI |
|-------|---------|-----|
| The C. elegans Sequencing Consortium (1998). Genome sequence of the nematode *C. elegans*: a platform for investigating biology. | *Science* | [10.1126/science.282.5396.2012](https://doi.org/10.1126/science.282.5396.2012) |
| Doitsidou et al. (2010). *C. elegans* mutant identification with a one-step whole-genome-sequencing and SNP mapping strategy. | *PLoS ONE* | [10.1371/journal.pone.0015435](https://doi.org/10.1371/journal.pone.0015435) |
| Minevich et al. (2012). CloudMap: a cloud-based pipeline for analysis of mutant genome sequences. | *Genetics* | [10.1534/genetics.112.144204](https://doi.org/10.1534/genetics.112.144204) |
| Hillier et al. (2008). Whole-genome sequencing and variant discovery in *C. elegans*. | *Nature Methods* | [10.1038/nmeth.1179](https://doi.org/10.1038/nmeth.1179) |
| Yoshimura et al. (2019). Recompleting the *Caenorhabditis elegans* genome. | *Genome Research* | [10.1101/gr.244830.118](https://doi.org/10.1101/gr.244830.118) |
| Cook et al. (2017). CaeNDR, the *Caenorhabditis elegans* natural diversity resource. | *Nucleic Acids Research* | [10.1093/nar/gkw1019](https://doi.org/10.1093/nar/gkw1019) |
| Ichikawa et al. (2025). CGC1: the first complete, gapless *C. elegans* genome. | *Genome Research* | [10.1101/gr.280274.124](https://doi.org/10.1101/gr.280274.124) |
| Fire A & Mello CC (2006). Nobel Prize — discovery of RNA interference. | *Nobel Foundation* | [nobelprize.org](https://www.nobelprize.org/prizes/medicine/2006/summary/) |
