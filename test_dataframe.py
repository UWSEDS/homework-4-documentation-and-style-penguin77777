# coding: utf-8
'''Test Files for HW3 and modified for HW4 based on PEP8 and tested by pylint.
 This file contains 11 tests.'''
import copy as cp
import pandas as pd
import numpy as np
import check_dataframe as checker

def data_downloader(name):
    '''Download and load test data. It takes a string and returns a dataframe.'''
    data_frame = pd.read_csv(name)
    return data_frame

DFSET = data_downloader("pronto.csv")
DFORG = cp.copy(DFSET)
DFSRT = DFSET[:6]
DFTHIN = DFSET[["Date", "Fremont Bridge East Sidewalk"]]
DFSET["Total Bicycle Count"] = DFSET["Fremont Bridge East Sidewalk"]\
 + DFSET["Fremont Bridge West Sidewalk"]
HOURTEMP = DFSET["Date"]
HOURTEMP = pd.to_datetime(HOURTEMP)
DFSET['Date'] = HOURTEMP
DFSET["Fremont Bridge East Sidewalk"] =\
 DFSET["Fremont Bridge East Sidewalk"].fillna(0.0).apply(np.int64)
DFSET["Fremont Bridge West Sidewalk"] =\
 DFSET["Fremont Bridge West Sidewalk"].fillna(0.0).apply(np.int64)
DFSET["Total Bicycle Count"] =\
 DFSET["Total Bicycle Count"].fillna(0.0).apply(np.int64)
DFORG["Total Bicycle Count"] = DFORG["Fremont Bridge East Sidewalk"]\
 + DFORG["Fremont Bridge West Sidewalk"]
HOURTEMP = DFORG["Date"]
HOURTEMP = pd.to_datetime(HOURTEMP)
DFORG['Date'] = HOURTEMP
LC1 = [
    "Fremont Bridge East Sidewak",
    "Fremont Bridge West Sidewalk",
    "Total Bicycle Count", "Date"]

def test_check_dataframe1():
    '''Test Case 1. It should return NameError since the column name
    is miss spoken.'''
    try:
        checker.check_dataframe(DFSET, LC1)
    except NameError:
        pass

LC2 = [
    "Fremont Bridge East Sidewalk",
    "Fremont Bridge West Sidewalk",
    "Total Bicycle Count", "Date"
    ]
def test_check_dataframe2():
    '''Test Case 2. It should return True.'''
    assert checker.check_dataframe(DFSET, LC2)

LC3 = [
    "Fremont Bridge East Sidewalk",
    "Fremont Bridge West Sidewalk",
    "Total Bicycle Count",
    "Year",
    "month",
    "day",
    "Hour"
    ]
def test_check_dataframe3():
    '''Test Case 3. It should return ValueError since the column name
    is miss spoken.'''
    try:
        checker.check_dataframe(DFORG, LC3)
    except ValueError:
        pass

LC4 = [
    "Fremont Bridge East Sidewalk",
    "Fremont Bridge West Sidewalk",
    "Total Bicycle Count",
    "Date"
    ]
def test_check_dataframe4():
    '''Test Case 4. It should return ValueError since the number of
    row is less than 10.'''
    try:
        checker.check_dataframe(DFSRT, LC4)
    except ValueError:
        pass

LC5 = ["Date"]
def test_check_dataframe5():
    '''Test Case 5. It should return ValueError since the column name
    is wrong.'''
    try:
        checker.check_dataframe(DFTHIN, LC5)
    except ValueError:
        pass

DT1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6.6, 7, 8, 9, 10, 11],
    'B': ['a', 'b', 'c', 'd', 'e', 'h', 'j', 'd', 'z', 'r', 'x'],
    'C': [1, 734570934423524523455, 2, 2, 5, 9, 2.2, 14, 58, 10, 11]
    })
LC6 = ["A", "B", "C"]
def test_check_dataframe6():
    '''Test Case 6. It should return TypeError since data type is not
    same across the column.'''
    try:
        checker.check_dataframe(DT1, LC6)
    except TypeError:
        pass

DT2 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6.6, 7, 8, 9, 10, 11],
    'B': ['a', 'b', 'c', 'd', 'e', 'h', 'j', 'd', 'z', 'r', 'x'],
    'C': [1, 7355, 2, 2, 5, 9, 2.2, 14, 58, 10, 11]
    })
LC7 = ["A", "B", "C"]
def test_check_dataframe7():
    '''Test Case 7. It should return True.'''
    assert checker.check_dataframe(DT2, LC7)

DT3 = pd.DataFrame({
    'A': [],
    'B': [],
    'C': []
    })
LC8 = ["A", "B", "C"]
def test_check_dataframe8():
    '''Test Case 8. It should return ValueError since the number of
    row is less than one.'''
    try:
        checker.check_dataframe_new(DT3, LC8)
    except ValueError:
        pass

DT4 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6.6, 7, 8, 9, 10, 11],
    'B': ['a', 'b', 'c', 'd', np.nan, 'h', 'j', 'd', 'z', 'r', 'x'],
    'C': [1, np.nan, 2, 2, 5, 9, 2.2, 14, 58, 10, 11]
    })
LC9 = ["A", "B", "C"]
def test_check_dataframe9():
    '''Test Case 9. It should return ValueError since NaN is present.'''
    try:
        checker.check_dataframe_new(DT4, LC9)
    except ValueError:
        pass

DT5 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6.6, 7, 8, 9, 10, 11],
    'B': ['a', 'b', 'c', 'd', 'e', 'h', 'j', 'd', 'z', 'r', 'x'],
    'C': [1, 735571236457823417635412374928759123451387659132570948,
          2, 2, 5, 9, 2.2, 14, 58, 10, 11]
    })
LC10 = ["A", "B", "C"]
def test_check_dataframe10():
    '''Test Case 10. It should return TypeError since data type is not
    same across one column.'''
    try:
        checker.check_dataframe_new(DT5, LC10)
    except TypeError:
        pass

DT6 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6.6, 7, 8, 9, 10, 11],
    'B': ['a', 'b', 'c', 'd', 'e', 'h', 'j', 'd', 'z', 'r', 'x'],
    'C': [1, 7355712364, 2, 2, 5, 9, 2.2, 14, 58, 10, 11]
    })
LC11 = ["A", "B", "C"]
def test_check_dataframe11():
    '''Test Case 11. It should return True.'''
    assert checker.check_dataframe_new(DT6, LC11)
