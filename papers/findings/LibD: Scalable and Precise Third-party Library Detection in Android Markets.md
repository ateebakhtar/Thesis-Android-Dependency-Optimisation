## LibD: Scalable and Precise Third-party Library Detection in Android Markets

https://sci-hub.se/10.1109/ICSE.2017.38

- Dataset of libraries https://github.com/IIE-LibD/libd/tree/master/liblist
- Previous approaches use clustering algorithms and feature hashing (both have a limitation of obfuscation)
- LibRadar is another tool developed on feature hashing 
- Androguard tool for finding relations between packages and classes (https://github.com/androguard/androguard)
- Has created an algorithm that has created threshold of libraries used from a large sample of applications
- How it works 
  - It has a collection of libraries that have its threshold defined
  - It has a whitelisting criteria of libraries (both mentioned in the dataset)
  - It then decompiles an application
  - Extracts libraries and finds similar or exact in its threshold
  - Libraries not found, or in the smaller threshold are then flagged
- It compared its results with LibRadar, another tool solving a similar problem
- Main usage is regarding security and vulnerabilities

### Learnings taken from the paper

- LibD and LibRadar are good tools to test our approach against it
- We have to develop an approach or use the existing datasets, to identify which libraries are good and which are not
- We need/could adopt a grouping or clustering approach, in which a group of libraries when used together gives a low APK size
- There wasnt a tool which was aiming for our optimisation so far, APK Size reduction, 
but our approach can be evaluated against these mentioned tools
- We also need to make a selections of applications (preferably open source) and collect data
  - Size of application
  - Libraries used in that application