import pandas as pd

def make_histogram(df , column_as_str, round_float_to, plot_or_frame):
    """Returns a histogram plot or a DataFrame.
        Pass a pandas DataFrame, a column as string, and the 
        number of significant digits for the data. The last argument
        returns a histogram plot if plot_or_frame == 1, otherwise it returns the data"""
    # Find the min and the max
    min = df[column_as_str].describe()['min']
    max = df[column_as_str].describe()['max']
    # Rough estimate for number of bins
    num_bins = int(round((max-min)/4,0))
    # create variables
    bins = []
    group_names = []
    top = 0
    # create bins and labels
    for x in range(1, num_bins+1):
        group_names.append(f'{top} - ')
        top = round(x * round(max/num_bins,2),round_float_to)
        group_names[-1]+=(f'{top}')
        bins.append(top)
    group_names.pop()
    df['binned'] = pd.cut(df[column_as_str],bins,labels=group_names)
    df['bins']= pd.cut(df[column_as_str],bins,labels=group_names)
    binned_df= pd.DataFrame(df.groupby('bins')[column_as_str].count())
    binned_df.reset_index(inplace=True)
    
    if plot_or_frame == 1:
        return binned_df.plot(kind='bar', x = 'bins', y = column_as_str)
    else:
        return binned_df