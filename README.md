TSP
1. SLS - Simulated Annealing with 2-Opt and Nearest Neighbor
2. BnB

SLS (Folder Structure)
1. Competition - Results csv file containing the outputs for the competition problems - Input,Route,Best Distance,Time; text file generated as per the submission instruction (check canvas)
2. TestRuns
   * Inputs - problems generated using generate_TSP.py. 20 files for each from Nodes [100,300,500,800,1000] were generated with mix of k,mean,variance combinations. This is for convenience to evaluate the performance on diverse set of inputs
3. SLS Algorithm
   * Plot2.0 - contains various plots (self explained)
   * bestSoFar - actual implementation of SA
   * Results Generate - structured to generate output for n files
