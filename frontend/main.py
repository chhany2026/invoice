#!/usr/bin/env python3
"""
Warranty Product Management System - Main Entry Point
Global warranty recording system accessible from QR codes or serial numbers
"""

import sys
from PyQt6.QtWidgets import QApplication
from main_window import WarrantyProductApp


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    window = WarrantyProductApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
