### **--> SVM - The Kernel Trick**

* **Issue:** Datasets that are not linearly separable cannot be classified directly be a linear SVM.
* **Solution:** The kernel trick maps the original features to a higher-dimensional space
* **Mechanism:** In this new space the data becomes linearly separable by a hyperplane.
* **Efficiency:** A kernel function K(xi, xj) computes the inner product efficiency, avoiding explicit, complex coordinate transformation



### **--> k-Nearest Neighbors (k-NN)**

* k-NN is a supervised learning algorithm for classification \& regression
* Predicts output for a new data point based on the k closest points in the training set
* Advantages:

  * Simple \& easy to implement
  * Non-parametric approach
  * works with both numerical \& categorical data
* **How k-NN works:**

  * Step1: decide k
  * Step2: Measure distance
  * Step3: Identify low distance k points
  * Step4: Predict output
* **k-NN - Distance Metrics:**

  * Euclidean Distance
  * Manhattan Distance
  * Minkowski Distance
* **Steps for implementing k-NN:**

  * Load dataset-> split -> normalize -> predict -> evaluate





### **--> Naive Bayes**

* Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem.
* It predicts the probability that a given instance belongs to a specific class.
* Called 'Naive' because it assumes all features are independent given the class label
* commonly used in text classification, spam detection \& sentiment analysis
* Naive Bayes based in Bayes' theorem
* **Formula: P(A|B)=\[P(B|A)\*P(A)/P(B)]**

  * A = class label e.g: spam or not spam
  * B = observed features (e.g: words in an email)
  * P(A) = Prior Probability
  * P(B|A) = Likelihood
  * P(B) = Evidence
* **Feature Independence Assumption:**

  * Naive Bayes assumes each feature contributes independently to the classification
  * Example: In a spam detection, 'win' \& 'prize' are treated as unrelated words





### **--> k-Means Clustering(Unsupervised Learning)**

* K-means is an unsupervised learning algorithm used to group data points into k clusters
* each cluster has a centroid representing the mean of its data points
* **Goal:** Group similar data points into a single cluster \& position them around a centroid
* **How works:**

  * Initialize k cluster centroid randomly
  * Assign each data point to the nearest centroid(using Euclidean distance)
  * Recalculate centroids as the mean of all points in each cluster
  * Repeat assignment \& update steps until clusters stabilize
* **Choosing the Optimal Number of Clusters (k):**

  * The Elbow Method
  * Silhouette Score
  * 





















