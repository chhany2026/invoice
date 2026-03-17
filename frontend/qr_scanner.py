import cv2
import threading
from pyzbar.pyzbar import decode
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PIL import Image
import numpy as np


class QRScannerThread(QThread):
    """Thread for continuous QR code scanning from camera"""
    
    qr_detected = pyqtSignal(str)  # Emits scanned QR code data
    frame_updated = pyqtSignal(QPixmap)  # Emits updated frame
    error_occurred = pyqtSignal(str)  # Emits error message
    
    def __init__(self, camera_id: int = 0):
        super().__init__()
        self.camera_id = camera_id
        self.is_running = True
        self.cap = None
    
    def run(self):
        """Main scanning loop"""
        try:
            self.cap = cv2.VideoCapture(self.camera_id)
            
            if not self.cap.isOpened():
                self.error_occurred.emit('Unable to open camera')
                return
            
            while self.is_running:
                ret, frame = self.cap.read()
                
                if not ret:
                    self.error_occurred.emit('Failed to read frame from camera')
                    break
                
                # Detect QR codes
                decoded_objects = decode(frame)
                
                for obj in decoded_objects:
                    qr_data = obj.data.decode('utf-8')
                    self.qr_detected.emit(qr_data)
                    
                    # Draw rectangle around QR code
                    points = obj.polygon
                    if len(points) > 0:
                        pts = np.array([(p.x, p.y) for p in points], dtype=np.int32)
                        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
                
                # Convert frame to QPixmap for display
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(qt_image)
                self.frame_updated.emit(pixmap)
                
                # Small delay to prevent CPU overload
                cv2.waitKey(1)
        
        except Exception as e:
            self.error_occurred.emit(f'Camera error: {str(e)}')
        
        finally:
            if self.cap:
                self.cap.release()
    
    def stop(self):
        """Stop the scanning thread"""
        self.is_running = False
        self.wait()


class QRScannerDialog(QDialog):
    """Dialog window for scanning QR codes"""
    
    qr_scanned = pyqtSignal(str)  # Emits the scanned QR data
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QR Code Scanner')
        self.setGeometry(100, 100, 640, 580)
        self.scanner_thread = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Camera feed label
        self.camera_label = QLabel()
        self.camera_label.setMinimumSize(640, 480)
        self.camera_label.setStyleSheet('border: 1px solid black;')
        layout.addWidget(self.camera_label)
        
        # Scanned data label
        self.data_label = QLabel('Waiting for QR code...')
        layout.addWidget(self.data_label)
        
        # Buttons
        button_layout = QVBoxLayout()
        
        self.scan_button = QPushButton('Start Scanning')
        self.scan_button.clicked.connect(self.start_scanning)
        button_layout.addWidget(self.scan_button)
        
        self.use_button = QPushButton('Use Scanned Code')
        self.use_button.clicked.connect(self.use_scanned_code)
        self.use_button.setEnabled(False)
        button_layout.addWidget(self.use_button)
        
        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close_scanner)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
        self.scanned_data = None
    
    def start_scanning(self):
        """Start the QR code scanner"""
        if self.scanner_thread and self.scanner_thread.isRunning():
            return
        
        self.scanner_thread = QRScannerThread()
        self.scanner_thread.qr_detected.connect(self.on_qr_detected)
        self.scanner_thread.frame_updated.connect(self.on_frame_updated)
        self.scanner_thread.error_occurred.connect(self.on_error)
        self.scanner_thread.start()
        
        self.scan_button.setEnabled(False)
    
    def on_qr_detected(self, qr_data: str):
        """Handle detected QR code"""
        self.scanned_data = qr_data
        self.data_label.setText(f'Scanned: {qr_data}')
        self.use_button.setEnabled(True)
    
    def on_frame_updated(self, pixmap: QPixmap):
        """Update camera feed display"""
        scaled_pixmap = pixmap.scaledToWidth(640, Qt.TransformationMode.SmoothTransformation)
        self.camera_label.setPixmap(scaled_pixmap)
    
    def on_error(self, error_msg: str):
        """Handle scanner errors"""
        self.data_label.setText(f'Error: {error_msg}')
        self.scan_button.setEnabled(True)
    
    def use_scanned_code(self):
        """Use the scanned QR code and close dialog"""
        if self.scanned_data:
            self.qr_scanned.emit(self.scanned_data)
            self.close_scanner()
    
    def close_scanner(self):
        """Stop scanner and close dialog"""
        if self.scanner_thread and self.scanner_thread.isRunning():
            self.scanner_thread.stop()
        self.accept()
