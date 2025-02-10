import pyautogui
import win32gui, win32com.client
import tkinter as tk
import time
import threading
from datetime import datetime, timedelta
from tkinter import *
from tkinter.scrolledtext import ScrolledText

data = []
posData = []
xlBIndex = -1
xlEIndex = -1
index = 0
filePath = "readFile.txt"
with open(filePath, 'r', encoding='utf-8') as file:
    for line in file:
        row = line.strip()  # 读取并解析每一行数据
        data.append(row)

for item in data:
    if item.startswith("xlb"):
        xlBIndex = index
    elif item.startswith('xle'):
        xlEIndex = index
    index += 1

posFilePath = "posReadFile.txt"
with open(posFilePath, 'r', encoding='utf-8') as file:
    for line in file:
        row = line.strip()  # 读取并解析每一行数据
        posData.append(row)

tTime = data[1].split(",")
cTime = data[2].split(",")

defaultDiff = int(data[0])
weihuTimes = int(data[3])
cunDangTime = int(data[4])
guJuanTimes = int(data[5])
xianJiTimes = int(data[6])
defaultTimes = 80  # 次数
maxDiff = 42
pyautogui.FAILSAFE = False

kkPic = "kk.png"
kkPlatIconPic = "kkPlatIcon.png"
loginPic = "login.png"
xiuxianPic = "xiuxian.png"
createPic = "create.png"
createPic1 = "create1.png"
createPic2 = "create2.png"
firstFloorPic = "firstfloor.png"
beginPic2 = "begin.png"
diffPic = "diff.png"
defaultPic = "default.png"
atwait = "atwait.png"
readyPic = "ready.png"
f1Pic = "f1.png"
fukuangPic = "fukuang.png"

def mousePos():
    currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
    run_log_print(f'{currentMouseX},{currentMouseY}')
    root.after(1000, mousePos)

def mouseMoveClick(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click()

def moveRightClick(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click(button='right')

def leftClick(index):
    dataSplit = posData[index].split(',')
    mouseMoveClick(int(dataSplit[0]), int(dataSplit[1]))

def rightClick(index):
    dataSplit = posData[index].split(',')
    moveRightClick(int(dataSplit[0]), int(dataSplit[1]))

def keyborad(x):
    pyautogui.press(x)
    time.sleep(0.2)

def hotkey(x, y):
    pyautogui.hotkey(x, y)
    time.sleep(0.2)

def run_log_print(message):
    run_log.config(state=tk.NORMAL)
    run_log.insert(tk.END, message + "\n")
    run_log.see(tk.END)
    run_log.update()
    run_log.config(state=tk.DISABLED)

def closeWnd():
    root.destroy()

def clickStart():
    while True:
        result = checkWnd('Warcraft III')
        if result:
            return True
        result = findButton(beginPic2,True)
        if result:
            return True

def findButtonClick(x, b):
    while True:
        try:
            # 找到指定图片在屏幕上的位置
            imageLocation = pyautogui.locateOnScreen(x, grayscale=True, confidence=0.8)
            run_log_print(f'选中 {x}')
            if b:
                pyautogui.click(imageLocation)
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
        except pyautogui.FailSafeException:
            run_log_print(f"{x} FailSafe触发，操作可能被阻止")
            time.sleep(1)


def findButton(x, b):
    try:
        # 找到指定图片在屏幕上的位置
        imageLocation = pyautogui.locateOnScreen(x, grayscale=True, confidence=0.8)
        run_log_print(f'选中 {x}')
        if b:
            pyautogui.click(imageLocation)
        return True
    except pyautogui.ImageNotFoundException:
        # run_log_print(f"{x} 没找到")
        return False
    except pyautogui.FailSafeException:
        run_log_print(f"{x} FailSafe触发，操作可能被阻止")
        return False


def findDoubleButton(x, b):
    try:
        # 找到指定图片在屏幕上的位置
        imageLocation = pyautogui.locateOnScreen(x, grayscale=True, confidence=0.8)
        run_log_print(f'选中 {x}')
        # 如果需要移动鼠标到该图片位置
        # pyautogui.moveTo(imageLocation)
        # 点击找到的图片位置
        if b:
            pyautogui.doubleClick(imageLocation)
        return True
    except pyautogui.ImageNotFoundException:
        # run_log_print(f"{x} 没找到")
        return False
    except pyautogui.FailSafeException:
        run_log_print(f"{x} FailSafe触发，操作可能被阻止")
        return False


def createRoom():
    findButtonClick(createPic, True)
    time.sleep(1)
    findButtonClick(createPic1, True)
    time.sleep(1)
    keyborad('232142141ffdsf')
    time.sleep(2)
    findButtonClick(createPic2, True)
    time.sleep(2)


def openPlatCreateRoom():
    findDoubleButton(kkPic, True)
    findButtonClick(loginPic, True)
    findButtonClick(kkPlatIconPic, False)
    time.sleep(2)
    mouseMoveClick(922, 88)
    time.sleep(1)
    findButtonClick(xiuxianPic, True)
    createRoom()


def selectDiff7():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('q')
    time.sleep(1)
    if diff == 1:
        keyborad('q')
    elif diff == 2:
        keyborad('w')
    elif diff == 30:
        keyborad('e')
    elif diff == 4:
        keyborad('r')
    elif diff == 5:
        keyborad('a')
    elif diff == 6:
        keyborad('s')
    elif diff == 7:
        keyborad('d')
    run_log_print(message=f'难度{diff}')

def selectDiff14():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('w')
    time.sleep(1)
    if diff == 8:
        keyborad('q')
    elif diff == 9:
        keyborad('w')
    elif diff == 10:
        keyborad('e')
    elif diff == 11:
        keyborad('r')
    elif diff == 12:
        keyborad('a')
    elif diff == 13:
        keyborad('s')
    elif diff == 14:
        keyborad('d')
    run_log_print(message=f'难度{diff}')

def selectDiff21():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('e')
    time.sleep(1)
    if diff == 15:
        keyborad('q')
    elif diff == 16:
        keyborad('w')
    elif diff == 17:
        keyborad('e')
    elif diff == 18:
        keyborad('r')
    elif diff == 19:
        keyborad('a')
    elif diff == 20:
        keyborad('s')
    elif diff == 21:
        keyborad('d')
    run_log_print(message=f'难度{diff}')

def selectDiff30():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('r')
    time.sleep(1)
    if diff == 22:
        keyborad('q')
    elif diff == 23:
        keyborad('w')
    elif diff == 24:
        keyborad('e')
    elif diff == 25:
        keyborad('r')
    elif diff == 26:
        keyborad('a')
    elif diff == 27:
        keyborad('s')
    elif diff == 28:
        keyborad('d')
    elif diff == 29:
        keyborad('z')
    elif diff == 30:
        keyborad('x')
    run_log_print(message=f'难度{diff}')

def selectDiff40():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('a')
    time.sleep(1)
    if diff == 31:
        keyborad('q')
    elif diff == 32:
        keyborad('w')
    elif diff == 33:
        keyborad('e')
    elif diff == 34:
        keyborad('r')
    elif diff == 35:
        keyborad('a')
    elif diff == 36:
        keyborad('s')
    elif diff == 37:
        keyborad('d')
    elif diff == 38:
        keyborad('z')
    elif diff == 39:
        keyborad('x')
    elif diff == 40:
        keyborad('c')
    run_log_print(message=f'难度{diff}')

def selectOther():
    diff = int(entryN.get())
    time.sleep(0.5)
    keyborad('s')
    time.sleep(1)
    if diff == 41:
        keyborad('q')
    elif diff == maxDiff:
        keyborad('w')
    run_log_print(message=f'难度{diff}')

def chooseDiff():
    findButtonClick(diffPic, False)
    diff = int(entryN.get())
    if diff == 0:
        keyborad('z')
    elif diff <= 7:
        selectDiff7()
    elif diff <= 14:
        selectDiff14()
    elif diff <= 21:
        selectDiff21()
    elif diff <= 30:
        selectDiff30()
    elif diff <= 40:
        selectDiff40()
    else:
        selectOther()

def keyQ(x):
    for i in range(0, x):
        keyborad('q')

def keyW(x):
    for i in range(0, x):
        keyborad('w')

def keyE(x):
    for i in range(0, x):
        keyborad('e')

def keyQWER(x):
    for i in range(0, x):
        keyborad('q')
        keyborad('w')
        keyborad('e')
        keyborad('r')
    keyborad('r')

def keyQE(x):
    keyQ(x)
    keyborad('e')

def keyQW(x, clickesc):
    keyborad('r')
    for i in range(0, x):
        keyborad('q')
        keyborad('w')
    if clickesc:
        keyborad('esc')

# 分身
def fenshenD():
    keyborad('esc')
    keyborad('f1')
    keyborad('d')

def buildHero():
    keyborad('f1')  # 建英雄
    rightClick(3)
    time.sleep(1)
    keyborad('b')
    keyborad('s')
    leftClick(4)
    time.sleep(0.2)
    leftClick(5)
    hotkey('ctrl', '2')

# 建光环
def buildGuanghuan():
    keyborad('b')
    keyborad('a')
    leftClick(1)
    leftClick(2)
    hotkey('ctrl', '4')
    time.sleep(0.5)

# 建矿脉
def buildKuang():
    keyborad('f1')
    rightClick(6)
    time.sleep(2)
    keyborad('b')
    keyborad('q')
    leftClick(7)
    time.sleep(0.2)
    leftClick(8)
    hotkey('ctrl', '6')

# 建加速
def buildJiasu():
    keyborad('f1')
    keyborad('b')
    keyborad('z')
    leftClick(9)
    time.sleep(0.5)
    leftClick(10)
    hotkey('ctrl', '7')

# 建个渡劫塔
def buildTown():
    keyborad('f1')
    keyborad('f')  # 跳
    leftClick(0)  # 中间位置建小塔
    keyborad('r')
    isBm = autoBmI.get()
    if isBm:
        keyborad('9')  # 自动拔苗
    keyE(4)  # 升级修炼速度
    keyborad('esc')
    isTimes = timesI.get()
    if not isTimes:
        buildGuanghuan()
    buildHero()
    if not isTimes:
        buildKuang()
    isJiaSu = jiaSuTI.get()
    if isJiaSu:
        buildJiasu()


def wakuangshengji():
    isFukuangDian = fuKuangDianI.get()
    if isFukuangDian:
        haveFukuang = findButton(fukuangPic, False)
        if haveFukuang:
            findButton(fukuangPic, True)
            mouseMoveClick(573, 492)


def shengjikeji():
    keyborad('f1')
    wakuangshengji()
    diff = int(entryN.get())
    if diff <= 25:
        keyborad('7')
        cut = diff - 20
        count = 6 - cut
        if count < 1:
            count = 1
        for i in range(0, count):
            keyborad('w')
            time.sleep(1)

def updateHeroSkill():
    keyborad('2')
    keyQ(1)
    run_log_print(message='升级英雄...')
    keyborad('f2')
    keyborad('d')  # 入口
    keyborad('q')
    keyborad('w')
    keyborad('e')
    keyborad('r')
    keyborad('a')
    keyborad('s')
    keyborad('esc')
    run_log_print(message='升级英雄结束')


def updateGuanghuan():
    keyborad('4')
    keyborad('c')
    leftClick(13)
    hotkey('ctrl', '4')
    # buff图标
    rightClick(14)
    # 如果是500w，直接升级光环
    keyQ(5)

# 升级人物上矿稿采掘(能力/速度)
def UpdatekuangGao(count):
    keyborad('f1')
    keyborad('r')
    for i in range(0, count):  # 采矿能力
        rightClick(11)
    for i in range(0, count):  # 采矿速度
        rightClick(12)

# 升级矿脉
def UpdateKuangMai(count):
    keyborad('6')
    keyQ(count)  # 矿升级

# 解析修炼数据
def jieXiXiuLian(index):
    dataSplit = data[index].split(',')
    if dataSplit[0].startswith('dj'):
        keyborad('esc')
        keyborad('f1')
        keyborad(f'{dataSplit[1]}')
        time.sleep(1)
    elif dataSplit[0].startswith("ukg"):
        UpdatekuangGao(int(dataSplit[1]))
    elif dataSplit[0].startswith("ukm"):
        UpdateKuangMai(int(dataSplit[1]))
    elif dataSplit[0].startswith("fs"):
        fenshenD()
    elif dataSplit[1] == "QE":
        keyborad('esc')
        keyborad('f1')
        keyQE(int(dataSplit[2]))
    else:
        keyborad('esc')
        keyborad('f1')
        keyQ(int(dataSplit[2]))
        time.sleep(float(dataSplit[3]))

# 人物修炼到250w
def xiulian():
    keyborad('f1')
    keyborad('esc')
    for i in range(xlBIndex + 1, xlEIndex):
        jieXiXiuLian(i)
    keyborad('6')
    keyborad('r')
    keyborad('r')

# 人物修炼
def xiulian1():
    keyborad('f1')
    keyborad('esc')
    for i in range(xlEIndex + 1, len(data)):
        jieXiXiuLian(i)

def updateDot():
    iswj = wji.get()
    isjj = jji.get()
    istd = tdi.get()
    issm = smi.get()
    ishm = hmi.get()
    issk = ski.get()
    iskw = kwi.get()
    isdd = ddi.get()
    iszy = zyi.get()
    iscundang = iswj or isjj or istd or issm or ishm or issk or iskw or isdd or iszy
    if iscundang:
        switchWar()
        keyborad('f1')
        keyborad('g')
        leftClick(18)  # 游戏存档
        # findButtonClick(cundangPic,True)
        run_log_print(f"开始点存档")
        time.sleep(0.5)
        # run_log_print(f'无尽 {iswj}，进阶 {isjj}，天道 {istd}，生命 {issm}，毁灭 {ishm}，时空 {issk}，枯萎 {iskw}')
        for i in range(0, 1):
            if iswj:
                leftClick(19)
                run_log_print(f"点击存档 无尽轮回")
                time.sleep(1)
            if isjj:
                leftClick(20)
                run_log_print(f"点击存档 进阶轮回")
                time.sleep(1)
            if istd:
                leftClick(21)
                run_log_print(f"点击存档 天道碎片")
                time.sleep(1)
            if issm:
                leftClick(22)
                run_log_print(f"点击存档 生命碎片")
                time.sleep(1)
            if ishm:
                leftClick(23)
                run_log_print(f"点击存档 毁灭碎片")
                time.sleep(1)
            if issk:
                leftClick(24)
                run_log_print(f"点击存档 时空碎片")
                time.sleep(1)
            if iskw:
                leftClick(25)
                run_log_print(f"点击存档 枯萎碎片")
                time.sleep(1)
            if isdd:
                leftClick(26)
                run_log_print(f"点击存档 大道碎片")
                time.sleep(1)
            if iszy:
                leftClick(27)
                run_log_print(f"点击存档 终焉碎片")
                time.sleep(1)
        keyborad('g')
    else:
        run_log_print(f"没有点击存档")

def gotokuang():
    keyborad('f1')
    # 小地图
    leftClick(15)  # 小地图矿位置
    rightClick(16)  # 右键矿位置
    keyborad('f')
    pyautogui.click()
    rightClick(17)  # 右键矿位置
    time.sleep(13)
    run_log_print(message='到达矿')


def upGuJuan_or_xianJi():
    isGuJuan = guJuanI.get()
    gujuancishu = int(entryGuJuan.get())
    isXianJi = xianJiI.get()
    xianJiCishu = int(entryXianJi.get())
    if isGuJuan or isXianJi:
        keyborad('esc')
        keyborad('f1')
        keyborad('r')
        if isGuJuan:
            for i in range(0, gujuancishu):
                rightClick(28)#右击古卷
        if isXianJi:
            for i in range(0, xianJiCishu):
                rightClick(29)  # 右键献祭
        keyborad('esc')

def building():
    ishunche = hunCheI.get()
    isTimes = timesI.get()
    if ishunche:
        run_log_print(message='开始混车')
        result = checkWnd('Warcraft III')
        if not result:
            findButtonClick(readyPic, True)  # 准备按钮
        findButtonClick(f1Pic, True)  # f1
        gotokuang()
        # time.sleep(3)
        wakuangshengji()
    else:
        clickStart()
        time.sleep(10)
        chooseDiff()
        run_log_print(message='选好难度了')
        buildTown()
        
        xiulian()
        if not isTimes:
            updateGuanghuan()
        run_log_print(message='建好小塔，准备去矿了')

        gotokuang()
        if not isTimes:
            fenshenD()
            shengjikeji()
        
        xiulian1()
        updateHeroSkill()
        upGuJuan_or_xianJi()
        keyborad('f1')
    updateDot()
    run_log_print(message='都修完了')

def switch_to_window(window_title):
    # 找到窗口的句柄
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            # 将窗口切换到前台
            win32gui.SetForegroundWindow(hwnd)
            run_log_print(message=f'已经切换到 {window_title}')
        except Exception as e:
            run_log_print(message=f'切换出错 {window_title}: {e}')
    else:
        run_log_print(message=f'{window_title} 没找到')

def checkWnd(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        run_log_print(message=f'找到 {window_title}')
        return True
    else:
        return False

def switchWar():
    result = checkWnd('Warcraft III')
    if result:
        switch_to_window('Warcraft III')
        time.sleep(1)
        return True
    else:
        run_log_print(message='没有找到Warcraft III')
        return False

def quitGame():
    result = switchWar()
    if result:
        findResult = findButton(defaultPic, True)  # 找到失败的返回按钮
        if not findResult:
            keyborad('f10')
            keyborad('e')
            keyborad('x')
            keyborad('x')
            time.sleep(1)
            run_log_print(message='退出游戏结束')

def start_countdown():
    run_log_print(message='开始倒计时')
    istimes = timesI.get()
    ishunche = hunCheI.get()
    isEveryCunDang = cunDangI.get()
    cunDangSecond = int(entrycunDang.get())
    cunDangCount = 1
    totalRunTime = 0

    if istimes:
        if ishunche:
            countdown_time = int(cTime[1])
        else:
            countdown_time = int(cTime[0])
    else:
        if ishunche:
            countdown_time = int(tTime[1])
        else:
            countdown_time = int(tTime[0])

    nowTime = datetime.now()
    # 要添加的秒数
    secondsAdd = countdown_time
    # 当前时间加上指定的秒数
    future_time = nowTime + timedelta(seconds=secondsAdd) 
    strShowTime = future_time.strftime('%Y-%m-%d %H:%M:%S')
    labelbackTime.config(text=strShowTime, state=tk.DISABLED)
    while future_time > nowTime:
        nowTime = datetime.now()
        time_difference = future_time - nowTime
        total_seconds = int(time_difference.total_seconds())
        timeLabel.config(text=f"结束时间：{total_seconds}", state=tk.DISABLED)
        totalRunTime += 1
        if isEveryCunDang and cunDangSecond * cunDangCount == totalRunTime:
            updateDot()
            cunDangCount += 1
        if countdown_time % 10 == 0:
            findResult = findButton(defaultPic, True)
            if findResult:
                break
        else:
            time.sleep(1)
    strShowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    run_log_print(f'{strShowTime} 倒计时结束，准备退出')

    quitGame()
    while True:
        result = checkWnd('Warcraft III')
        if result:
            quitGame()
        else:
            break
        time.sleep(1)
    run_log_print(f'{datetime.now()} 已经退出War3')

    timeLabel.config(text="剩余时间", state=tk.DISABLED)

def beginGame():
    isweihu = weiHuI.get()
    count = defaultTimes
    if isweihu:
        count = int(entryWeiHu.get())
    run_log_print(message='开始游戏了')
    notFindPlat = 5
    for i in range(0, count):
        result = checkWnd('KK官方对战平台')
        if result:
            findwait = findButton(atwait, True)
            if findwait:
                run_log_print(message=f'找到活动弹框')
            run_log_print(message=f'正在进行第{i + 1}次游戏')
            label3.config(text=f"正在循环：{i + 1}次", state=tk.DISABLED)
            building()
            start_countdown()
            time.sleep(2)
            run_log_print(message=f'进行下一把 {i + 2}')
        else:
            run_log_print(message='没有找到平台')
            openPlatCreateRoom()
            notFindPlat = notFindPlat - 1
            if notFindPlat == 0:
                print(f"not find plat")
                break
    closeWnd()
    print(f"python end")

def start_thread():
    thread = threading.Thread(target=beginGame)
    thread.daemon = True
    thread.start()

def eventReduce():
    count = int(entryN.get())
    if count > 0:
        count = count - 1
    default_text.set(count)

def eventAdd():
    count = int(entryN.get())
    if count < maxDiff:
        count = count + 1
    default_text.set(count)

def test():
    gujuancishu = int(entryGuJuan.get())
    print(gujuancishu)

def checkbutton_callback(checkvar, entry):
    if checkvar.get():
        entry.config(state=tk.NORMAL)
    else:
        entry.config(state=tk.DISABLED)

def checkbutton_callback1(checkvar, entry1, entry2):
    if not checkvar.get():
        entry1.config(state=tk.NORMAL)
        entry2.config(state=tk.NORMAL)
    else:
        entry1.config(state=tk.DISABLED)
        entry2.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("界面")
    root.geometry("500x480")
    grid_frame = tk.Frame(root)
    grid_frame.grid()
    row = 0
    timesI = tk.BooleanVar()
    c1 = tk.Checkbutton(grid_frame, text="次数", variable=timesI)
    c1.grid(row=row, column=0, sticky=W)

    hunCheI = tk.BooleanVar()
    hunChe = tk.Checkbutton(grid_frame, text="混车", variable=hunCheI)
    hunChe.grid(row=row, column=1, sticky=W)

    timeLabel = tk.Label(grid_frame, text="结束时间")
    timeLabel.grid(row=row, column=3, columnspan=2, sticky=W)

    row += 1
    label1 = tk.Label(grid_frame, text="难度")
    label1.grid(row=row, column=0, sticky=W)
    default_text = tk.StringVar()
    default_text.set(defaultDiff)
    entryN = tk.Entry(grid_frame, textvariable=default_text, width=5)  # 创建一个输入框
    entryN.grid(row=row, column=1, sticky=W)
    buttonReduce = tk.Button(grid_frame, text="-", command=eventReduce, width=5)
    buttonReduce.grid(row=1, column=2, sticky=W)
    buttonAdd = tk.Button(grid_frame, text="+", command=eventAdd, width=5)
    buttonAdd.grid(row=row, column=3, sticky=W)
    label3 = tk.Label(grid_frame, text="正在循环")
    label3.grid(row=row, column=4, columnspan=2, sticky=W)

    row += 1
    button = tk.Button(grid_frame, text="开始", command=start_thread)
    button.grid(row=row, column=0, sticky=W)
    button1 = tk.Button(grid_frame, text="鼠标坐标", command=mousePos)
    button1.grid(row=row, column=1,  sticky=W)
    button2 = tk.Button(grid_frame, text="测试", command=test)
    button2.grid(row=row, column=2, sticky=W)

    row += 1
    autoBmI = tk.BooleanVar()
    autoBm = tk.Checkbutton(grid_frame, text="自动拔苗", variable=autoBmI)
    autoBm.grid(row=row, column=0, columnspan=2, sticky=W)
    weiHuI = tk.BooleanVar()
    weiHu = tk.Checkbutton(grid_frame, text="维护", variable=weiHuI,
                           command=lambda: checkbutton_callback(weiHuI, entryWeiHu))
    weiHu.grid(row=row, column=2, sticky=W)
    weiHu_text = tk.StringVar()
    weiHu_text.set(weihuTimes)
    entryWeiHu = tk.Entry(grid_frame, textvariable=weiHu_text, width=5)  # 创建一个输入框
    entryWeiHu.grid(row=row, column=3, sticky=W)
    checkbutton_callback(weiHuI, entryWeiHu)
    jiaSuTI = tk.BooleanVar()
    jiaSuT = tk.Checkbutton(grid_frame, text="建加速塔", variable=jiaSuTI)
    jiaSuT.grid(row=row, column=4, columnspan=2, sticky=W)
    fuKuangDianI = tk.BooleanVar()
    fuKuangDian = tk.Checkbutton(grid_frame, text="富矿点击", variable=fuKuangDianI)
    fuKuangDian.grid(row=row, column=6, columnspan=2, sticky=W)

    row += 1
    guJuanI = tk.BooleanVar()
    guJuanB = tk.Checkbutton(grid_frame, text="古卷(次)", variable=guJuanI,
                           command=lambda: checkbutton_callback(guJuanI, entryGuJuan))
    guJuanB.grid(row=row, column=0, columnspan=2, sticky=W)
    guJuan_text = tk.StringVar()
    guJuan_text.set(guJuanTimes)
    entryGuJuan = tk.Entry(grid_frame, textvariable=guJuan_text, width=5)  # 创建一个输入框
    entryGuJuan.grid(row=row, column=2, sticky=W)
    checkbutton_callback(guJuanI, entryGuJuan)

    xianJiI = tk.BooleanVar()
    xiaJiB = tk.Checkbutton(grid_frame, text="献祭(次)", variable=xianJiI,
                             command=lambda: checkbutton_callback(xianJiI, entryXianJi))
    xiaJiB.grid(row=row, column=3, columnspan=2, sticky=W)
    xianJi_text = tk.StringVar()
    xianJi_text.set(xianJiTimes)
    entryXianJi = tk.Entry(grid_frame, textvariable=xianJi_text, width=5)  # 创建一个输入框
    entryXianJi.grid(row=row, column=5, sticky=W)
    checkbutton_callback(xianJiI, entryXianJi)

    row += 1
    cunDangI = tk.BooleanVar()
    cunDangB = tk.Checkbutton(grid_frame, text="存档间隔(秒)", variable=cunDangI,
                           command=lambda: checkbutton_callback(cunDangI, entrycunDang))
    cunDangB.grid(row=row, column=0, columnspan=2, sticky=W)
    cunDang_text = tk.StringVar()
    cunDang_text.set(cunDangTime)
    entrycunDang = tk.Entry(grid_frame, textvariable=cunDang_text, width=5)  # 创建一个输入框
    entrycunDang.grid(row=row, column=2, sticky=W)
    checkbutton_callback(cunDangI, entrycunDang)

    row += 1
    wji = tk.BooleanVar()
    wujing = tk.Checkbutton(grid_frame, text="无尽", variable=wji)
    wujing.grid(row=row, column=0, sticky=W)

    jji = tk.BooleanVar()
    jingJie = tk.Checkbutton(grid_frame, text="进阶", variable=jji)
    jingJie.grid(row=row, column=1, sticky=W)

    tdi = tk.BooleanVar()
    tianDao = tk.Checkbutton(grid_frame, text="天道", variable=tdi)
    tianDao.grid(row=row, column=2, sticky=W)

    smi = tk.BooleanVar()
    shengMing = tk.Checkbutton(grid_frame, text="生命", variable=smi)
    shengMing.grid(row=row, column=3, sticky=W)
    row += 1
    hmi = tk.BooleanVar()
    huiMie = tk.Checkbutton(grid_frame, text="毁灭", variable=hmi)
    huiMie.grid(row=row, column=0, sticky=W)

    ski = tk.BooleanVar()
    shiKong = tk.Checkbutton(grid_frame, text="时空", variable=ski)
    shiKong.grid(row=row, column=1, sticky=W)

    kwi = tk.BooleanVar()
    kuWei = tk.Checkbutton(grid_frame, text="枯萎", variable=kwi)
    kuWei.grid(row=row, column=2, sticky=W)

    ddi = tk.BooleanVar()
    daDao = tk.Checkbutton(grid_frame, text="大道", variable=ddi)
    daDao.grid(row=row, column=3, sticky=W)

    zyi = tk.BooleanVar()
    zhongYan = tk.Checkbutton(grid_frame, text="终焉", variable=zyi)
    zhongYan.grid(row=row, column=4, sticky=W)

    row = row + 1
    labelbackTime = tk.Label(grid_frame, text="退出时间")
    labelbackTime.grid(row=row, column=0, sticky=W)

    labelbackTime = tk.Label(grid_frame, text="")
    labelbackTime.grid(row=row, column=1, columnspan=2, sticky=W)

    row = row + 1
    log_frame = tk.Frame()  # 创建存放日志组件的容器
    log_frame.grid(padx=5, row=row, column=0, sticky=W)

    run_log = ScrolledText(log_frame, width=50, height=15)
    run_log.grid(padx=5, row=row, column=1, sticky=W)

    root.mainloop()
