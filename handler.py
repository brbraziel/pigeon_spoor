def plot_from_db():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_json('bucket/output/2021_11_29.json')
    df[df['class'] == 'bird']['timestamp'].value_counts().plot()
    plt.show()

insert_database()