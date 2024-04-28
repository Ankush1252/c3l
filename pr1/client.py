import xmlrpc.client
server = xmlrpc.client.ServerProxy('http://localhost:8000')
n = int(input("Enter the number to calculate factorial: "))
result = server.calculate_factorial(n)
print(f"The factorial of {n} is: {result}")