import numpy as np
import pandas as pd
from scipy.stats import t


def summary(df):
    """
    Computes detailed statistics (count, mean, std dev, t-stat, p-value, min, max, percentiles) for each column in a DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame where each column represents a series of portfolio returns.

    Returns:
    pd.DataFrame: A DataFrame summarizing the statistics for each column.
    """
    results = {}
    for col in df.columns:
        returns = df[col]
        n = len(returns)

        mean_return = np.mean(returns)
        std_deviation = np.std(returns, ddof=1)
        t_stat = mean_return / (std_deviation / np.sqrt(n)) if n > 1 else np.nan

        p_val = (1 - t.cdf(abs(t_stat), df=n - 1)) * 2 if n > 1 else np.nan

        percentiles = np.percentile(returns, [25, 50, 75]) if n > 0 else [np.nan] * 3

        # Store results in a dictionary
        results[col] = {
            "count": n,
            "mean": mean_return,
            "std": std_deviation,
            "tstat": t_stat,
            "pval": p_val,
            "min": np.min(returns) if n > 0 else np.nan,
            "25%": percentiles[0],
            "50%": percentiles[1],
            "75%": percentiles[2],
            "max": np.max(returns) if n > 0 else np.nan,
        }

    # Convert results to a DataFrame
    summary_df = pd.DataFrame(results)
    return summary_df
