# -*- coding: utf-8 -*-

import names

def main():
    test.log("Test Software Panel")

    startApplication("ui")
    test.vp("VP1")
    mouseClick(waitForObject(names.o_Sidebar), 129, 95, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP2")
    clickButton(waitForObject(names.software_QPushButton))
    test.vp("VP3")    
    
