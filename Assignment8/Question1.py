import pandas as pd

dates = ['2026-01-01', '2026-01-02', '2026-01-03']
values = [10, 20, 15]

df = pd.DataFrame({
    'date': dates,
    'value': values
})

df['date'] = pd.to_datetime(df['date'])

ts = df.set_index('date')

print(ts)