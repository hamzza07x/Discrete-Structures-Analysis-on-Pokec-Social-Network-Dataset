# Discrete Structures Analysis on Pokec Social Network Dataset

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Workflow](#project-workflow)
3. [Concepts Applied and Questions Addressed](#concepts-applied-and-questions-addressed)
    - [Propositions](#propositions)
    - [Quantifiers](#quantifiers)
    - [Sets](#sets)
    - [Venn Diagrams](#venn-diagrams)
    - [Functions](#functions)
    - [Relations](#relations)
    - [Induction](#induction)
    - [Permutations and Combinations](#permutations-and-combinations)
    - [Counting](#counting)
    - [Trees](#trees)
    - [Graphs](#graphs)
4. [Dataset](#dataset)
5. [Tools and Technologies](#tools-and-technologies)
6. [Requirements](#requirements)
7. [How to Run](#how-to-run)
8. [Example Output](#example-output)

## Project Overview
This project involves analyzing the Pokec Social Network dataset using concepts from discrete mathematics. Pokec is Slovakia's most popular online social network, with over 1.6 million users. The dataset includes anonymized user profiles (gender, age, hobbies, education, etc.) and friendships, offering a rich opportunity to explore real-world applications of discrete structures.

Through this project, theoretical concepts such as propositions, quantifiers, sets, relations, functions, and graph theory are applied to answer insightful questions about the data.

## Project Workflow
1. **Import the Data**  
   Parse data from the `soc-pokec-relationships.txt` and `soc-pokec-profiles.txt` files using C++ or Python.  
   Dataset can be accessed from: [Pokec Dataset](https://snap.stanford.edu/data/soc-Pokec.html).
   Make sure to keep both files in the same directory as the `.py` file.

3. **Store the Data**  
   Use appropriate data structures (e.g., structs, classes, arrays, trees, or graphs) to represent user profiles and relationships.

4. **Analyze the Data**  
   Implement discrete mathematics concepts to answer specific questions and generate insights.

## Concepts Applied and Questions Addressed

### Propositions
- Check if propositions hold for two users, such as:
  - If a user is over 30 years old, their completion percentage exceeds 50%.
  - A user is public if and only if they logged in within the last year.

### Quantifiers
- Find users meeting certain criteria, e.g.,:
  - **Exists**: A user in the `zilinsky kraj` region above 25 years old with a completion percentage above 70%.
  - **For all**: Users in a region where every user above 18 has completed at least 50% of their profile.

### Sets
- Perform operations like union, intersection, and complement:
  - Set A: All socially public users.
  - Set B: Users in Bratislava.
  - Find \( A \cup B \), \( A \cap B \), and \( A' \).

### Venn Diagrams
- Visualize overlaps between user sets (e.g., public users, users above 30, users in a specific region).

### Functions
- Map user IDs to attributes like completion percentage.
- Determine the domain, range, injectivity, and surjectivity.

### Relations
- Check properties of user relationships:
  - **Symmetry**: If A is friends with B, is B friends with A?
  - **Transitivity**: If A is friends with B and B with C, is A friends with C?
  - **Reflexivity**: Do users have a relationship with themselves?

### Induction
- Prove properties like "the number of users with completion_percentage above a threshold exceeds X" using induction.

### Permutations and Combinations
- Count subgroups (e.g., users over 25 in Bratislava) and calculate permutations (e.g., arranging users by completion_percentage).

### Counting
- Implement functions to:
  - Count users with completion_percentage above 80%.
  - Count users by region.
  - Generate a report on public profiles.

### Trees
- Represent relationships with tree structures:
  - Use preorder, postorder, and BFS traversals.

### Graphs
- Represent the network as a graph:
  - Find a bipartite subgraph of 3,000 users.
  - Calculate the Minimum Spanning Tree for a subgraph of 3,000 users.

## Dataset
The dataset contains:
- `soc-pokec-relationships.txt`: User friendships (oriented relationships).
- `soc-pokec-profiles.txt`: User profiles with attributes in Slovak.

## Tools and Technologies
- **Programming Languages**: C++ or Python
- **Data Structures**: Structs, classes, arrays, trees, graphs
- **Algorithms**: Graph traversal, MST, BFS

## Requirements
  - Python 3.x
  - (Optional) Libraries:
    - `matplotlib` (for graphical visualizations)
    - `networkx` (for graph-based algorithms)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pokec-discrete-analysis.git
   cd pokec-discrete-analysis
   ```

2.Compile
     ```bash
     python3 main.py
     ```

3. Ensure the dataset files (`soc-pokec-relationships.txt` and `soc-pokec-profiles.txt`) are in the appropriate directory.

## Example Output
You can expect output like:
- A report on users with a completion percentage greater than 80%.
- A graph showing the relationships between users (for graph-related tasks).
- Sets showing intersections, unions, and complements of user attributes.
