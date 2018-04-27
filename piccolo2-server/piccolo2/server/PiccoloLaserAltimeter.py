from PiccoloInstrument import PiccoloAuxInstrument,PiccoloAuxHandlerThread
import time
import logging
import serial
import glob

class LightWareSF11Altimeter(PiccoloAuxHandlerThread):
    """Interface for Lightware SF11 Laser Altimeter 
    https://www.mikrocontroller.com/images/SF11ManualRev4.pdf
    Polling mode: altimeter sends readings constantly
    On demand mode: send 'd' to altimeter to retrieve reading
    """
    def __init__(self,port=None,baudrate=115200,timeout=.2,mode='polling'):

        self._baud = baudrate
        self._timeout = timeout
        self._latestAltitude = 'N/A'
        self.mode = mode

        if port is None:
            self.autoDetectPort()
        else:
            try:
                self._ser = serial.Serial(port,baudrate,timeout=timeout)
            except:
                #if the serial port can't be opened,set status to disconnected
                self._ser = None

        PiccoloAuxHandlerThread.__init__(self)
        if not self.connected:
            logging.warn("No SF11 Laser Altimeter is Connected")
   
    
    def autoDetectPort(self):
        possible_ports = glob.glob('/dev/ttyUSB*')+['/dev/serial0']
        for port in possible_ports:
            self._ser = serial.Serial(port,self._baud,timeout=self._timeout)
            logging.info("Testing altimeter connection on {}".format(port))
            if self._testConnection():
                #we've found a working port, keep it
                logging.info("Connection succeeded")
                break
            else:
                logging.info("Connection failed")


    def _readAltitudeFromSerial(self):
            try:
                record = self._ser.readline()
                self._latestAltitude = record.strip().split()[0]
                #make sure the latestAltitude is castable to float
                _ = float(self._latestAltitude)
            except Exception:
                self._latestAltitude = 'N/A'

    def run(self):
        while(True):
            if self.mode=='polling' and self.connected:
                #in polling mode, buffer must be constantly flushed
                self._readAltitudeFromSerial()

            else:
                time.sleep(.1)
        
    def _testConnection(self):
        #if the serial port failed to initialize, we're not connected
        isConnected = False
        if self._ser is not None:
            for i in range(3):
                self._ser.write(b'd')
                self._readAltitudeFromSerial()
                if self._latestAltitude != 'N/A':
                    isConnected = True
                    break
        return isConnected


    def requestInstrumentMeasurement(self):
        if self.connected and self.mode == 'ondemand':
            self._ser.write(b'd')
            self._readAltitudeFromSerial()

    def retrieveInstrumentResponse(self):
        if self.connected:
            return self._latestAltitude
        else:
            return "No connection to LightWareSF11Altimeter found" 

#"/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_DQ00A0BA-if00-port0"
#"usb-FTDI_FT230X_Basic_UART_DQ00A2QI-if00-port0"
if __name__ == '__main__':    
    pa = PiccoloAuxInstrument("alt",LightWareSF11Altimeter(baudrate=115200))
    while True:
        print(pa.getRecord())
        time.sleep(.1)
