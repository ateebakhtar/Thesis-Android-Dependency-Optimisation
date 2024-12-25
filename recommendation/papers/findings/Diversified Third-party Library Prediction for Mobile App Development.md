# Diversified Third-party Library Prediction for Mobile App Development

https://sci-hub.se/10.1109/TSE.2020.2982154

- Tool for recommendation of libraries (libSeek)
- Used Collaborative filtering and Matrix factorization for suggesting libraries
- Based on common libraries used in other application, its recommends possible libraries that can be used
- Made their own dataset, with the help of LibRadar to extract dependencies and AndroidZoo for applications on playstore
- Mentioned other tools for analyzing or detecting libraries used in apps
  - LibRadar
  - LibD 
  - LibPecker 
  - LibScout
- Work focused towards recommendation of libraries with the similarity of dependencies used on other application
- Made a dataset of Applications, libraries and their relations (https://github.com/malibdata/MALib-Dataset)

### Learnings
- Can use approaches of collaborative filtering for our analysis
- Can use similar approaches but focus more on APK size reduction and make relations accordingly
- This used libraries from playstore, might not be useful for us, since we need the size of libraries to include in our analysis
- Make a list of libraries, that can maybe be useful for us
- It also has a built-in relation between libraries used in what applications