# DSA Coursework: Sorting Algorithms Experiment

## Overview
This project compares the performance of two sorting algorithms:
- Selection Sort: O(n²)
- Merge Sort: O(n log n)
The experiment measures how long each algorithm takes to sort lists of different sizes.

## Files
- 'selection_sort.py': Contains the Selection Sort algorithm.
- 'merge_sort.py': Contains the Merge Sort algorithm.
- 'test_sorts.py': Tests both sorting algorithms.
- 'experiment.py': Runs the timing experiments.
- 'plotter.py': Creates the performance graph.
- 'DSA_Coursework_Report.pdf': Contains the written report.
- 'DSA_AI_Declaration_CoverSheet.pdf': AI declaration cover sheet.
- 'AI_Prompt_Log.docx': Record of AI prompts used during the coursework.

## Requirements
- Python 3.x
- Matplotlib

Install Matplotlib using:
```bash
pip install matplotlib
```

## How to Run
### 1. Test the Sorting Algorithms
Run:
```bash
python test_sorts.py
```
This checks whether both sorting algorithms work correctly on different inputs, including:
- Already sorted lists
- Lists with repeated values
- Unsorted lists

### 2. Run the Experiment
Run:
```bash
python experiment.py
```
The experiment:
- Tests input sizes of 500, 1000, 2000, 4000, and 8000.
- Runs five random trials for each input size.
- Calculates the mean running time.
- Measures Selection Sort on already sorted lists.
- Measures only the sorting time.

### 3. Generate the Graph
Run:
```bash
python plotter.py
```
This creates a graph showing the running times of:
- Selection Sort on random lists
- Merge Sort on random lists
- Selection Sort on already sorted lists

The graph uses:
- Input size `n` on the x-axis
- Time in seconds on the y-axis

## Results
The experiment shows that:
- Selection Sort takes approximately O(n²) time.
- Merge Sort takes approximately O(n log n) time.
- Selection Sort remains slow even when the input list is already sorted.
- Merge Sort performs better than Selection Sort on larger datasets.
- Selection Sort may be suitable for small datasets because it is simple and uses little extra memory.

## Conclusion
Merge Sort is the better choice for sorting large datasets because its O(n log n) time complexity allows it to perform more efficiently as the input size increases.
Selection Sort is simpler and uses constant extra space, but its O(n²) time complexity makes it less suitable for large datasets.
