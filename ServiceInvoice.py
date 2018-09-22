# Establishing 'services' dictionary and populating with keys and values.
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service'}

# Establishing service cost variables and setting them to 0 for future use.
service_cost1 = 0
service_cost2 = 0

# Printing service menu with reference to dictionary values.
print('Davy\'s auto shop services')
print('Oil change -- $' + str(services['Oil change']))
print('Tire rotation -- $' + str(services['Tire rotation']))
print('Car wash -- $' + str(services['Car wash']))
print('Car wax -- $' + str(services['Car wax']))
print()

# Prompting user for input of desired services.
user_service1 = input('Select first service:\n')
user_service2 = input('Select second service:\n')
print()

# Printing invoice heading.
print('Davy\'s auto shop invoice')
print()

# checking user_service 1 for -, if true, prints relevant message stored in services
if user_service1 == '-':
    print('Service 1:', services[user_service1])

# if user_service1 is not -, prints relevant data stored in services and then reassigns service_cost1 value.
else:    
    print('Service 1:', user_service1 + ', $' + str(services[user_service1]))
    service_cost1 = services[user_service1]

# checking user_service2 for -, if true, prints relevant message stored in services
if user_service2 == '-':
    print('Service 2:', services[user_service2])

# if user_service2 is not -, prints relevant data stored in services and then reassigns service_cost2 value.
else:    
    print('Service 2:', user_service2 + ', $' + str(services[user_service2]))
    service_cost2 = services[user_service2]
print()

#calculates total service cost and prints.
service_total = service_cost1 + service_cost2
print('Total: $' + str(service_total))
    
