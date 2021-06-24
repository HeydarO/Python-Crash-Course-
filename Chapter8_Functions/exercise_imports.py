"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

### import module_name
# import user_info
#
# user_profile = user_info.build_profile('albert', 'einstein',
#                             location = 'princeton',
#                             field = 'physics')
# print(user_profile)

### from module_name import function_name
# from user_info import build_profile
#
# user_profile = build_profile('albert', 'einstein',
#                             location = 'princeton',
#                             field = 'physics')
# print(user_profile)

### from module_name import function_name as fn
# from user_info import build_profile as bp
#
# user_profile = bp('albert', 'einstein',
#                             location = 'princeton',
#                             field = 'physics')
# print(user_profile)

### import module_name as mn
# import user_info as user
#
# user_profile = user.build_profile('albert', 'einstein',
#                             location = 'princeton',
#                             field = 'physics')
# print(user_profile)

### from module_name import *
from user_info import *

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                            field = 'physics')
print(user_profile)
