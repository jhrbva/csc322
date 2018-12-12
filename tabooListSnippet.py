def tabooword_filter(string,taboolist) :
    dirty_file = string.lower().split()
    bad_words = taboolist.split()

    diff = set(dirty_file) - set(bad_words)
    clean_list = [item for item in dirty_file if item in diff]
    clean_file = ' '.join(clean_list)
    
    return clean_file

#test
taboo_list = "bastard idiot shit jackass"
my_file = "hello you bastard nice to meet you jackass"
tabooword_filter(my_file,taboo_list)
