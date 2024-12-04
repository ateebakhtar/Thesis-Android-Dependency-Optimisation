# A Comparative Study on Optimization, Obfuscation, and Deobfuscation Tools in Android

https://jisis.org/wp-content/uploads/2022/11/jisis-2021-vol11-no1-01.pdf

- Discusses Obfuscation and optimisation using tools 
  - R8
  - ReDex
  - Obfusapk (Not useful to us)
  - DeGuard (Not useful to us)
- D8 and Proguard were previosly being used for optimising and obfuscating
- R8 is a newer tool and does the work of both D8 and ProGuard
- R8 removes unused code, resources and in our case libraries also
- Redex minify and compress the code, and also removes dead codes
- Can be downloaded and run on an application
- Compared performance of ReDex and R8
- 3 APK's were used for analysis
- ReDex was applied after R8, which further optimised 

### Learnings taken from the paper

- We can compare our applications and approaches after running R8 and ReDex
- We can use our script, for size comparison
- We can also measure the chain of our approaches, Our Approach, R8, Redex and then compare the results