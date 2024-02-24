# Please do not alter the given template
# You can add any number of methods and attributes as you required without changing the given template
 
import player as pl
 
class PlayerManagement:
    def __init__(self):
        self.__player_list=[]

 
    def add_player_details(self,player_name,no_of_matches,points):
        #Fill your code here
        p_obj=pl.Player(player_name,no_of_matches,points)
        p_obj.find_status_category()
        self.__player_list.append(p_obj)
        return

    def view_player_details(self,status_category):
        #Fill your code here
        lst=[]
        for i in self.__player_list:
            if status_category==i.get_status_category():
                lst.append(i)
        return lst #TODO CHANGE THIS RETURN VALUE