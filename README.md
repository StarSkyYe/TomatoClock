# TomatoClock
simple tomato clock
利用PyQt5实现一个简易的番茄时钟，用于个人使用。
基本功能：设置工作时长和休息时长，进行计时，在进入休息状态时，可选择是否播放音乐。
工程结构说明：
1 media用于存放mp3音频文件
2 QtApp是一个Qt工程，用于可视化设计界面，使用的是Qt Creator，目的是为了得到 Widget.ui 的ui文件
3 uic.bat是批处理命令，实现编译Widget.ui和图标资源，得到ui_Widget.py的ui界面实现相关python代码和res_rc.py的图标资源的python文件
4 clockWidget.py是实现界面功能逻辑
5 AppMain.py是作为程序的启动入口
