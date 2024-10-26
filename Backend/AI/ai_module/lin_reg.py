import numpy as np

class LinearRegressor:
    def __init__(self, solver="analytic"):
        self.X = None
        self.y = None
        self.w = None
        self.solver = solver

    def fit(self, X, y):
        self.X = X
        self.y = y
        if self.solver == "sgd":
            pass
        else:
            self.w = self.analytic_solver(self.X, self.y)
        return self
    
    def predict(self, x):
        return x @ self.w
    
    @staticmethod
    def analytic_solver(X, y):
        X_T = X.T
        return np.linalg.inv(X_T @ X) @ X_T @ y
    

if __name__ == "__main__":
    X = np.array([
        [0, 0, 1],
        [2, 0, 0],
        [4, 4, 4],
        [1, 1, 0]
    ])
    y = np.array([0, 1.5, 5, 1])
    res = LinearRegressor().fit(X, y).predict(np.array([1,1,1]))
    print(res)