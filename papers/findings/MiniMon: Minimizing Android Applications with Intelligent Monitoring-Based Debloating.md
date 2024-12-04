# MiniMon: Minimizing Android Applications with Intelligent Monitoring-Based Debloating

https://dl.acm.org/doi/pdf/10.1145/3597503.3639113

- Android application has many features, but not all used by the consumer
- Minimon - removes code of unnecessary or unused features and makes the application
- **MethodGeneralizer** - to identify what features are being used
  - No existing data
  - Used custom benchmark 
  - 41 applications to generate data
- Some technical work done to get users actions, and then using static analysis identify usages and then eliminate them 
and recompile the application
- Link to minimon https://zenodo.org/records/10149997
- Tools like R8 already remove unused code from application, but running before R8, also shows positive results

### Learnings taken from the paper

- Minimon has to be installed and checked how to run it on application
- If we are able to run Minimon, we can compare results using our prepared script, to compare our approach
- We have to compare our approach before running R8 and after running R8 as well as Minimon
- Technique used in this paper might not be useful to us, but the end result of de-bloating application can be used for a comparative analysis