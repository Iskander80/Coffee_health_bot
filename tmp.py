# import urls
# import os, sys
# import subprocess
# from ping3 import ping
# from handlers.handlers import warning_message
# from handlers.handlers import approval_message
#
# print(ping('192.168.0.1'))
#
# for ip_dev in urls.ip_list:
#     with open('tmp.txt', 'w') as DEVNULL:
#         try:
#             subprocess.check_call(
#                 ['ping ', '-n', ' 2 ', ip_dev[0]],
# #                ['print', ip_dev[0]],
#
#                 stdout=DEVNULL,  # suppress output
#                 stderr=DEVNULL
#             )
#             print(ip_dev[1] + "yes")
#         except subprocess.CalledProcessError:
#             print("")
