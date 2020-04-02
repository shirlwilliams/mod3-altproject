import os
import pandas as pd
import matplotlib.pyplot as plt

# Function to rename columns as pythonic
def column_cleaner(col, bad_characters='()*&^@#$%'):
    for ch in bad_characters:
        col = col.replace(ch, " ")
        col = col.replace(" ", "_")
        col = col.lower()
        return col


def clean_data(df, write_file=False, filepath=None):
    # rename columns
    df.rename(mapper=column_cleaner, axis=1, inplace=True)
    
    if write_file:
        if not filepath:
            print("filepath is empty")
            pass
        else:
            path, filepath = os.path.split(filepath)
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
            filepath = filepath if filepath.endswith(".csv") else filepath+'.csv'
            df.to_csv(filepath, index=False)
    return df

def test_data(model_filepath, needs_clean=False, csv_filepath=False):
    # read in file
    df = pd.read_csv(csv_filepath)
    if needs_cleaning:
        # clean the dataframe
        df = clean_data(df)
        
# Plot a confusion matrix
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    #Add Normalization Option
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print('Normalized confusion matrix')
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment='center',
                 color='white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')