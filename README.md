# Reductions: Vertex Cover and 3-Satisfiability

## Project Overview
This assignment engages with the concept of reductions, specifically showcasing the NP-Hardness of the Vertex Cover Problem through a reduction from the 3-Satisfiability Problem. The documentation is divided into two main sections: an exploration of the Vertex Cover Problem and a detailed explanation of its reduction to 3-SAT.

## Part 1: The Vertex Cover Problem
This section introduces the Vertex Cover Problem as a decision problem, where the objective is to identify a vertex cover of a given cardinality within a graph. We provide an overview of the brute-force algorithm implemented in `vertex_cover.py`, highlighting its usage as both an independent script and a Python module.

## Part 2: The 3-Satisfiability Problem
A brief exposition on the 3-Satisfiability Problem, or 3-SAT, precedes a meticulous illustration of the reduction from 3-SAT to Vertex Cover. This section elucidates the seamless translation of a 3-SAT instance into an equivalent Vertex Cover instance. An imperative part of the task is implementing a polynomial-complexity algorithm to determine the satisfiability of 3-SAT, leveraging the provided `vertex_cover` implementation.

### Example Usage
```bash
$ ./compile.sh
$ ./run.sh input_proposition.txt
Satisfying assignment:
~p, q, ~r

