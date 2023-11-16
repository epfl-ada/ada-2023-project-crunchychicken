import pandas as pd

def batched(it, sz: int):
    """Generator for retrieving batches from an iterator."""

    start = 0
    while start + sz < len(it):
        yield it[start:start+sz]
        start += sz
    yield it[start:]

def convert_and_downcast(df: pd.DataFrame) -> pd.DataFrame:
    """Convert object columns to string and downcast numeric columns to save memory."""
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype('string')
        elif df[col].dtype == float:
            df[col] = pd.to_numeric(df[col], downcast='float')
        else:
            df[col] = pd.to_numeric(df[col], downcast='integer')
    return df
