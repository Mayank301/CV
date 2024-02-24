# Please do not change the given template.  Fill your code only in the provided places.
 
class Player:
    # Write the code for the parameterized constructor here
    def __init__(self,player_name,no_of_matches,points):
        self.__player_name=player_name
        self.__no_of_matches=no_of_matches
        self.__points=points;
        self.__status_category=""

    def get_player_name(self):
        return self.__player_name
    def set_player_name(self,player_name):
        self.__player_name=player_name
    def get_no_of_matches(self):
        return self.__no_of_matches
    def set_no_of_matches(self,no_of_matches):
        self.__no_of_matches=no_of_matches
    def get_points(self):
        return self.__points
    def set_points(self,points):
        self.__points=points
    def get_status_category(self):
        return self.__status_category
    def set_status_category(self,status_category):
        self.__status_category=status_category

    def find_status_category(self):
        # Fill your code here 
        if self.__points<=0:
            self.__status_category="Miserable"
        elif self.__points>=1 and self.__points<=60:
            self.__status_category="Tolerable"
        elif self.__points>=51 and self.__points<=75:
            self.__status_category="Satisfactory"
        else:
            self.__status_category="Excellent"
        return