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

## Thesis 2 Plan

Thesis 1 is complete now to proceed with thesis 2, and incorporating feedback from thesis 1. 

### Thesis 1 feedback
- No such research on pre idea step, mainly there is no research done on how we came to select our topic
- No work or research has been done on resource management

### Thesis 2 Plan
- Do work on pre-topic research, and extract issues work
  - Find papers with android terms related to optimisation
  - Find issues in github, stack overflow and playstore reviews
  - Make a list of issues and then we select an issue matching one regarding to APK analysis
  - And compile the work and then compile it into the thesis report
- Work on resource management
  - Find papers on resource management optimisation
  - Alter script to show contribution share of resources in an APK vs the other files
- Complete work on Dependency optimisation 
  - Find some research on how to recommend libraries, and model it to our data
  - Make a script to test the model on projects
  - Compare script results with other tools 
- Compile all above steps to existing documents for final thesis report