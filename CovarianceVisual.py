# from matplotlib import pyplot as plt
# from matplotlib import cm as cm
# from pandas import DataFrame, read_csv
#
# df = read_csv(f)
# df=df[0:10]
#
#
# def correlation_matrix(df,method='pearson'):
#
#     fig = plt.figure()
#     ax1 = fig.add_subplot(111)
#
#     cmap = cm.get_cmap('jet', 30)
#     cax = ax1.imshow(df.corr(method=method), interpolation="nearest", cmap=cmap)
#     ax1.grid(False)
#     plt.title('Feature Correlation')
#     labels=['Sex','Length','Diam','Height','Whole','Shucked','Viscera','Shell','Rings',]
#
#     ax1.set_xticklabels(labels,fontsize=6)
#     ax1.set_yticklabels(labels,fontsize=6)
#
#     # Add colorbar, make sure to specify tick locations to match desired ticklabels
#     fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
#     plt.show()
#
# correlation_matrix(df)