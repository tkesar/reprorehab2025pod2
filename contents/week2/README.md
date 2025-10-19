# Week 2. Tabular Data Manipulation in Python I

This week, we start working with tabular data - one of the most common formats you'll encounter in rehabilitation and behavioral research.

Our main tool will be **pandas**, a powerful Python library that makes data loading, filtering, and summarizing easier than ever.

You will learn how to:
- load `.csv` and `.tsv` files into pandas DataFrames,
- explore dataset structure and metadata
- rename columns, slice and filter values,
- and perform basic descriptive statistics and visualization.

### Goal of Week 2:
Get comfortable with pandas' DataFrame - how to load, inspect, reshape, and summarize data.

Once you can do this fluently, every dataset you meet (physio, motion, fNIRS, speech, etc.) will start to feel like a familiar structure waiting to be explored.

## 🧩 Slides - Tabular Data Manipulation in Python I

Reference slides summarize:
- key pandas functions (`read_csv`, `rename`, `iloc`, `loc`, `describe`),
- common parameters (`sep`, `header`, `usecols`, `engine`),
- and quick visualization commands.

Use them as a lookup while you code!

## 📘 Main Assignment - `Week2_assignment.py`

You will use a **public wearable-sensor dataset** (PhysioNet) to practice hands-on data handling.

### Tasks include:
1. Loading a CSV file using `pd.read_csv()` and inspecting structure with `.head()` and `.info()`.
2. Renaming columns (`rename`) and selecting subsets(`iloc`, `loc`).
3. Filtering rows that meet a condition.
4. Computing summary statistics (`describe`, `mean`, `std`, `min`, `max`).
5. Reading a more complex TSV file (motion-capture dataset) and visualizing a few variables using `plot.line`, `plot.scatter`, and `plot.hist`.

This exercise helps you build an intuition for how datasets are organized and how to **interrogate data directly from code, without switching to Excel.

## 🧭 Extra - `Week2_extra.py`

Timestamps are evertwhere - from wearable devices to behavioral recordings.

This notebook introduces pandas' `Timestamp` and `DatetimeIndex` objects and walks through how to:

- convert strings and numbers to datetime (`to_datetime`),
- handle Unix time and time zones,
- extract attributes like year, month, day, hour, etc.,
- and compute time differences between two measurement points.

- [Slides (google)](https://docs.google.com/presentation/d/1tm2DKr1KZNaURV3C7QE2lnvFvVvNnKGAq3m_InlaVn0/edit?usp=sharing)

- [Assignment](https://colab.research.google.com/drive/1m-d2-PZ_9SbxWG44KY-I1wez1xIKsB93?usp=sharing)

- [Extra assignment](https://colab.research.google.com/drive/1bSRzKw9X5kntkJYVPzBc5bYgpCdVtO9P?usp=sharing)
