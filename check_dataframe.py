# coding: utf-8
'''This module is a function module for dataframe checking. It contains two
  dataframe checkers. The first one is imported from HW2 which obeys HW2
  requirement and the second one (check_data_frame_new) obeys HW3 requirement.'''
# Old dataframe checker obeys HW2 requirements.
def check_dataframe(input_dataframe, list_of_columns):#Old checker
    '''This function takes two arguments: input_dataframe, a pandas dataframe
    which is being tested; list_of_columns, columns name in string and passed
    into the function as a list. Returns True if input_dataframe is OK otherwise
    raise error.'''
    if len(input_dataframe.index) < 10:
        raise ValueError("inputDf has less than 10 rows.")
    if len(input_dataframe.columns) != len(list_of_columns):
        raise ValueError("inputDf and lostOfColumns not same length.")
    for col in list_of_columns:
        if col not in input_dataframe.columns:
            raise NameError("inputDf and lostOfColumns have diff column.")
    for col in list_of_columns:
        data_column = input_dataframe[col]
        for i in range(len(data_column)-1):
            if type(data_column[i]) != type(data_column[i+1]):
                raise TypeError("inputDf has column with diff data type.")
    return True

# Function below is a new dataframe checker obeys HW3 requirement.
def check_dataframe_new(input_dataframe, list_of_columns):#New checker
    '''This function takes two arguments: input_dataframe, a pandas dataframe
    which is being tested; list_of_columns, columns name in string and passed
    into the function as a list. Returns True if input_dataframe is OK otherwise
    raise error. The rules are updates by HW3.'''
    if len(input_dataframe.index) < 1:
        raise ValueError("inputDf has less than 1 rows.")
    if input_dataframe.isnull().sum().sum() > 0:
        raise ValueError("inputDf has NaN.")
    for col in list_of_columns:
        data_column = input_dataframe[col]
        for i in range(len(data_column)-1):
            if type(data_column[i]) != type(data_column[i+1]):
                raise TypeError("inputDf has column with diff data type.")
    return True
