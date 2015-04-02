name = raw_input("What's your name?\n> ")
age = int(raw_input("How old are you?\n> "))
uname = raw_input("What is your username?\n> ")

userOut = "Your name is %s, you are %d years old and your username is %s" % (name, age, uname)
print userOut

userFile = open('user_file.txt', 'w')
userFile.write(userOut)
userFile.close()
