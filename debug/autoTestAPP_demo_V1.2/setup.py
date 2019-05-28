# _*_ coding:utf-8 _*_
import os

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
    import selenium
except :
    os.system('pip install selenium')
	
try:
    import appium
except :
    os.system('pip install Appium-Python-Client==0.29')
