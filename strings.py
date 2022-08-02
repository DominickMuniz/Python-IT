
#checks if input is a palindrome
def is_palindrome(input_string):
    original_string = ""
    reverse_string = ""
    
    for letter in input_string.strip():
	  # Add non-blank letters to the 
		# end of one string, and to the front
		# of the other string
        new_string = new_string+letter.replace(" ","")
        reverse_string = letter.replace(" ", "")+ reverse_string
	
    if new_string.lower() == reverse_string.lower():
	    return True
    return False 
