distance = int(input('How far would you like to travel in miles? '))
match distance:
    case _ if distance < 3:
        print('It\'s better to walk this distance')
    case _ if 3 <= distance < 3000:
        print('It\'s better to travel by car')
    case _ if distance >= 3000:
        print('It\'s better to fly by plane')
