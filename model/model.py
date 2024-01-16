from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


# 三次多项式回归模型
def polynomial_regression_model(X_train, X_test, y_train, y_test):
    poly_reg = PolynomialFeatures(degree=3)
    poly_X_train = poly_reg.fit_transform(X_train)
    poly_X_test = poly_reg.transform(X_test)

    model = LinearRegression()
    model.fit(poly_X_train, y_train)

    y_test_pred = model.predict(poly_X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''    
    with open('../evaluation/polynomial_regression_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 岭回归模型
def ridge_regression_model(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    alpha = 1.0
    model = Ridge(alpha=alpha)
    model.fit(X_train_scaled, y_train)

    y_test_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/ridge_regression_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 支持向量回归模型（线性核函数）
def svr_linear_model(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVR(kernel='linear')
    model.fit(X_train_scaled, y_train)

    y_test_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/svr_linear_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 支持向量回归模型（多项式核函数）
def svr_poly_model(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVR(kernel='poly', degree=2)
    model.fit(X_train_scaled, y_train)

    y_test_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/svr_poly_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 支持向量回归模型（RBF核函数）
def svr_rbf_model(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVR(kernel='rbf')
    model.fit(X_train_scaled, y_train)

    y_test_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/svr_rbf_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 决策树回归模型
def decision_tree_regression_model(X_train, X_test, y_train, y_test):
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/decision_tree_regression_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model


# 随机森林回归模型
def random_forest_regression_model(X_train, X_test, y_train, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    '''
    with open('../evaluation/random_forest_regression_evaluation.txt', 'w') as f:
        f.write("Test:\n")
        f.write("Mean Squared Error: " + str(mse) + '\n')
        f.write("Coefficient of Determination: " + str(r2))
    '''

    return model
