# -*- coding: utf-8 -*-

import names

def main():
    test.log("This Test is designed to fail")
    startApplication("ui")
    mouseClick(waitForObject(names.o_Sidebar), 184, 118, Qt.NoModifier, Qt.LeftButton)    
    test.vp("VP1")