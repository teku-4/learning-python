#non coalesive oprators
#if the value is non diplays the default value

value=None
result=value or 10
print(f"since the value is {value} the default value is {result}")
#if the value is false diplay default value
value=False
default_value= value or 300
print(f"since the value is {value} the default value is{default_value}")