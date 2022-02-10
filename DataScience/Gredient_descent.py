    
import numpy as np
import matplotlib.pyplot as plt
  
def mean_squared_error(y_true, y_predicted):
    cost = np.sum((y_true-y_predicted)**2) / len(y_true)
    return cost
  
# Gradient Descent Function
# Here iterations, learning_rate, stopping_threshold
# are hyperparameters that can be tuned

#  For linear regression
def gradient_descent_self(x, y, iterations = 1000, learning_rate = 0.0001):
    current_slope = 0
    current_intercept = 0
    
    intercept = []
    
    slope =[]
    
    for i in range(iterations):
        
        y_predicted = (current_slope * x) + current_intercept
        
        current_cost_for_slope = (1/len(y)) * np.sum((y_predicted - y) * x)
        
        current_cost_for_intercept = (1/len(y)) * np.sum((y_predicted - y))
        
        current_slope = current_slope - (learning_rate * current_cost_for_slope)
        
        current_intercept = current_intercept - (learning_rate * current_cost_for_intercept)

        slope.append(current_cost_for_slope)
        intercept.append(current_cost_for_intercept)
        
    print(f"Slope: {current_slope}\nIntercept: {current_intercept}")
    
    return current_slope, current_intercept

    
    
def gradient_descent_for_logistic_regression(X ,y ):
    
    return
    
    
    
    
    
    

      

from sklearn.linear_model import LinearRegression

model = LinearRegression()
  
def main():
      
    # Data
    X = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,
           55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,
           45.41973014, 54.35163488, 44.1640495 , 58.16847072, 56.72720806,
           48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754])
    Y = np.array([31.70700585, 68.77759598, 62.5623823 , 71.54663223, 87.23092513,
           78.21151827, 79.64197305, 59.17148932, 75.3312423 , 71.30087989,
           55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
           60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319])
  
    # Estimating weight and bias using gradient descent
    
    estimated_weight1, eatimated_bias1 = gradient_descent_self(X, Y, iterations=10000)
  
    # Making predictions using estimated parameters
  
    Y_pred1 = estimated_weight1*X + eatimated_bias1
  
    # Plotting the regression line

    # plt.figure(figsize = (8,6))
    # # plt.title("Using Self")
    # plt.scatter(X, Y, marker='o', color='red')
    # plt.plot([min(X), max(X)], [min(Y_pred1), max(Y_pred1)], color='blue',markerfacecolor='red',
    #          markersize=10,linestyle='dashed')
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.show()
    
    model.fit(X.reshape(-1 , 1) , Y)
    
    print(f"Estimated Weight: {model.coef_}\nEstimated Bias: {model.intercept_}")
    print("model score ",model.score(X.reshape(-1 , 1) , Y))
  
  
main()















# def gradient_descent(x, y, iterations = 1000, learning_rate = 0.0001, 
#                      stopping_threshold = 1e-6):
      
#     # Initializing weight, bias, learning rate and iterations
#     current_weight = 0.1
#     current_bias = 0.01
#     # iterations = 1
#     n = float(len(x))
      
#     costs = []
#     weights = []
#     previous_cost = None
      
#     # Estimation of optimal parameters 
#     for i in range(iterations):
          
#         # Making predictions
#         y_predicted = (current_weight * x) + current_bias
          
#         # Calculationg the current cost
#         current_cost = mean_squared_error(y, y_predicted)
  
#         # If the change in cost is less than or equal to 
#         # stopping_threshold we stop the gradient descent

#         # if previous_cost and abs(previous_cost-current_cost)<=stopping_threshold:
#         #     break
          
#         previous_cost = current_cost
  
#         costs.append(current_cost)
#         weights.append(current_weight)
          
#         # Calculating the gradients
#         weight_derivative = -(2/n) * sum(x * (y-y_predicted))
#         bias_derivative = -(2/n) * sum(y-y_predicted)
          
#         # Updating weights and bias
#         current_weight = current_weight - (learning_rate * weight_derivative)
#         current_bias = current_bias - (learning_rate * bias_derivative)
                  
#         # Printing the parameters for each 1000th iteration
#         # print(f"Iteration {i+1}: Cost {current_cost}, Weight \
#         # {current_weight}, Bias {current_bias}")
      
      
#     # Visualizing the weights and cost at for all iterations
#     # plt.figure(figsize = (8,6))
#     # plt.plot(weights, costs)
#     # plt.scatter(weights, costs, marker='o', color='red')
#     # plt.title("Cost vs Weights")
#     # plt.ylabel("Cost")
#     # plt.xlabel("Weight")
#     # plt.show()
#     return current_weight, current_bias