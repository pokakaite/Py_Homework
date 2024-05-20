from models import *

greeting = Greeting()

donut = BasicDonat()
choco_donut = ChocoDonut()
donut_item = DonutItem(donut)
choco_donut_item = DonutItem(choco_donut)


list_items = ListItems()
list_items.add_to_list(donut_item)
list_items.add_to_list(choco_donut_item)


show_items = ShowItems()




########################
greeting.show()
show_items.show(list_items.get_list())
