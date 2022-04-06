import os;
from sys import platform

xlsx_path = os.getcwd() + "/Input_Xlsxs"
binary_path = os.getcwd() + "/Output_Binaries"
script_path = os.getcwd() + "/Output_Scripts"

##WINDOW
if platform == "win32":
    project_path = ""
##darwin means 'Mac'
elif platform == "darwin":
    project_path = ""
else:
    project_path = "SomethingWrong : no OS"

project_binary_path = project_path + "/Assets/Resources/BinaryTextData"
project_script_path = project_path + "/Assets/01_Scripts/Utils/TextTableManage"

#영어 , 한국어 , 일본어 , 중국어(간체) , 중국어(번체) , 독일어 ,  러시아어 , 스페인어 , 프랑스어
languages = ["EN" , "KR" , "JP" , "CH_SIM" , "CH_TR" , "GE" , "RU",  "SP" , "FR"]
languages_comment = ["English" , "Korean" , "Japnese" , "Chinese Simplified" , "Chinese Traditional" , \
                    "German" , "Russian",  "Spanish" , "French"]
