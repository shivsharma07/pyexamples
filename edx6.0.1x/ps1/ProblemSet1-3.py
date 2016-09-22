def item_order(order):
    menuItems = ['salad', 'hamburger', 'water']
    orderItems = order.split(' ')
    saladOrderCount = 0
    hamburgerOrderCount = 0
    waterOrderCount = 0
    for item in orderItems:
        if item == menuItems[0]:
            saladOrderCount += 1
        elif item == menuItems[1]:
            hamburgerOrderCount += 1
        elif item == menuItems[2]:
            waterOrderCount += 1
    return 'salad:'+ str(saladOrderCount)+' hamburger:'+str(hamburgerOrderCount)+' water:'+str(waterOrderCount)
    
print item_order("salad water hamburger salad hamburger")