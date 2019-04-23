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
    import jsonpath
except :
    os.system('pip install jsonpath==0.80')
	
try:
    import selenium
except :
    os.system('pip install selenium')
	
try:
    import appium
except :
    os.system('pip install Appium-Python-Client==0.29')
