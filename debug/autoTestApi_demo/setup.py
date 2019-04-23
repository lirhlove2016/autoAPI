# _*_ coding:utf-8 _*_
import os

try:
    import requests
except :
    os.system('pip install requests')

try:
    import xlrd
except :
    os.system('pip install xlrd')

try:
    import xlwt
except :
    os.system('pip install xlwt')
try:
    import xlutils
except :
    os.system('pip install xlutils==2.0.0')
	
try:
    import jsonpatht
except :
    os.system('pip install jsonpath==0.80')