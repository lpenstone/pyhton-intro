global_var = "I can be accessed anywhere!"

def print_vars(passed_var):
	local_var = "I can only be accessed inside the print_vars function!"
	print("<---- INSIDE FUNCTION ---->")
	print("passed:" + passed_var) # "I am sent into the function"
	print("local:" + local_var) # "I can only be accessed inside the print_vars function!"
	print("global:" + global_var) # "I can be accessed anywhere!"

print_vars("I am sent into the function")

print("<---- OUTSIDE FUNCTION ---->")
# print("passed:" + passed_var) # NameError: name 'passed_var' is not defined
# print("local:" + local_var) # NameError: name 'local_var' is not defined
print("global:" + global_var) # "I can be accessed anywhere!"