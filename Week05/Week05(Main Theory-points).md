### **--> Introduction to Flask**

* Flask is lightweight python web framework
* Ideal framework for building web apps, APIs, \& ML/DL model deployment
* key features:

  * Minimalist core: flexible \& extensible
  * Built-in development server \& developer
  * supports templating (Jinja2) \& routing 
* Why use flask for ML/DL/AL:

  * Deploy trained models as web APIs
  * serve predictions via HTTP requests(Rest API)
  * Simple integration with python ML lib: scikit-learn, PyTorch, TensorFlow
* Others frameworks:

  * Django(Full web apps, ORM, auth)
  * FastAPI(Fast APIs async ML inference)
* Example:

  * Problem: You trained an ML model->how does a user use it?
  * flask solution: input(user)->Flask API->ML model->Output(prediction)



### **--> Machine Learning**

* In traditional programming , we try to program every possible scenario
* unprogrammed scenarios result in errors
* Purpose of Machine is to enable machines to learn like humans
* Machines learn patterns from data instead of being explicitly programmed
* Examples: spam detection, movie recommendations, search suggestion
* Traditional= Rules + data->Output
* ML= Data + Output -> Algorithm learn rules



### **--> Linear Regression**

* Predicts output (y) from input (x) using line: y=mx+b
* Example: predicting house price from square footage
* Linear regression is an example of explainable AI
* linear relationship: change in input -> proportional change in output

  * Example: study hours increases -> grades increases
* for multiple variables: y=b+m1x1+m2x2+...+mnxn
* Common cost function: linear regression uses MSE(average of squared differences between predicted \& actual)



### **--> Linear Regression - Gradient Descent Optimization**

* algorithm used to minimize errors
* A gradient is a function that increases or decreases its value gradually
* Descent means to move downward
* Gradient descent: gradually moving downward at varying speeds to minimize a function.
* An optimization method used to minimize cost function
* it works like a rolling a ball, that moves from high speed to low speed, as like in errors from high errors to low errors
* **How it works?**

  * start with a random values for a and b
  * update step by step: m=m-learning\_rate\*gradient
  * repeat until the cost function is minimized
* Key ingredient learning rate:

  * too small-> slow learning
  * too long => overshooting, may not coverage
  * maintain an optimal learning rate
  * use adaptive learning rate if needed 



### **--> Linear Regression - Optimization Techniques**

* how improve gradient descent?

  * adjust learning rate
* use convergence criteria, stop when:

  * define target accuracy
  * error barely changes
  * fixed number of iterations
* Other tricks:

  * feature scaling for faster convergence
  * try different initial values
* **Workflow for Python implementation:**

  * Load dataset
  * define Hypothesis (y= mx + c) 
  * define cost function
  * Apply gradient Descent

