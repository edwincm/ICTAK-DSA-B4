# P-test,T-test,z-test,F-Distribution (Dr. Sajil C. K.)

# Probability

> The ratio of the number of favorable outcomes (x) to the total number of outcomes (n) of any given event (experiment)
> Probability of any given experiment = $\frac{Favourable \ Outcomes}{Total \ Outcomes}$ = $\frac{x}{n}$

Probability is of 4 major types:
Classical Probability
Empirical Probability
Subjective Probability
Axiomatic Probability

Rare events
infinite number of experiments

Probability of getting Heads in a coin toss is 0.5 given there is an infinite number of tosses

Class work Link: [Link](https://docs.google.com/spreadsheets/d/1ADKtgwdo02B9271rPi8ELXI6BsxpCHYBdJfc532VJe8/edit?gid=0#gid=0)

Personal Work  Link: [Link](https://docs.google.com/spreadsheets/d/1EyLLEHI0oJw25xHDb4DtVCwBeu43J1e8tUun0OPM5lE/edit?gid=0#gid=0)

Probability of getting a value above a threshold: area under the curve \- integral of that range

N(Mu, sigma square)

Gaussian Curve and Normal Distribution  
Both are the same but difference is in the mean and variance

Normal distribution \= zero mean

When you subtract mean from each point in a graph, we can make it zero-centered

There are reversible and irreversible transformations

# Sampling

It is for feasibility  
Inference will be more or less close to the inference from the whole dataset

## Population

Represents the entire dataset

## Sample

A subset of the entire dataset

“Sample size” \- number of elements in a sample

# Central Limit Theorem (CLT)

Example of income of indians

Population \- 150 cr

Sample 1 \= x1, x2, …., x30 \= Mu S1  
Sample 2 \= x1, x2, …., x30 \= Mu S2  
Sample 3 \= x1, x2, …., x30 \= Mu S3  
….  
Sample 1000 \= x1, x2, …., x30 \= Mu S1000

The curve of the means of all the sample (sampling distribution) will produce a normal distribution regardless of how the distribution of the population looks like. And the mean of the sampling distribution will be like (tending towards) the mean of the population.

# Z-Test

## How to say if a data point is significant or not with CLT

How do we determine the cut-off of a probability to classify an event as rare-event?  
By using “significance” or “alpha value”  
Can use 0.05( for engineering related stuff) or 0.01 (for life relate stuff like surgeries, medicines, etc.)

> Population mean and SD MUST be available to perform this test


![](https://www.dummies.com/wp-content/uploads/451654.image0.jpg)

# Paired-Test

Probability of find the evidence of data

Null hypothesis vs Alternate hypothesis

P-Value \- if p-value is less than alpha, there is significance. But if it is higher, then it wont happen as per random chance and so it won't have an effect.

Court system \- the person who is suspected of a crime is called the accused and not a criminal. When the verdict comes, it is either “since the prosecution had failed to prove the guilt of the accused, he is declared not guilty”. The accused may or may not have committed the crime, but because evidence couldn’t be obatined and the crime proven, the accused is declared not guilty.

> only if population mean is available

We first calculate the z-value and then find the p-value from the z-table

P-Value can be obtained from T-Score
“Degree of Freedom”

![](https://microbenotes.com/wp-content/uploads/2021/01/p-value-from-the-t-score-e1610102691606.jpg)

# Resources:
- [Inferential statistics](https://datatab.net/tutorial/hypothesis)
- [Distribution Visualiser](https://onlinestatbook.com/stat_sim/sampling_dist/)
