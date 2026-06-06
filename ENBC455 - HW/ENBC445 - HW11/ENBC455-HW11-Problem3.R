# Packages
install.packages("BiocManager")
BiocManager::install(c("GenomicFeatures", "AnnotationDbi", "ballgown"))

# Ensure the library and data directory are loaded
library(ballgown)
data_directory = system.file('extdata', package='ballgown')

# Create the ballgown object (Loads your data into R)
bg = ballgown(dataDir=data_directory, samplePattern='sample', meas='all')

# Define the experimental groups (0 = Wild-Type, 1 = Engineered)
pData(bg) = data.frame(id=sampleNames(bg), group=c(0,0,1,1))

# Run the statistical test for differential expression
stat_results = stattest(bg, feature='transcript', meas='FPKM', covariate='group')

# Filter the results for statistically significant DEGs (p-value < 0.05)
sig_results = subset(stat_results, stat_results$pval < 0.05)

# Number of DEGs
nrow(sig_results)

# Export the results to a TSV file
write.table(sig_results, "outputfilename.tsv", sep="\t", quote=FALSE, row.names=FALSE)