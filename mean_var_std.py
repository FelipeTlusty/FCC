import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list)
    re_matrix = matrix.reshape(3,3)
    calculations = {}
    
    # Mean
    calculations['mean'] = [np.mean(re_matrix, axis = 0).tolist(), np.mean(re_matrix, axis = 1).tolist(), np.mean(matrix)]

    # Variance
    calculations['variance'] = [np.var(re_matrix, axis = 0).tolist(), np.var(re_matrix, axis = 1).tolist(), np.var(matrix)]

    # Std Deviation
    calculations['standard deviation'] = [np.std(re_matrix, axis = 0).tolist(), np.std(re_matrix, axis = 1).tolist(), np.std(matrix)]

    # Max
    calculations['max'] = [np.max(re_matrix, axis = 0).tolist(), np.max(re_matrix, axis = 1).tolist(), np.max(matrix)]

    # Min
    calculations['min'] = [np.min(re_matrix, axis = 0).tolist(), np.min(re_matrix, axis = 1).tolist(), np.min(matrix)]

    # Sum
    calculations['sum'] = [np.sum(re_matrix, axis = 0).tolist(), np.sum(re_matrix, axis = 1).tolist(), np.sum(matrix)]

    return calculations