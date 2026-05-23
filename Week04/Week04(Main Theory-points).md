### **--> Outlier Detection Using Statistical Rules**

* Outliers are data points that falls outside the normal range, representing extreme values that can distort the means and median of the dataset
* Methods of outlier identification \& removal:

  * IQR method
  * Z-score method
  * Domain-driven Threshold





### **--> Correlation \& Covariance Analysis**

* Measure the relationships between numerical variables



### **--> Creating an Exploratory Data Analysis Report**

* EDA report is a short narrative summary of data insights
* It Combines tables, figures, \& bullet summaries
* Guides preprocessing \& modeling decisions
* Ensures data quality before ML
* Key Takeaways:

  * Eda report should be concise + structured
  * Use visuals \& bullet points for clarity
  * Document issues, insights, \& next steps
  * Acts as a bridge between data \& modeling





### **--> Matplotlib Figure Anatomy \& Visualization Workflow**

* Matplotlib provides a figure that acts like a canvas on which various graphs \& plots can be created



### **--> Introduction to Seaborn Visualization Library**

* part of python's data visualization ecosystem
* Widely used in AI \& Data Science Pipelines
* Seaborn is the advanced version of Matplotlib
* Why Seaborn:

  * Cleaner visuals with minimal code
  * built in themes \& color palettes
  * high level statistical plots
  * ideal for exploratory data analysis(EDA) in AI/ML pipeline
* Key Features:

  * Hight level plotting functions (e.g sns.dstplot, scatter plots)
  * Automatic handling of Pandas data frames
  * built in themes: dark grid, white grid, dark, white, ticks
  * seamless integration with NumPy, Pandas, Matplotlib
* Offers visuals for:

  * Distribution plots(Histogram, KDE)
  * Categorical plots(Bar, Box, violin)
  * Regression/Relationship scatter plots with trend line
  * Matrix plots(Heatmaps pair grid maps)
  * Provide quick visual mapping for understanding
* Plots levels in seaborn:

  * Figure-level plots
  * Axis-level plots
  * Themes



### **--> Feature Scaling \& Normalization**

* Scaling ensures features are on a similar range to improve distance-based model performance
* Methods of scaling:

  * Z-score method standardization
  * Min-Max scaling(normalization)
* **Data leakage risk**: Applying scaling on both training \& test data together leads to data leakage, as test data information is used during training
* Scale feature when using distance-based models(KNN, SVM, PCA, clustering)
* Avoid for handle carefully for tree-based models(Decision Trees, Random forest), as they are insensitive to scale

