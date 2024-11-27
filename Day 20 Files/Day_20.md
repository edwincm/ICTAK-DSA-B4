# Feature Engineering and Visualization, Data Types (continuous and discrete), Techniques for Feature Extraction and Transformation, Matplotlib, Seaborn

# Data type:

* Continuous  
* Discrete  
* Classification & regression

# Visualisation

* Matplotlib  
  * Figures  
  * Axis labels  
  * Sub-figures  
  * ticks  
* Types of plots:  
  * Line plot  
  * Bar charts  
  * Pie charts  
  * Histogram  
  * CDF plot  
  * KDE plot  
  * Scatter plot  
    * With color  
  * Heatmaps  
  * boxplots  
* Seaborn

# Feature Extraction and Transformation

# Features and Labels

# Featurization:

* Text data  
* BoW  
* TF-IDF

# Feature Engineering:

* Feature orthogonality:  
  * Cosine similarity  
* Feature Colinearity  
* Feature slicing  
* Indicator variable  
* Feature binning  
* Mathematical transforms:  
  * Logarithms  
  * FFT & STFT

---

The plot() function is used to draw points (markers) in a diagram.

* The function takes parameters for specifying points in the diagram.  
* Parameter 1 is an array containing the points on the x-axis.  
* Parameter 2 is an array containing the points on the y-axis.  
* If we need to plot a line from (1, 3\) to (8, 10), we have to pass two arrays \[1, 8\] and \[3, 10\] to the plot function.

Marker \- You can use the keyword argument marker to emphasize each point with a specified marker

Scatter plot

- Requires 2 numerical variables  
- Helps figure out Correlation between the 2 variables

Box plot

- Useful for outlier removal

Feature: 

* variables; input that helps our ML model; these should have some \+ve or \-ve correlation with the other data available

Feature 1  
Feature 2  
Feature 3

Target variable

How to find the best feature that helps train the model with higher accuracy?  
1\. Based on the Correlation of these features with the target variable  
2\. Based on the correlation between the features i.e the orthogonality between the features (either through pearson correlation coefficient or through cosine similarity)

Colinearity

- Different outcomes are better  
- We want features that are NOT collinear  
- Can be considered the opposite of orthorgonality

**Ideally, a usable Feature should be Collinear with the target and orthogonal with other features**

Feature Slicing:

* Imbalance division in the dataset  
* With at least 10K data points in each division  
* Used to divide the dataset into 2 sections. These sections are used for training and we obtain 2 models   
* We can use the combined model to check whether the individual models perform better or not.

Indicator Variable and Feature binning:

**Log helps reduce tailed distribution into more symmetric distributions (it is possible to reverse it also)**

- **Can use box-cos transformation to fix the issue even more (scipy)**

For words/textual data:  
Bag of Words  
Term Frequency-Inverse Document Frequency (TF-IDF)  
