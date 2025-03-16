## BEMAP: A Novel Benchmark Suite Construction Approach for Representing User Interaction Behavior in Android Applications

1. **Problem Identified**:
    - Existing benchmark suites like **Geekbench 5.0** fail to authentically represent the **micro-architecture level performance behavior** of real Android applications, especially those with **interactive operations** (e.g., screen sliding).
    - There is a lack of tools to efficiently collect features from Android applications for benchmark selection.

2. **Proposed Solution**:
    - A novel approach called **BEMAP** (Benchmark Suite Construction Approach) is proposed to construct a supplementary benchmark suite from real-world Android applications.
    - BEMAP focuses on representing **user interaction behavior** for CPU micro-architecture design.

3. **Key Innovations in BEMAP**:
    - **Two-Stage RFC (Representative Feature Construction)**:
        - Stage 1: Identifies important performance events (e.g., IPC - Instructions Per Cycle) using **SGBRT** (Stochastic Gradient Boosted Regression Tree).
        - Stage 2: Constructs representative features using **ICA** (Independent Component Analysis).
    - **SPC-MMA (Source Performance Counters from Multiple Micro-Architectures)**:
        - Collects performance events from multiple mobile CPUs with different micro-architectures to ensure fairness.
    - **ES (Elbow-Silhouette) Approach**:
        - Determines the optimal number of clusters (**K**) for grouping Android applications using **K-Means**.
    - **AutoProfiler**:
        - A new tool designed to automatically profile micro-architecture events (e.g., IPC, L1 I-cache misses) for Android applications with interactive operations.

4. **Outcome**:
    - **SPBench**: A novel benchmark suite constructed using BEMAP, consisting of **15 benchmarks** selected from **100 real Android applications**.
    - SPBench represents **three common user interaction operations** and demonstrates significantly higher accuracy in representing micro-architecture performance behaviors compared to state-of-the-art approaches.

5. **Experimental Validation**:
    - SPBench was tested on **four significantly different micro-architectures** and proved effective in representing real-world application performance.

---

### Keywords
- Benchmark suite
- Micro-architecture performance
- Android applications
- User interaction behavior
- Performance counters
- IPC (Instructions Per Cycle)
- Machine learning (SGBRT, ICA)
- Clustering (K-Means, Elbow-Silhouette)
- AutoProfiler
- SPBench
- Geekbench 5.0

---

### Performance Issues
- Inaccurate representation of real-world application behavior in existing benchmarks.
- Lack of tools for efficient feature collection in Android applications.
- Difficulty in ensuring fairness across different micro-architectures.
- Challenges in profiling interactive operations (e.g., screen sliding).