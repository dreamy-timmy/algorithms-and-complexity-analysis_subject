import time

def get_execution_time(n_values: list[int], method: callable) -> list:
    '''
    Returns the execution time of a method for different n values.
    Parameters:
        n_values(list[int]): list of n values to be used in the method
        method(callable): method to be executed

    Returns:
        list: list of execution time values for each n value
    '''
    time_values = []
    print('----------------------')
    print('Method: ', method.__name__)
    for n in n_values:
        st = time.time()
        res = method(n)
        end = time.time()
        print('n: ', n)
        time_values.append(end-st)
    return time_values

import matplotlib.pyplot as plt

def plot_time_analysis_results(n_values: list, Methods_Values: list[list], Methods_Names: list[str]):
    '''
    Plots the time analysis results for the given methods.
    Parameters:
        n_values(list[int]): list of n values to be used in the methods
        Methods_Values(list[list]): list of lists of time values for each method
        Methods_Names(list[str]): list of names of the methods
    '''
    plt.figure(figsize=(10, 5))
    for i, method_time_values in enumerate(Methods_Values):
        plt.plot(n_values, method_time_values, label=Methods_Names[i])
    plt.xlabel('n values')
    plt.ylabel('time')
    
    plt.legend()

    plt.show()
    