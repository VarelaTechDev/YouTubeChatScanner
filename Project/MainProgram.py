import os
import threading

from CollectChat import ChatScan
from DownloadVideo import RunDownloader
from ComputeData import ComputeRawChatData
from Utilities import PrintFunctions, HelperFunctions


PrintFunctions.print_list_of_choices()


while(True):
    os.chdir(HelperFunctions.MainDirectory)

    try:
        choice = (int(input("Please pick an option. Type '0' to view your options: ")))

        if (choice == 0):
            PrintFunctions.print_list_of_choices()

        elif (choice == 1):
            ChatScan.gather_video_info()

        elif (choice == 2):
            RunDownloader.prerequisite_checklist()

        elif (choice == 3):
            print()

        elif (choice == 4):
            if (threading.active_count() > 1):
                print("You have some programs running in the background!")
                continue
            break

        elif (choice == 5):
            print("Number of jobs running: {}".format(threading.active_count() - 1))

        elif(choice == 6):
            HelperFunctions.printContents(HelperFunctions.RawChatDataDir, False, "Chat Data: ")
            HelperFunctions.printContents(HelperFunctions.VideoDownloadedDir, True, "Video Content: ")

        elif(choice == 7):
            ComputeRawChatData.DataCompute()

        else:
            PrintFunctions.print_improper_choice()

    except ValueError:
        PrintFunctions.print_improper_choice()
    print()