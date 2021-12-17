import numpy as np
import pandas as pd

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt




odsurvey_raw = pd.read_csv('C:/Users/test/Desktop/OD_Survey/OD_survey-Final_raw-data_2013.csv', encoding='utf8', dtype={"Code": int, "name": str, "latitude": float, "longitude": float})

print(odsurvey_raw.head())


# Those columns which we need are filtered in

odsurvey_abstract_allmodes=odsurvey_raw.loc[:,['ipere','d_orisr','d_dessr','d_hrede','d_mode1']]
print(odsurvey_abstract_allmodes.head())


# Filter for one mode of transportation
odsurvey_abstract_mode2 = odsurvey_abstract_allmodes.loc[odsurvey_abstract_allmodes['d_mode1']=='2']

print(odsurvey_abstract_mode2.head())


odsurvey_abstract_mode2_timeunder2400=odsurvey_abstract_mode2.loc[odsurvey_abstract_mode2['d_hrede']<=2400]

print(odsurvey_abstract_mode2_timeunder2400.head())

n=odsurvey_abstract_mode2_timeunder2400.d_orisr.nunique()
m=odsurvey_abstract_mode2_timeunder2400.d_dessr.nunique()
k=odsurvey_abstract_mode2_timeunder2400.d_hrede.nunique()

print(n,m,k)



origin_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_orisr'].value_counts()
origin_distinct_frequency = origin_distinct_frequency.to_frame().reset_index()
# origin_distinct_frequency=pd.DataFrame(origin_distinct_frequency)
# origin_distinct_frequency.reset_index()
print(origin_distinct_frequency)

origin_distinct_frequency_ascending=origin_distinct_frequency.sort_values(origin_distinct_frequency.columns[0], ascending = True)
print(origin_distinct_frequency_ascending)
origin_distinct_frequency_ascending = origin_distinct_frequency_ascending.reset_index()
print(origin_distinct_frequency_ascending)





destination_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_dessr'].value_counts()
destination_distinct_frequency = destination_distinct_frequency.to_frame().reset_index()
# destination_distinct_frequency=pd.DataFrame(destination_distinct_frequency)
# destination_distinct_frequency.reset_index()
print(destination_distinct_frequency)

destination_distinct_frequency_ascending=destination_distinct_frequency.sort_values(destination_distinct_frequency.columns[0], ascending = True)
print(destination_distinct_frequency_ascending)
destination_distinct_frequency_ascending = destination_distinct_frequency_ascending.reset_index()
print(destination_distinct_frequency_ascending)






time_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_hrede'].value_counts()
time_distinct_frequency=time_distinct_frequency.to_frame().reset_index()
# time_distinct_frequency=pd.DataFrame(time_distinct_frequency)
# time_distinct_frequency.reset_index()
print(time_distinct_frequency)

if isinstance(time_distinct_frequency, pd.DataFrame):print ('do stuff')

time_distinct_frequency_ascending=time_distinct_frequency.sort_values(time_distinct_frequency.columns[0], ascending = True)
print(time_distinct_frequency_ascending)
time_distinct_frequency_ascending = time_distinct_frequency_ascending.reset_index()
print(time_distinct_frequency_ascending)


print(time_distinct_frequency_ascending['index'])
# print(time_distinct_frequency.index)
print(time_distinct_frequency_ascending.index[time_distinct_frequency_ascending['index'] == 100].tolist())

print('------------------------------------------------------------------------------------------------------')


odsurvey_abstract_mode2_timeunder2400=odsurvey_abstract_mode2_timeunder2400.head(1000)




odmatrix = np.zeros((n,n,k))

for ind in odsurvey_abstract_mode2_timeunder2400.index:

    t=odsurvey_abstract_mode2_timeunder2400['d_hrede'][ind]
    print (t)
    t1=time_distinct_frequency_ascending[time_distinct_frequency_ascending['index'] == t].index.tolist()


    o=odsurvey_abstract_mode2_timeunder2400['d_orisr'][ind]
    print (o)
    o1=origin_distinct_frequency_ascending[origin_distinct_frequency_ascending['index'] == o].index.tolist()


    d=odsurvey_abstract_mode2_timeunder2400['d_dessr'][ind]
    print (d)
    d1=destination_distinct_frequency_ascending[destination_distinct_frequency_ascending['index'] == d].index.tolist()

    print(t1,o1,d1)
    odmatrix[o1,d1,t1]=odmatrix[o1,d1,t1]+1
    print (odmatrix[o1,d1,t1])
    print('-------------------')

print(odmatrix)





plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = odmatrix
z, x, y = data.nonzero()
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()


