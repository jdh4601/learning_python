# global scope
greeting = "Hello" 

# local scope
def change_greeting(new_greeting):
    greeting = new_greeting
# local scope
def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()
