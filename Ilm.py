import pandas

def findTableNull(dataframe, only_missing = False):
  # Tabel Null
  result = dataframe.isnull().sum()
  if result.sum() == 0:
    # Hasil Bersih
    return None
  # Hasil in Tabel
  result = result.to_frame(name = 'Total')
  result = result.sort_values('Total', ascending = False)
  if only_missing:
    # Only Missing
    result = result[result['Total'] > 0]
  # Hasil
  return result
