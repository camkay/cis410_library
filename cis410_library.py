import pandas as pd

def remove_list_item(*, the_list, the_item):

  new_list = [item for item in the_list if item != the_item] 
  return new_list

def plot_x_by_class_y(*, table, x_column, y_column, y_log = True):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'
  assert type(y_log) == bool, f'y_log must be of type bool. y_log is of type {type(y_log)}.'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=y_log)
  return None

def pasterisk(*, my_list, thresholds = [.05, .01, .001], sig_symbol = "*"):
  # check argument types
  assert type(my_list)    == list, f'my_list should be of type list. It is of type {type(my_list)}'
  assert type(thresholds) == list, f'thresholds should be of type list. It is of type {type(thresholds)}'
  assert type(sig_symbol) == str, f'sig_symbol should be of type str. It is of type {type(sig_symbol)}'

  # check values within my_list and thresholds
  assert any([x > 1 or x < 0 for x in my_list])    == False, 'all values in my_list must be between 0 and 1 (inclusive).'
  assert any([x > 1 or x < 0 for x in thresholds]) == False, 'all values in thresholds must be between 0 and 1 (inclusive).'
  
  # create a list of zeroes to count the number of asterisk required
  out = [0] * len(my_list)

  # produce a list of the asterisks required for each p-value
  for threshold in thresholds: # for each threshold...
    for i in range(len(my_list)): # ...iterate through the list...
      if my_list[i] < threshold: # ...testing whether the p_val is less than the threshold...
        out[i] += 1 # ...and incrementing the output by 1 if it is
  
  # conver that list of numbers to a list of asterisks
  out = [x * sig_symbol for x in out]

  # return out
  return out
