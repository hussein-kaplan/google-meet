import webbrowser
import pyautogui
import schedule
import time
meeturl = str(input("meet url for class: "))
starting_time = str(input('Enter the meeting started time(hh:mm): '))
ending_time = str(input('Enter the meeting endet in minute: '))
comment = str(input("are you whant comment (Enter yes or no) :"))
if comment == "yes":
    my_comment = str(input('Enter the comment : '))
    comment_time = str(input('Enter the comment time example 10 menute the comment whil be aplay after 10 menute started the class : '))
def job():
    webbrowser.open(meeturl)
    time.sleep(10)
    pyautogui.moveTo(433, 488) 
    pyautogui.click()
    pyautogui.moveTo(423, 470) 
    pyautogui.click()
    #-- if he want to comment
    if comment == "yes":
        end_com = int(comment_time) * 60
        time.sleep(int(end_com))
        pyautogui.moveTo(86, 686) 
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(230, 612) 
        pyautogui.click()
        time.sleep(5)
        pyautogui.write(my_comment)   
        time.sleep(5) 
        pyautogui.press('enter')    
    end = int(ending_time) * 60
    time.sleep(int(end))
    pyautogui.moveTo(584, 679) 
    pyautogui.click()
schedule.every().saturday.at(str(starting_time)).do(job)
while True:
    schedule.run_pending()
    time.sleep(1)