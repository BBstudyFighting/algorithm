'''
Query a list of CITY names from STATION for cities that have an even ID number.  #even ID number : ID 짝수만!
Print the results in any order, but exclude duplicates from the answer.
'''
SELECT DISTINCT CITY #DISTINCT: 중복을 제거해줌
FROM STATION
WHERE ID%2 = 0
