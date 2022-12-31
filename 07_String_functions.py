story="once there was a time there was a youtuber named Harry who uploaded python course with notes"
print(story[0:5])
#STRING FUNCTIONS
print(len(story)) # length of the story is returned
print(story.endswith("notes"))# it will return true if the value # ends with the notes so true else false
print(story.count("a"))#calculating the number of occurence of character or word
print(story.capitalize()) # it will automatically convert the first letter of word in capital
print(story.find("Harry"))# return the integer position if found and if not found so -1, but it will only show first occurence
print(story.replace("Harry","CodeWithHarry"))#it will change all occurence to the new value of string

