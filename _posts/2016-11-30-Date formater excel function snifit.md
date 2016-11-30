---
layout: post
title: Dateformater, Excel function snifit
---
날짜 형식으로 변환해야 할 숫자가 4 - 3 문자로 이루어져 있고, 함수가 쓰여진 셀의 왼쪽 열에 있을 경우.

'''
IF(LEN(ADDRESS(ROW(),COLUMN()-1,4))=4,(CONCATENATE("2016","-",LEFT(ADDRESS(ROW(),COLUMN()-1,4),2),"-",RIGHT(ADDRESS(ROW(),COLUMN()-1,4),2))),IF(LEN(ADDRESS(ROW(),COLUMN()-1,4))=3,(CONCATENATE("2016","-","0",LEFT(ADDRESS(ROW(),COLUMN()-1,4),1),"-",RIGHT(A2,2)))," "))
'''
