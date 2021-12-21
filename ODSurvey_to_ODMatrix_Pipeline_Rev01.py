import numpy as np
import pandas as pd

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt




odsurvey_raw = pd.read_csv('C:/Users/test/Desktop/OD_Survey/OD_survey-Final_raw-data_2013.csv', encoding='utf8')
print(odsurvey_raw.head())


# Those columns which we need are filtered in

odsurvey_abstract_allmodes=odsurvey_raw.loc[:,['d_orisr','d_dessr','d_hrede','d_mode1']]
print(odsurvey_abstract_allmodes.head())


odsurvey_abstract_timeunder2400=odsurvey_abstract_allmodes.loc[odsurvey_abstract_allmodes['d_hrede']<=2400]
print(odsurvey_abstract_timeunder2400.head())



conditions = [
    (odsurvey_abstract_timeunder2400['d_hrede']>=0) & (odsurvey_abstract_timeunder2400['d_hrede']<100),
    (odsurvey_abstract_timeunder2400['d_hrede']>=100) & (odsurvey_abstract_timeunder2400['d_hrede']<200),
    (odsurvey_abstract_timeunder2400['d_hrede']>=200) & (odsurvey_abstract_timeunder2400['d_hrede']<300),
    (odsurvey_abstract_timeunder2400['d_hrede']>=300) & (odsurvey_abstract_timeunder2400['d_hrede']<400),
    (odsurvey_abstract_timeunder2400['d_hrede']>=400) & (odsurvey_abstract_timeunder2400['d_hrede']<500),
    (odsurvey_abstract_timeunder2400['d_hrede']>=500) & (odsurvey_abstract_timeunder2400['d_hrede']<600),
    (odsurvey_abstract_timeunder2400['d_hrede']>=600) & (odsurvey_abstract_timeunder2400['d_hrede']<700),
    (odsurvey_abstract_timeunder2400['d_hrede']>=700) & (odsurvey_abstract_timeunder2400['d_hrede']<800),
    (odsurvey_abstract_timeunder2400['d_hrede']>=800) & (odsurvey_abstract_timeunder2400['d_hrede']<900),
    (odsurvey_abstract_timeunder2400['d_hrede']>=900) & (odsurvey_abstract_timeunder2400['d_hrede']<1000),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1000) & (odsurvey_abstract_timeunder2400['d_hrede']<1100),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1100) & (odsurvey_abstract_timeunder2400['d_hrede']<1200),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1200) & (odsurvey_abstract_timeunder2400['d_hrede']<1300),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1300) & (odsurvey_abstract_timeunder2400['d_hrede']<1400),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1400) & (odsurvey_abstract_timeunder2400['d_hrede']<1500),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1500) & (odsurvey_abstract_timeunder2400['d_hrede']<1600),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1600) & (odsurvey_abstract_timeunder2400['d_hrede']<1700),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1700) & (odsurvey_abstract_timeunder2400['d_hrede']<1800),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1800) & (odsurvey_abstract_timeunder2400['d_hrede']<1900),
    (odsurvey_abstract_timeunder2400['d_hrede']>=1900) & (odsurvey_abstract_timeunder2400['d_hrede']<2000),
    (odsurvey_abstract_timeunder2400['d_hrede']>=2000) & (odsurvey_abstract_timeunder2400['d_hrede']<2100),
    (odsurvey_abstract_timeunder2400['d_hrede']>=2100) & (odsurvey_abstract_timeunder2400['d_hrede']<2200),
    (odsurvey_abstract_timeunder2400['d_hrede']>=2200) & (odsurvey_abstract_timeunder2400['d_hrede']<2300),
    (odsurvey_abstract_timeunder2400['d_hrede']>=2300) & (odsurvey_abstract_timeunder2400['d_hrede']<2400),
]

values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

odsurvey_abstract_timeunder2400['time_group']=np.select(conditions, values)


print(odsurvey_abstract_timeunder2400.head)


odsurvey_abstract_timeunder2400=odsurvey_abstract_timeunder2400.head(20)


for i in range(1, 2):
    odsurvey_abstract_timeunder2400.loc[odsurvey_abstract_timeunder2400['d_mode1'] == i]
    for j in range(1, 2):
        odsurvey_abstract_timeunder2400.loc[odsurvey_abstract_timeunder2400['time_group'] == j]

        origin_distinct_frequency=odsurvey_abstract_timeunder2400['d_orisr'].value_counts()
        origin_distinct_frequency = origin_distinct_frequency.to_frame().reset_index()
        # origin_distinct_frequency=pd.DataFrame(origin_distinct_frequency)
        # origin_distinct_frequency.reset_index()
        print(origin_distinct_frequency)
        # origin_distinct_frequency_ascending=origin_distinct_frequency.sort_values(origin_distinct_frequency.columns[0], ascending = True)
        # print(origin_distinct_frequency_ascending)
        # origin_distinct_frequency_ascending = origin_distinct_frequency_ascending.reset_index()
        # print(origin_distinct_frequency_ascending)

        for col in origin_distinct_frequency.columns: print(col)
        df = []

        for ind in origin_distinct_frequency.index:
            print(odsurvey_abstract_timeunder2400['d_orisr'])
            print('-------------------------------------')
            print(origin_distinct_frequency['index'][ind])
            print('----------------')
            odsurvey_abstract_timeunder2400_for_specific_origin=odsurvey_abstract_timeunder2400.loc[odsurvey_abstract_timeunder2400['d_orisr'] == origin_distinct_frequency['index'][ind]]
            print(odsurvey_abstract_timeunder2400_for_specific_origin)
            count_from_defined_origin_to_diff_destination=odsurvey_abstract_timeunder2400['d_dessr'].value_counts()
            count_from_defined_origin_to_diff_destination =  count_from_defined_origin_to_diff_destination.to_frame().reset_index()
            count_from_defined_origin_to_diff_destination = count_from_defined_origin_to_diff_destination.rename({'index': 'to', 'd_dessr': 'num of vehicles'}, axis='columns')
            print(count_from_defined_origin_to_diff_destination)
            count_from_defined_origin_to_diff_destination.insert(0, 'from', origin_distinct_frequency['index'][ind])
            # count_from_defined_origin_to_diff_destination['d_orisr']=origin_distinct_frequency['index'][ind]
            print(count_from_defined_origin_to_diff_destination)
            df.append(count_from_defined_origin_to_diff_destination)

            

            print('-------------------------------------------------------------------------------------------')

        
        print(df)


        # for ind in origin_distinct_frequency.index:
        #     result = pd.concat(count_from_defined_origin_to_diff_destination[ind])

        






        


            
        print('$OR,D2\n* From-Time  To-Time')
        print('   ',j-1,'         ',j)
        print('* Factor')
        print('*      from      to      num of vehicles')
        
           




        # startstationtripcountwithcoord.to_csv('C:/Users/test/Desktop/OD_Survey/finalformat/%%%%%%.od')








        # destination_distinct_frequency=odsurvey_abstract_timeunder2400['d_dessr'].value_counts()
        # destination_distinct_frequency = destination_distinct_frequency.to_frame().reset_index()
        # # destination_distinct_frequency=pd.DataFrame(destination_distinct_frequency)
        # # destination_distinct_frequency.reset_index()
        # print(destination_distinct_frequency)
        # destination_distinct_frequency_ascending=destination_distinct_frequency.sort_values(destination_distinct_frequency.columns[0], ascending = True)
        # print(destination_distinct_frequency_ascending)
        # destination_distinct_frequency_ascending = destination_distinct_frequency_ascending.reset_index()
        # print(destination_distinct_frequency_ascending)



        # time_distinct_frequency=odsurvey_abstract_timeunder2400['d_hrede'].value_counts()
        # time_distinct_frequency=time_distinct_frequency.to_frame().reset_index()
        # # time_distinct_frequency=pd.DataFrame(time_distinct_frequency)
        # # time_distinct_frequency.reset_index()
        # print(time_distinct_frequency)
        # if isinstance(time_distinct_frequency, pd.DataFrame):print ('do stuff')
        # time_distinct_frequency_ascending=time_distinct_frequency.sort_values(time_distinct_frequency.columns[0], ascending = True)
        # print(time_distinct_frequency_ascending)
        # time_distinct_frequency_ascending = time_distinct_frequency_ascending.reset_index()
        # print(time_distinct_frequency_ascending)
        # print(time_distinct_frequency_ascending['index'])

        # print(time_distinct_frequency_ascending.index[time_distinct_frequency_ascending['index'] == 100].tolist())



        # n=odsurvey_abstract_timeunder2400.d_orisr.nunique()
        # m=odsurvey_abstract_timeunder2400.d_dessr.nunique()
        # k=odsurvey_abstract_timeunder2400.d_hrede.nunique()

        # print(n,m,k)


        # odmatrix = np.zeros((n,n,k))

        # for ind in odsurvey_abstract_timeunder2400.index:

        #     t=odsurvey_abstract_timeunder2400['d_hrede'][ind]
        #     print (t)
        #     t1=time_distinct_frequency_ascending[time_distinct_frequency_ascending['index'] == t].index.tolist()


        #     o=odsurvey_abstract_timeunder2400['d_orisr'][ind]
        #     print (o)
        #     o1=origin_distinct_frequency_ascending[origin_distinct_frequency_ascending['index'] == o].index.tolist()


        #     d=odsurvey_abstract_timeunder2400['d_dessr'][ind]
        #     print (d)
        #     d1=destination_distinct_frequency_ascending[destination_distinct_frequency_ascending['index'] == d].index.tolist()

        #     print(t1,o1,d1)
        #     odmatrix[o1,d1,t1]=odmatrix[o1,d1,t1]+1
        #     print (odmatrix[o1,d1,t1])
        #     print('-------------------')

        # print(odmatrix)


    











# origin_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_orisr'].value_counts()
# origin_distinct_frequency = origin_distinct_frequency.to_frame().reset_index()
# # origin_distinct_frequency=pd.DataFrame(origin_distinct_frequency)
# # origin_distinct_frequency.reset_index()
# print(origin_distinct_frequency)

# origin_distinct_frequency_ascending=origin_distinct_frequency.sort_values(origin_distinct_frequency.columns[0], ascending = True)
# print(origin_distinct_frequency_ascending)
# origin_distinct_frequency_ascending = origin_distinct_frequency_ascending.reset_index()
# print(origin_distinct_frequency_ascending)





# destination_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_dessr'].value_counts()
# destination_distinct_frequency = destination_distinct_frequency.to_frame().reset_index()
# # destination_distinct_frequency=pd.DataFrame(destination_distinct_frequency)
# # destination_distinct_frequency.reset_index()
# print(destination_distinct_frequency)

# destination_distinct_frequency_ascending=destination_distinct_frequency.sort_values(destination_distinct_frequency.columns[0], ascending = True)
# print(destination_distinct_frequency_ascending)
# destination_distinct_frequency_ascending = destination_distinct_frequency_ascending.reset_index()
# print(destination_distinct_frequency_ascending)






# time_distinct_frequency=odsurvey_abstract_mode2_timeunder2400['d_hrede'].value_counts()
# time_distinct_frequency=time_distinct_frequency.to_frame().reset_index()
# # time_distinct_frequency=pd.DataFrame(time_distinct_frequency)
# # time_distinct_frequency.reset_index()
# print(time_distinct_frequency)

# if isinstance(time_distinct_frequency, pd.DataFrame):print ('do stuff')

# time_distinct_frequency_ascending=time_distinct_frequency.sort_values(time_distinct_frequency.columns[0], ascending = True)
# print(time_distinct_frequency_ascending)
# time_distinct_frequency_ascending = time_distinct_frequency_ascending.reset_index()
# print(time_distinct_frequency_ascending)


# print(time_distinct_frequency_ascending['index'])
# # print(time_distinct_frequency.index)
# print(time_distinct_frequency_ascending.index[time_distinct_frequency_ascending['index'] == 100].tolist())

# print('------------------------------------------------------------------------------------------------------')


# odsurvey_abstract_mode2_timeunder2400=odsurvey_abstract_mode2_timeunder2400.head(10)




# odmatrix = np.zeros((n,n,k))

# for ind in odsurvey_abstract_mode2_timeunder2400.index:

#     t=odsurvey_abstract_mode2_timeunder2400['d_hrede'][ind]
#     print (t)
#     t1=time_distinct_frequency_ascending[time_distinct_frequency_ascending['index'] == t].index.tolist()


#     o=odsurvey_abstract_mode2_timeunder2400['d_orisr'][ind]
#     print (o)
#     o1=origin_distinct_frequency_ascending[origin_distinct_frequency_ascending['index'] == o].index.tolist()


#     d=odsurvey_abstract_mode2_timeunder2400['d_dessr'][ind]
#     print (d)
#     d1=destination_distinct_frequency_ascending[destination_distinct_frequency_ascending['index'] == d].index.tolist()

#     print(t1,o1,d1)
#     odmatrix[o1,d1,t1]=odmatrix[o1,d1,t1]+1
#     print (odmatrix[o1,d1,t1])
#     print('-------------------')

# print(odmatrix)





# # plt.rcParams["figure.figsize"] = [7.00, 3.50]
# # plt.rcParams["figure.autolayout"] = True
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # data = odmatrix
# # z, x, y = data.nonzero()
# # ax.scatter(x, y, z, c=z, alpha=1)
# # plt.show()


