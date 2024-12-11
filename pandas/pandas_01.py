import pandas as pd
import matplotlib.pyplot as mlt
from matplotlib import style

style.use('ggplot')

web_stats = {
    'Day': [1,2,3,4,5,6],
    'Visitors':[45, 56, 67, 84, 45, 47],
    'Bounce_Rate':[23, 54, 34,56, 34, 59],
}

# DataFrame converts semi-structured data tp structured
df = pd.DataFrame(web_stats)
print(df)
