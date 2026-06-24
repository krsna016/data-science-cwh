import pytest
import pandas as pd
import numpy as np

def test_dataframe_initialization():
    # Foundational test to ensure pandas is correctly mapped and instantiated
    df = pd.DataFrame({'Data': [10, 20, 30, 40, 50]})
    assert not df.empty
    assert len(df) == 5

def test_numpy_statistical_aggregations():
    # Asserting that core mathematical operations via Numpy function deterministically
    arr = np.array([1, 2, 3, 4, 5])
    assert np.mean(arr) == 3.0
    assert np.sum(arr) == 15
    assert np.std(arr) > 0
