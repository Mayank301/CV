import player_management as pm
 
def main():
    no_players=int(input("Enter the no. of players:"))
 
    # Fill your code here for getting inputs, creating appropriate object and  
    # invoke necessary methods as per the requirement specification.
    player_obj=pm.PlayerManagement()
    for i in range(no_players):
        print("Enter the player details ",i+1,":")
        name,no_of_matches,points=input().split(':')
        player_obj.add_player_details(name,no_of_matches,float(points))
    status_category=input("Enter the status category to search:")
    player_rec=player_obj.view_player_details(status_category)
    # Fill your code for invoking the appropriate method(s) as per the requirements
    if len(player_rec)!=0:
        print("The no. of player in this category:",len(player_rec))
        for i in player_rec:
            print("Player Name:",i.get_player_name())
            print("No of matches:",i.get_no_of_matches())
            print("Points:",i.get_points())
    else:
        print("No players found in this category")

if __name__=='__main__':
    main()