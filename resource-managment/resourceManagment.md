## Resource Management 

#### Introduction

In today's mobile landscape, Android applications are becoming increasingly feature-rich, leading to larger app sizes and 
greater consumption of device resources such as storage and network bandwidth. Efficient asset management is therefore crucial 
for delivering optimized applications that provide a good user experience by minimizing download size, reducing storage footprint,
and improving performance. Assets, which include images, audio, video, fonts, and other static files, contribute significantly 
to an app's overall size. Without proper management, applications can become bloated with unused or inefficiently sized assets,
leading to user frustration and potential uninstalls. The primary goal of asset management in Android is to deliver only the 
necessary assets to the user's device, in the most efficient format and size possible, at the time they are needed [Configure 
on demand delivery | Google Play | Android Developers, Overview of Play Feature Delivery | Google Play | Android Developers]. 
Several strategies can be employed to achieve this, often in combination [Yes, several of the resource and asset management 
approaches can be combined to achieve even greater efficiency]. These approaches can be broadly categorized into build-time 
optimizations and runtime/delivery strategies.

- **Build-time optimizations**

  - **Resource shrinking** using tools like R8, which automatically removes unused resources from the app [jisis-2021-vol11-no1-01.pdf].
  
  - **Lint tools** for identifying and eliminating registered but unused resources [235da5ab25c9208b657efff69681707f.pdf].
  
  - Employing more advanced **static analysis** to detect and remove even more subtle forms of unused assets [235da5ab25c9208b657efff69681707f.pdf].
  
  - Asset compression to reduce the file size of existing assets [thesis_final.pdf]. Utilizing efficient asset formats like vector graphics and JSON-based animations (Lottie), which are typically smaller and more scalable than raster images or traditional animation formats [Optimal Implementation of Motion Graphic Assets on Onboarding Android Applications].

- **Runtime and delivery strategies**
  
  - Dynamic Delivery, powered by Android App Bundles (AABs), allows the Google Play Store to generate and serve optimized APKs containing only the assets relevant to a user's device configuration (e.g., screen density, language) [Configure on demand delivery | Google Play | Android Developers, Overview of Play Feature Delivery | Google Play | Android Developers].
  
  - Play Feature Delivery enables the separation of app features and their associated assets into feature modules that can be downloaded on demand, after the initial app installation [Configure on demand delivery | Google Play | Android Developers, Overview of Play Feature Delivery | Google Play | Android Developers].
  
  - Content adaptation and prioritization involve delivering frequently used assets initially and managing or downloading less common assets based on usage patterns [Where did my 256 GB go? A Measurement Analysis of Storage Consumption on Smart Mobile Devices].
  
  - For large games, strategies exist to optimize the delivery of Opaque Binary Blobs (OBB), potentially by accessing only necessary parts when needed [Where did my 256 GB go? A Measurement Analysis of Storage Consumption on Smart Mobile Devices].

#### Literature Analysis
Several papers highlight the problem of "software bloat" in Android applications. For instance, the authors of the REDDROID prototype aimed to comprehensively depict the landscape of the bloatware issue in the Android application domain for the first time. Their experimental results sought to help developers gain insights into application resource consumption and better plan their optimization strategies. Similarly, the LegoDroid approach was designed based on the finding that users access only a very small subset of app features, leading to unnecessary downloads and installations of full-sized applications. LegoDroid focuses on automatically decomposing an Android app for flexible loading and installation, aiming for a slimmer bundle that hosts only the target APIs needed by users.
In terms of build-time optimizations, various techniques and tools are discussed. Static analysis is a recurring theme, with REDDROID utilizing it to understand software bloat issues. The paper also mentions existing static analysis tools like EdgeMiner and FlowDroid. Furthermore, the use of R8 for resource shrinking, which we discussed earlier, is implicitly supported by the mention of optimization tools in general. One paper specifically compares optimization tools like R8 and ReDex. These tools play a crucial role in automatically removing unused code and resources, thereby reducing the final app size. ProGuard, another tool related to code shrinking and obfuscation, is mentioned in the context of automating its configuration using static analysis results.
Runtime and delivery strategies, which we introduced earlier, are further elaborated in the context of dynamic delivery. DeltaDroid, a test-suite augmentation approach, is presented for testing dynamic delivery in Android apps. This suggests the increasing importance of modularizing apps and delivering features and assets on demand. While not explicitly detailing asset management within dynamic delivery, this research supports the broader concept of delivering only necessary components. LegoDroid also aligns with this by advocating for flexible loading and installation based on user needs. Our previous conversation mentioned Android App Bundles (AABs) and Play Feature Delivery as key enablers of dynamic delivery, which is supported by the problem statement addressed in these research papers – the need to avoid downloading and installing unnecessary parts of an application.
Several research efforts focus on analyzing and mitigating app bloat. MiniMon, a monitoring-based debloating framework, is introduced, aiming to identify methods in an app corresponding to user-desired features that are not logged during monitoring. This approach combines monitoring with analysis to achieve a more fine-grained reduction in app size by identifying and potentially removing unused functionalities. The XDebloat approach also targets automated feature-oriented app debloating. These works demonstrate active research in automatically identifying and removing unnecessary components from Android applications, which inherently includes managing associated assets.
Furthermore, research has been conducted on understanding storage consumption behavior in Android apps. This line of work highlights the increasing need for efficient mobile storage management and proposes elastic storage designs to reclaim space occupied by inactive apps or features. While not solely focused on asset management, these studies provide valuable context on the overall problem of app size and resource usage, where assets play a significant role.
The paper on ApkDiff, a tool for matching Android app versions based on class structure, addresses the challenges in reverse engineering and analyzing updated applications. While not directly about asset management, the ability to efficiently compare app versions is valuable in understanding how assets and code change and potentially contribute to increased app size over time.
In conclusion, the provided literature underscores the significance of software bloat in Android apps and presents various research directions for mitigation. These include static and dynamic analysis techniques to identify unused code and resources, frameworks for flexible app decomposition and on-demand delivery, and tools for code and resource shrinking and optimization. The research also highlights the need for a deeper understanding of app storage consumption to devise effective management strategies. Our previous conversation about build-time and runtime asset management techniques is well-supported and expanded upon by the research presented in these sources, showcasing an active and evolving field aimed at creating leaner and more efficient Android applications.

### Build-Time Optimizations

##### Code Shrinking, Obfuscation, and Optimization:

- Android's default build process tool, R8, performs code shrinking (removing unused code), obfuscation (shortening class and member names), and optimization (applying improved code optimization strategies) to reduce app size and improve performance [Shrink, obfuscate, and optimize your app | Android Studio | Android Developers].

- Setting isMinifyEnabled = true in the build configuration enables these features [Shrink, obfuscate, and optimize your app | Android Studio | Android Developers].

- Proguard is another tool that performs similar functions to R8 [ProGuard] and its manual details configuration for usage [ProGuard manual].

- These tools work at compile-time [The Focus of This Paper 1) Compile-Time Redundancy from Java Libraries: Fig. 1b] by analyzing the application code to distinguish and remove unused library classes and methods from Java libraries [The Focus of This Paper 1) Compile-Time Redundancy from Java Libraries: Fig. 1b].

- The goal is to reduce the size of the monolithic Dalvik code file by splitting it into classes and then removing redundancies [The Focus of This Paper 1) Compile-Time Redundancy from Java Libraries: Fig. 1b].

- ReDex is another optimizer that performs minification, compression, inlining, and dead code elimination on Android bytecode [A Comparative Study on Optimization, Obfuscation, and Deobfuscation Tools in Android].

- Compiler optimizations, like inlining and call site optimization, are common during the app release process [How Does Code Optimization Impact Third-party Library Detection for Android Applications? | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering].

- Optimized bytecode methods might be removed by dex2oat, making direct comparison challenging [EuroSec ’23, May 8, 2023, Rome, Italy Jakob Bleier and Martina Lindorfer].

- R8 combines rules from various sources, including library dependencies, which can affect its behavior [Shrink, obfuscate, and optimize your app | Android Studio | Android Developers]. A full report of applied R8 rules can be generated [Shrink, obfuscate, and optimize your app | Android Studio | Android Developers].

##### Removal of Unused Resources
- Tools like Lint can remove redundant registered resources from the "Res" directory of an Android project by identifying resources not statically referred to by a field in class R [Code and File Compaction Techniques].

- However, Lint cannot optimize assets in the "Asset" directory (like music, images, animations, movies) as they are referred to by relative paths (string literals) [Code and File Compaction Techniques]. Optimization of these would require string analysis techniques [Code and File Compaction Techniques].

- Resource shrinking is also performed by R8 [A Comparative Study on Optimization, Obfuscation, and Deobfuscation Tools in Android].

##### Removal of Redundant Native Libraries (ABIs)
- Android applications often include multiple sets of embedded Application Binary Interfaces (ABIs) to support different CPU architectures, leading to install-time redundancy [Install-time Redundancy from Application Binary Inter-face and SDKs].

- Install-time redundancy refers to files that become redundant only after the installation platform is known [Install-time Redundancy from Application Binary Inter-face and SDKs].

- A significant proportion of analyzed apps contain redundant ABIs [ABI details].

- Developers sometimes include unstripped native libraries (containing debug information), increasing the app size [Unstripped native libs.]. While the percentage of such apps decreased from 2014 to 2019, it still contributes to storage pressure [Unstripped native libs.].

##### Code and File Compaction Techniques:
- Compressing Java class files into a more compact format can reduce the size of jar or apk files. This involves reorganizing class files, improving compression algorithms, and sharing information across class files [Code and File Compaction Techniques].

### Runtime and Delivery Strategies

##### Android App Bundles and Dynamic Delivery (Play Feature Delivery)

- The Android App Bundle (AAB) is a publishing format that allows for dynamic delivery [2021. Play Feature Delivery. Retrieved from https://developer.android.com/guide/playcore/dynamic-delivery., Create An Instant-Enabled App Bundle | Android Developers].

- App Bundles enable developers to modularize app features, delivering only the necessary code and resources to a specific device or when a feature is requested [2021. Play Feature Delivery. Retrieved from https://developer.android.com/guide/playcore/dynamic-delivery., Developers can also configure App Bundle or use the on-demand delivery so that only the code and resources that are needed for a specific device or feature are down-loaded].

- Play Feature Delivery allows for conditional delivery or on-demand download of app features [2021. Play Feature Delivery. Retrieved from https://developer.android.com/guide/playcore/dynamic-delivery.].

- This reduces the initial download size by providing only the code and resources needed for initial app usage [Developers can also configure App Bundle or use the on-demand delivery so that only the code and resources that are needed for a specific device or feature are down-loaded].

- Developers upload an instant-enabled app bundle to the Play Console to publish Instant Apps [Practical implementation results].

- The Play Console helps manage Play Store publications [Practical implementation results].

- Dynamic delivery can handle request errors [2021. Play Feature Delivery - Handle request errors. Retrieved from https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors].

- UX best practices exist for on-demand delivery to communicate with users [2021. UX best practices for on demand delivery. Retrieved from https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines#communicate].

##### On-Demand Delivery:

- Developers can configure their apps so that certain features are downloaded only when needed by the user [Developers can also configure App Bundle or use the on-demand delivery so that only the code and resources that are needed for a specific device or feature are down-loaded]. This is part of Play Feature Delivery [2021. Play Feature Delivery - Handle request errors. Retrieved from https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors].

##### Splitting APKs (Legacy):

- Historically, to support various devices, developers packaged multiple redundant resources in a single APK [Install-time Redundancy from Application Binary Inter-face and SDKs].

- Google encouraged publishing multiple smaller APKs, each optimized for specific device configurations [Install-time Redundancy from Application Binary Inter-face and SDKs]. App Bundles have largely replaced this manual process [Android App Bundle (AAB)].

##### Feature-Based Customization and Removal of Unused Features:
- Studies show users often use only a subset of app features, indicating feature bloat [Despite this, our study shows that there are still a large number of methods that a specific user does not need in these apps, and our work is needed for better user-specific app debloating.].

- Approaches like MiniMon aim to remove unnecessary features based on user interaction logs [MiniMon: Minimizing Android Applications with Intelligent Monitoring-Based Debloating]. MiniMon monitors executed methods and uses program analysis to identify and remove related unused code for user-specific debloating [MiniMon: Minimizing Android Applications with Intelligent Monitoring-Based Debloating]. This complements static analysis techniques [These approaches have become the default settings for Android app development, and are complementary to MiniMon. MiniMon can be run before or after R8.].

- Research explores feature-based software customization to mitigate bloat [Feature-based software customization: Preliminary analysis, for-malization, and methods].

##### "Hot" and "Cold" Code Separation (Conceptual):

- An aggressive approach involves splitting code into frequently used ("hot") and infrequently used ("cold") parts [Code and File Compaction Techniques].

- Running devices would initially receive only the hot code, with cold code remaining on a remote server and transmitted only when necessary [Code and File Compaction Techniques].

#### References

1. N. Ghorbani et al., "MiniMon: Minimizing Android Applications with Intelligent Monitoring-Based Debloating," in *Proc. Int. Conf. Softw. Eng. (ICSE)*, Lisbon, Portugal, Apr. 14–20, 2024.
2. Y. Jiang, Q. Bao, S. Wang, X. Liu, and D. Wu, "RedDroid: Android Application Redundancy Customization Based on Static Analysis," in *Proc. IEEE Int. Symp. Softw. Rel. Eng. (ISSRE)*, 2018, pp. 189–199.
3. W. Pugh, “Compressing Java Class Files,” in *Proc. ACM SIGPLAN Conf. Program. Lang. Des. Implement. (PLDI)*, 1999, pp. 247–258.
4. I. Google, “Improve Your Code with Lint,” 2017. [Online]. Available: https://developer.android.com/studio/write/lint.html#overview
5. F. Tip, C. Laffra, P. F. Sweeney, and D. Streeter, “Practical Experience with an Application Extractor for Java,” in *Proc. ACM SIGPLAN Conf. Object-Oriented Program. Syst. Lang. Appl. (OOPSLA)*, 1999, pp. 292–305.
6. Y. Jiang, D. Wu, and P. Liu, “Jred: Program Customization and Bloatware Mitigation Based on Static Analysis,” in *Proc. IEEE Annu. Comput. Softw. Appl. Conf. (COMPSAC)*, vol. 1, 2016, pp. 12–21.
7. A. Bijlani, U. Ramachandran, and R. Campbell, “Where Did My 256 GB Go? A Measurement Analysis of Storage Consumption on Smart Mobile Devices,” *Proc. ACM Meas. Anal. Comput. Syst.*, vol. 5, no. 2, Art. no. 28, 2021.
8. G. You, G. Kim, S.-j. Cho, and H. Han, “A Comparative Study on Optimization, Obfuscation, and Deobfuscation Tools in Android,” *J. Internet Serv. Inf. Secur.*, vol. 11, no. 1, pp. 2–15, 2021.
9. “Configure On-Demand Delivery | Google Play | Android Developers.” [Online]. Available: https://developer.android.com/guide/app-bundle/configure-ondemand
10. “Overview of Play Feature Delivery | Google Play | Android Developers.” [Online]. Available: https://developer.android.com/guide/app-bundle/feature-delivery
11. “Shrink, Obfuscate, and Optimize Your App | Android Studio | Android Developers.” [Online]. Available: https://developer.android.com/studio/build/shrink-code
12. “ProGuard.” [Online]. Available: https://www.guardsquare.com/proguard
13. “ProGuard Manual.” [Online]. Available: https://www.guardsquare.com/manual/home
14. “The Focus of This Paper 1) Compile-Time Redundancy from Java Libraries: Fig. 1b.”
15. “How Does Code Optimization Impact Third-Party Library Detection for Android Applications?” in *Proc. IEEE/ACM Int. Conf. Autom. Softw. Eng. (ASE)*, 2023.
16. J. Bleier and M. Lindorfer, “EuroSec ’23,” in *Proc. Eur. Workshop Syst. Secur.*, Rome, Italy, May 8, 2023.
17. “Code and File Compaction Techniques.”
18. “Install-Time Redundancy from Application Binary Interface and SDKs.”
19. “ABI Details.”
20. “Unstripped Native Libs.”
21. “Play Feature Delivery,” 2021. [Online]. Available: https://developer.android.com/guide/playcore/dynamic-delivery
22. “Create an Instant-Enabled App Bundle | Android Developers.” [Online]. Available: https://developer.android.com/guide/app-bundle
23. “Developers Can Also Configure App Bundle or Use On-Demand Delivery So That Only the Code and Resources That Are Needed for a Specific Device or Feature Are Downloaded.”
24. “Play Feature Delivery - Handle Request Errors,” 2021. [Online]. Available: https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors
25. “UX Best Practices for On-Demand Delivery,” 2021. [Online]. Available: https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines#communicate
26. “Android App Bundle (AAB).”
27. “Despite This, Our Study Shows That There Are Still a Large Number of Methods That a Specific User Does Not Need in These Apps, and Our Work Is Needed for Better User-Specific App Debloating.”
28. “Feature-Based Software Customization: Preliminary Analysis, Formalization, and...”  