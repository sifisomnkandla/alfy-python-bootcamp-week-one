#Dictionaries

monthConversions = {
    3: 'January',
    'Feb' : 'February',
    'Mar' : 'March',
    'Apr' : 'April',
    'May' : 'May',
    'Jun' : 'June',
    'Jul' : 'July',
    'Aug' : 'August',
    'Sep' : 'September',
    'Oct' : 'October',
    'Nov' : 'November',
    'Dec' : 'December'
}

#Obtain using Rudimentary find option
print(monthConversions[3])

#Obtain using the Get function. Allows error trapping and use of a default value
print(monthConversions.get('Jant', 'Not a valid key'))