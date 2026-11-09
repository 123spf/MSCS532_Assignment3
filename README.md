# MSCS 532 Assignment 3: Quicksort and Hash Tables

Stephanie Peguero 
MSCS532_B01

## 1\. What the Program Does

This project contains implementations and empirical analyses of two core algorithms:

* **Part 1 (Quicksort):** Implements both Randomized and Deterministic Quicksort algorithms. It compares their execution times across different array distributions (random, sorted, reverse-sorted, and heavily repeated) to demonstrate the $O(n\log n)$ average case versus the $O({n}^{2})$ worst case.

* **Part 2 (Hash Table):** Implements a Hash Table using chaining (lists) to resolve collisions. It includes fully functional `insert`, `search`, and `delete` methods, demonstrating $O(1)$ expected time complexity.

## 2\. How to Run It

Open your terminal, navigate to the directory containing the project files, and run the Python scripts:

**For Part 1 (Quicksort analysis):** `quicksort.py`

**For Part 2 (Hash Table testing):** `hashtable.py`

## 3\. Expected Output

* The Quicksort script will output the execution times (in seconds) for both sorting methods across four different array distributions of size 1000\.
  
* The Randomized Quicksort remains consistently fast ($O(n\log n)$), while the Deterministic Quicksort slows down significantly on the sorted and reverse-sorted arrays ($O({n}^{2})$).
