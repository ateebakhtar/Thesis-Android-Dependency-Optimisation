# Library Optimization in Android Development: A Comprehensive Study on APK Size

### Flow Diagram (v1)
These are the flow diagrams, they cover the high level views and some initial low
level ideas. This is the 1st version, more updates will happens when the working evolves.  [**Diagrams**](./diagrams/flow_diagrams.md)

### Research papers

- APK size optimisation and its tools are mentioned [**here**](./papers/ResearchPapers.md) and their respective [**findings**](./papers/findings)
- Papers regarding recommendations are mentioned [**here**](./recommendation/papers/researchPapers.md) and their respective [**findings**](./recommendation/papers/findings)

### Scripts and Outputs

- Script for compiling and extracting data from an APK is placed [**here**](./tools/scripts/main.py) and its sample
  [**output**](./tools/scripts/filtered_apk_data.csv)
- Script for extracting dependency tree for an application is placed [**here**](./recommendation/script/repoAnalysis/main.py) and its 
sample [**output**](./recommendation/script/repoAnalysis/dependency_tree.csv)
- Script for extracting repository links from github can be found [**here**](/recommendation/script/RepoLinkExtraction/extractRepos.py) and its
  [**output**](/recommendation/script/RepoLinkExtraction/github_links.csv)

### Filtered Applications flow  [**here**](/recommendation/script/filteredApplication/filtered.md)

### Dependency Extraction flow  [**here**](/recommendation/script/dependencyParsing/dependencyExtraction.md)