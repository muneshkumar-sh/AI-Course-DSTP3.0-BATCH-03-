### **--> Decision Trees**

* A Supervised machine learning algorithm
* based on statistical analysis
* Simulates human-like decision making
* works for both classification \& regression
* Extracts simple decision rules from structured data
* predicts target values based on input features
* for classification, identifies the correct class
* for regression , predicts continuous(true) values
* The model is represented as a tree-like structure
* internal nodes represents tests, \& branches represent outcomes
* leaves represent final predictions
* Decision tree represents human power for decision-making
* **How it works?**

  * The algorithm begins at the root node \& selects the feature based on a splitting criterion
  * The dataset is partitioned into smaller subsets based on feature values
  * This process is repeated recursively, creating branches until a stopping condition is met
  * The final tree consists of decision rules that map input features t outputs
* **Advantage**

  * An example of explainable AI
* **Real world example:**

  * Predicting whether a customer will buy insurance
  * Nodes might split data based on "Age", "Income", \& "Marital status".
  * "Age>30" ->"Income>60k" "Buys insurance=yes"





### **--> Decision Trees - Data Splitting \& Feature Selection**

* Important components of Decision tree:

  * Root Node
  * Decision Tree
  * Leaf Node(Terminal Node)
  * Branch: A possible outcome of a decision rule leading to the next node
* **Splitting Criteria:**

  * Information gain: measures reduction in entropy after a split higher gain means a better split
  * Gini Index: measures impurity of a dataset. Lower Gini value indicates purer subsets.
  * Entropy: Quantifies uncertainty in the dataset entropy=0 means perfectly pure nodes
  * the algorithm chooses the feature that maximizes purity improvement at each step
* **Overfitting:**  Overfitting occurs when a decision tree becomes too complex \& learns noise instead of patterns
* methods of avoiding overfitting:

  * Pre-pruning(early stopping)

    * define tree depth
    * minimum samples per node
    * minimum information gain
  * Post-pruning(reduced error pruning)

    * build the full tree fist
    * remove weak branches that do not improve performance
* **Confusion Matrix:** No. of classes X No. of classes dimensions matrix

  * it tells when our is trained then on testing data how much confuse on one class to another class



### **--> Random Forest**

* is an ensemble learning method that combines multiple decision trees to improve predictive performance
* Instead of relying on a single tree Random Forest builds many trees \& aggregates their predictions to reduce overfitting
* Applications:

  * Spam detection, Medical diagnosis(classification), House price prediction, Stock forecasting(regression)
* Advantages:

  * Reduces overfitting
  * Improve accuracy
  * Robustness: resistant to overfitting due to averaging across trees
  * Handles large/high-dimensional datasets
  * works for both classification \& regression tasks, bar charts can visualize feature importance
* How works:

  * Bootstrap sampling(each tree has subset of data \& pick samples randomly with replacement)
  * Random feature selection
  * Multiple trees are grown independently, \& predictions are aggregated(combined)

    * for classification, based on voting, final output will be on majority voting
    * for regression , calculate average 
* Real life analogy:

  * Asking multiple experts rather than relying on the one expert



### **--> Random Forest - How It Works- Techniques used: Bootstrapping \& Bagging**



* **Bootstrapping:** 

  * Randomly sample n data points with replacement(not remove sample, it exist in dataset) for each tree
  * Some samples appear multiple times, while others are not selected (out-of-bag samples)
  * Advantage:

    * Different subsamples of the dataset are used for each decision tree
    * Each decision tree learns in a different way
    * improving decision-making
    * Better classifier then a single decision tree
    * Widely used for improved results
  * Out-of-bag(OOB) samples: Used as an internal testing dataset and a good candidate for model evaluation. Provides an efficient performance estimate, especially for small datasets
* **Bagging:**

  * Combines prediction from multiple trees to reduce variance
  * for classification, based on voting, final output will be on majority voting
  * for regression, average of predictions is taken





### **--> Random Forest - Feature Importance \& Out-of-Bag Error**

* **Feature importance:**

  * measures each feature's contribution to predictive performance
  * helps identify most influential features \& guides selection
  * Computed across all trees not just one
  * Application: interpretation, simplification, \& model optimization
  * Calculation of feature importance:

    * Step01: measure reduction in impurity(Gini/Entropy) at each split
    * Step02: sum reduction across all trees \& normalize (0-1)
    * Step03: rank features; higher value -> more important
  * Formula = decrease in impurity at node n; sum over nodes where feature f used
  * Example: House price prediction: features \[Size, Bedrooms, Age, Location]

    * Feature importance: size=0.55, location=0.25, bedrooms=0.15, age=0.05
    * here most importance is size, and we have normalize these important features between 0 and 1
    * Model relies mostly on size, moderately on location, least on age
* **Out-of-Bag Error:** 

  * OOB error is an internal validation metric using bootstrapped samples (\~1/3 left out)
  * Efficient, especially for small datasets
  * examples: 1000 samples, each tree trains on 667, then 333 OOB used for testing
  * Calculating OOB error step by step:

    * Identify OOB samples for each tree
    * Predict output using that tree
    * Aggregate predictions across all trees, compare with actual
  * Example: 

    * 1000 samples, 300/333
    * correct OOB -> OOB
    * accuracy \~ 90%



### **--> Random Forest - Hyperparameter Tuning \& Optimization**

* **Parameter Tuning:** 

  * Goal: improve predictive performance \& generalization
  * Random forest Hyperparameters control tree growth \& ensemble behavior
  * proper tuning balances bias \& variance to prevent over/underfitting
  * Parameters: n\_estimators, max\_depth, min\_samples\_split, min\_samples\_leaf, max\_features



### **--> Support Vector Machines (SVM)**

* SVMs are supervised learning algorithms used for classification \& sometimes regression
* SVM find he optimal hyperplane that separates classes by maximizing the margin between them
* SVM are the data points closest to the hyperplane; they define its position \& influence classification
* Margin: distance between the hyperplane \& the nearest data points of any class
* SVM maximize this margin to improve generalization on unseen data
* Large margin -> lower generalization error; small margin -> sensitivity to noise/outliers
* SVM vectors lie on the margin \& are critical for defining it
* **Hyperplane equation:** w.x+b=0, x is a feature vector, w is the weight vector , b is the bias
* **Goal:** To maximize the margin between classes, the SVM minimizes the objective function(1/2||w||^2).











































