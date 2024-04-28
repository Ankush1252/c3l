import Pyro4
uri = input("Enter the URI of the server: ")
concatenator = Pyro4.Proxy(uri)
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = concatenator.concatenate(str1, str2)
print("Concatenated string:", result)