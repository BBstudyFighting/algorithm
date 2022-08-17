SELECT quartet
     , round(avg(x),2) AS x_mean
     , round(variance(x),2) AS x_var
     , round(avg(y),2) AS y_mean
     , round(variance(y),2) AS y_var
FROM points
GROUP BY quartet;