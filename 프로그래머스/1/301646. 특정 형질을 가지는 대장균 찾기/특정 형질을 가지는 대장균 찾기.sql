SELECT 
    COUNT(*) as COUNT
FROM 
    # 이진수 계산법에 따라 형질 유무를 나타내는 칼럼을 계산 
    (SELECT
        (CASE WHEN GENOTYPE % 2 = 1 THEN 1 ELSE 0 END) as TYPE1,
        (CASE WHEN GENOTYPE DIV 2 % 2 = 1 THEN 1 ELSE 0 END) as TYPE2,
        (CASE WHEN GENOTYPE DIV 2 DIV 2 % 2 = 1 THEN 1 ELSE 0 END) as TYPE3,
        (CASE WHEN GENOTYPE DIV 2 DIV 2 DIV 2 % 2 = 1 THEN 1 ELSE 0 END) as TYPE4
    FROM ECOLI_DATA) AS SUB
# 조건에 맞는 형질을 가지는 대장균 행만 추출 
WHERE TYPE2 = 0 and (TYPE1 = 1 OR TYPE3 = 1);