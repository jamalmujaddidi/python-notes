# Function Definition and Calling With and Without Parameters

def greet():
    print("Hello, John!")


greet()


def greet_user(first_name, last_name):
    print(f"Hi dear customer Mr. {first_name} {last_name}")
    print(f"What can I do for you, {first_name}?")


greet_user("John", "Smith")