from datetime import datetime
current_time=datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format_1)
format_2=current_time.strftime("%m/%d/%Y")
print(format_2)
format_3=current_time.strftime("%A,%B %d,%Y")
print(format_3)
format_4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format_4)
format_5=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
print(format_5)
format_6=current_time.isoformat()
print(format_6)
