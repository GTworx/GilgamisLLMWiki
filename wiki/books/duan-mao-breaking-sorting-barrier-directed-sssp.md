# Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

## Metadata
- **Index**: Work 939
- **Author(s)**: [[ran-duan]], [[jiayi-mao]], [[xiao-mao]]
- **Genre(s)**: [[pure-and-applied-mathematics]], [[data-science-and-scientific-computing]]
- **Key Themes**: [[computational-complexity-and-algorithmic-limits]], [[scientific-methodology-falsification-and-metascience]]

## Summary
Achieves a historic algorithmic breakthrough in graph theory, breaking the 40-year sorting barrier for the Directed Single-Source Shortest Path (SSSP) problem with non-negative edge weights.

## Analytical Overview
### Shattering a Forty-Year Algorithmic Barrier

In *Breaking the Sorting Barrier for Directed Single-Source Shortest Paths*, theoretical computer scientists Ran Duan, Jiayi Mao, and Xiao Mao of Tsinghua University resolve one of the most celebrated open problems in fundamental algorithmic graph theory. Since Edsger Dijkstra published his seminal shortest-path algorithm in 1959, and Fredman and Tarjan optimized it with Fibonacci heaps in 1984 to $O(m + n \log n)$, it was widely conjectured that computing Directed SSSP inherently required sorting the vertices by distance.

### The Sub-Logarithmic Horizon

Duan and colleagues overturn this longstanding assumption:
- They design a revolutionary algorithm that computes Directed SSSP on graphs with non-negative real edge weights in **$O(m + n \sqrt{\log n})$** time, decisively breaking below the $O(n \log n)$ sorting barrier.
- The algorithm achieves this through a novel hierarchical graph decomposition technique paired with adaptive multi-level priority buckets that bypass the information-theoretic sorting bound.

### Foundational Impact on Computer Science

Because shortest path computations underpin routing protocols, transportation logistics, network flow algorithms, and web-scale graph databases, this breakthrough marks the most significant leap in fundamental graph algorithm efficiency in four decades.

## Primary Sources
- [2025 Breakingthe Sorting Barrier for Directed Single-Source Shortest Paths.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/Math Physics_/2025 Breakingthe Sorting Barrier for Directed Single-Source Shortest Paths.pdf)
