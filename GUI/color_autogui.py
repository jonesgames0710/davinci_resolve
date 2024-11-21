import pyautogui
import time



  #ウィンドウの四角形をクリック
#50 794
pyautogui.moveTo(8059,2414,duration=0)
pyautogui.click()

#変形「パン」をクリック
#480 795
pyautogui.moveTo(8929,2424,duration=0)
pyautogui.click()

#「座標」を入力
#58.31
pyautogui.write('57.29')

#変形「ティルト」をクリック
#608 794
pyautogui.moveTo(9158,2424,duration=0)
pyautogui.click()
#「座標」を入力
#44.50
pyautogui.write('44.43')

#ソフトネス　ソフト１をクリック
#490 883
pyautogui.moveTo(8950,2575,duration=0)
pyautogui.click()

#「0」を入力
pyautogui.write('0')
pyautogui.press('\t')
pyautogui.press('\t')

#ソフトネス　ソフト２をクリック
#604 883
#pyautogui.moveTo(604,883,duration=0)
#pyautogui.click()

#「0」を入力
pyautogui.write('0')
pyautogui.press('\t')
pyautogui.press('\t')

#ソフトネス　ソフト３をクリック
#490 910
#pyautogui.moveTo(490,910,duration=0)
#pyautogui.click()

#「0」を入力
pyautogui.write('0')
pyautogui.press('\t')
pyautogui.press('\t')


#ソフトネス　ソフト４をクリック
#610 910
#pyautogui.moveTo(610,910,duration=0)
#pyautogui.click()

#「0」を入力
pyautogui.write('0')

#エフェクトのブラー(ガウス)からノードまでドラッグ
#950 180から660 260
pyautogui.moveTo(9448,1696,duration=0)
pyautogui.dragTo(8897,1357,button='left',duration=0)


#ブラー(ガウス)の強度をクリック
#1190 156
pyautogui.moveTo(9888,1359,duration=0)
pyautogui.click()

#「0,7」を入力
pyautogui.write('0.7')
pyautogui.press('return')

