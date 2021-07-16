# collaboration_project

The ROI should work on the matrix of catchments’ characteristics X, The matrix X is 50 x 13, or 13 x 50, the 50 rows represent each of the 50 catchments we have and the 13 columns represent the 13 characteristics we have (e.g. catchment area, amount of fertilisers applied, WWTPs’ total capacity). 


The main goal of this study is to estimate WQ percentiles at ungauged catchment/watershed. We proposed a regional statistical approach that consists of two steps. The first step is the region of influence (ROI), which is applied to identify the similar gauged catchments for a target ungauged catchment.  The second step is the nonparametric TS multiple regression.

To evaluate the regional models proposed We applied cross-validation approach by assuming each of the 50 catchments we have as ungauged catchment (target catchment) and use the remaining 49 catchments to estimate the WQ percentile at this target catchment.

Thus, in each of these 50 steps of the cross-validation, the ROI consists of calculating the Euclidean distance between the assumed ungauged catchment and the remaining 49 catchments, sort them in ascending order, and apply two criteria to identify the size of catchments to include as similar to be used in the following step of the model.
