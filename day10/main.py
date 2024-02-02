# Functions with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input"
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"


print(format_name("shuBHAm", "THORat"))
print(format_name("", ""))

