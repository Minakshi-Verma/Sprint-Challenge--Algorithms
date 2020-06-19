'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # print(word[:2])
    
    # find the basecase  
    if len(word)<2:   # word is supposed to have atleast 2 letters to find 'th'
        return 0
    
    elif word[:2] == 'th': # checks if first two letters of the word has 'th        
        return 1+ count_th(word[2:])
    
    else: # else if "th' not found, move 1 letter ahead and check the 'th' again
        return count_th(word[1:])    


count_th("andthegh")

 
    
