# import os

# print(os.path.dirname(os.path.abspath(__file__)))


import os
print(os.access("C:\\html\\Orient_Classical\\translation\\hanja\\static\\pdf", os.F_OK)) # 파일 자체가 존재하는지 체크 (정상 : True)
print(os.access("C:\\html\\Orient_Classical\\translation\\hanja\\static\\pdf", os.R_OK)) # 읽기 권한이 있는지 체크 (정상 : True)
print(os.access("C:\\html\\Orient_Classical\\translation\\hanja\\static\\pdf", os.W_OK)) # 쓰기 권한이 있는지 체크 (정상 : True)
print(os.access("C:\\html\\Orient_Classical\\translation\\hanja\\static\\pdf", os.X_OK)) # 실행 권한이 있는지 체크 (정상 : True)