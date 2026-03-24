from __future__ import annotations

import pandas as pd


def dfskimmer(df):
    """
    Provides a cursory glance at the dataframe descriptive statistics.
    Most output columns speak for themselves.

    unique: The number of unique values
    top:    The mode of the variable (most common value)
    freq:   Frequency of the mode

    returns a Pandas DataFrame.
    """
    rows = []
    for col in df.columns:
        s = df[col]
        mode = s.mode()

        base = {
            "column": col,
            "dtype": s.dtype,
            "missing": s.isna().sum(),
            "complete": s.count(),
            "unique": s.nunique(),
            "top": mode.iloc[0] if not mode.empty else None,
            "freq": s.value_counts().iloc[0] if not s.empty else None,
        }
        
        if pd.api.types.is_numeric_dtype(s):
            base.update({
                "mean": s.mean(),
                "std": s.std(),
                "min": s.min(),
                "p25": s.quantile(0.25),
                "median": s.median(),
                "p75": s.quantile(0.75),
                "p99": s.quantile(0.99),
                "max": s.max(),
            })
        
        rows.append(base)
    
    return pd.DataFrame(rows)


__all__ = ["dfskimmer"]