# Main Program
import os, sys, time
from playsound import playsound
import Railway-Reservation-System.Sounds.Sound
import Railway-Reservation-System.Main_Program.Main_Menu
import Railway-Reservation-System.Train.Train_Details
import Railway-Reservation-System.Train.Train_Update
import Railway-Reservation-System.Tickets.Ticket_Reservation
import Railway-Reservation-System.Tickets.Ticket_Cancellation
import Railway-Reservation-System.Tickets.PNR_Status
import Railway-Reservation-System.Help_and_Feedback.Help_and_Feedback
# Password Screen
import Railway-Reservation-System.Main_Program.Password_Screen
a = Railway-Reservation-System.Main_Program.Password_Screen.Password()
# Main Programs
while a :
    Railway-Reservation-System.Main_Program.Main_Menu.Menu()
    a = input("\nEnter your choice : ")
    time.sleep(0.5)
    print("\n\nInitiating......\n")
    time.sleep(1)
    os.system('cls')
    if a == "1":
        Railway-Reservation-System.Train.Train_Details.DETAIL()
    elif a == "2":
        a = Railway-Reservation-System.Train.Train_Update.CHOICE()
        if a == 1:
            Railway-Reservation-System.Train.Train_Update.INSERT()
        else :     
            Railway-Reservation-System.Train.Train_Update.UPDATE()
    elif a == "3":
        Railway-Reservation-System.Tickets.Ticket_Reservation.INSERT()
    elif a == "4":
        Railway-Reservation-System.Tickets.Ticket_Cancellation.CANCEL()
    elif a == "5":
        Railway-Reservation-System.Tickets.PNR_Status.STATUS()
    elif a == "6":
        a = Railway-Reservation-System.Help_and_Feedback.Help_and_Feedback.CHOICE()
        if a == 1:
            Railway-Reservation-System.Help_and_Feedback.Help_and_Feedback.HELP()
        else :     
            Railway-Reservation-System.Help_and_Feedback.Help_and_Feedback.FEEDBACK()
    elif a == "7" :
        time.sleep(0.5)
        print("\n\n \t\t\t\tQuitting....")
        Railway-Reservation-System.Sounds.Sound.THANKS()
        os.system("cls")
        sys.exit()
    else :
        print("\n\nPlease enter a valid input.... \n")
        Railway-Reservation-System.Sounds.Sound.INPUT()
        print("_"*80)
    time.sleep(1)
    Railway-Reservation-System.Sounds.Sound.CONTQUIT()
    a = input("\n \t  Enter M to go to Menu Or any Other key to end the program ")
    if a == "M":
        continue
    else :
        time.sleep(0.5)
        print("\nQuitting....")
        Railway-Reservation-System.Sounds.Sound.THANKS()
        time.sleep(1.5)
        os.system("cls")
        break