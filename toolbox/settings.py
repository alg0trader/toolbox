
import os.path
from .toolbox import get_path
from ConfigParser import RawConfigParser


class BaseSettings:
    """
    Class for core settings functionality.
    """
    def __init__(self):
        self.saveData = None
        self.loadData = None
        self.settingsFile = get_path() + r'\toolbox.ini'
        self.config = RawConfigParser()
    
    def Exists(self):
        if os.path.isfile(self.settingsFile): return True
        else: return False
    
    def SetValue(self, section, key, value):
        try:
            self.config.set(section, str(key), value)
        except Exception as e:
            self.config.add_section(section)
            self.config.set(section, str(key), value)
        
        self.Write()

    def Write(self):
        with open(self.settingsFile, 'w+') as cfgFile:
            self.config.write(cfgFile)
    
    def Read(self):
        if self.Exists(): self.config.read(self.settingsFile)
        else: raise ValueError("File does not exist")
    
    def GetValue(self, section, key):
        return self.config.get(section, str(key))


class CurveSettings(BaseSettings):
    """
    Class for curve-specific settings.
    """
    _RIGHT = 0
    _TOP_RIGHT = 1
    _TOP = 2
    _TOP_LEFT = 3
    _LEFT = 4
    _BOTTOM_LEFT = 5
    _BOTTOM = 6
    _BOTTOM_RIGHT = 7

    _CURVE_SECTION = 'curve_tab'
    _CURVE_TYPE_CFG = {'Key':'0', 'Value':{'Circular':'0', 'Hermite':'1'}}
    _PAD_VECTOR_CFG = {'Key':'1', 'Value':{'Auto':'0', 'Manual':'1'}}
    _ARC_RADIUS = {'Key':'2'}
    _ARC_UNIT_CFG = {'Key':'3', 'Value':{'mm':'0', 'in':'1', 'mil':'2'}}
    _MAX_ARC_CHECK_CFG = {'Key':'4', 'Value':'0'}
    _FROM_PAD_CFG = {'Key':'5', 'Value':_BOTTOM}
    _TO_PAD_CFG = {'Key':'6', 'Value':_BOTTOM}


    def __init__(self):
        BaseSettings.__init__(self)

    def Defaults(self):
        self.curveType = self._CURVE_TYPE_CFG['Value']['Circular']
        self.padVectorCfg = self._PAD_VECTOR_CFG['Value']['Auto']
        self.arcRadius = '0'
        self.arcRadiusUnit = self._ARC_UNIT_CFG['Value']['mm']
        self.maxArcCheck = '1'
        self.fromPad = self._FROM_PAD_CFG['Value']
        self.toPad = self._TO_PAD_CFG['Value']
        
        self.Save()
    
    def Save(self):
        self.SetValue(self._CURVE_SECTION, self._CURVE_TYPE_CFG['Key'], self.curveType)
        self.SetValue(self._CURVE_SECTION, self._PAD_VECTOR_CFG['Key'], self.padVectorCfg)
        self.SetValue(self._CURVE_SECTION, self._ARC_RADIUS['Key'], self.arcRadius)
        self.SetValue(self._CURVE_SECTION, self._ARC_UNIT_CFG['Key'], self.arcRadiusUnit)
        self.SetValue(self._CURVE_SECTION, self._MAX_ARC_CHECK_CFG['Key'], self.maxArcCheck)
        self.SetValue(self._CURVE_SECTION, self._FROM_PAD_CFG['Key'], self.fromPad)
        self.SetValue(self._CURVE_SECTION, self._TO_PAD_CFG['Key'], self.toPad)
        self.Write()
    
    def Load(self):
        try:
            self.Read()

            self.curveType = self.GetValue(self._CURVE_SECTION, self._CURVE_TYPE_CFG['Key'])
            self.padVectorCfg = self.GetValue(self._CURVE_SECTION, self._PAD_VECTOR_CFG['Key'])
            self.arcRadius = self.GetValue(self._CURVE_SECTION, self._ARC_RADIUS['Key'])
            self.arcRadiusUnit = self.GetValue(self._CURVE_SECTION, self._ARC_UNIT_CFG['Key'])
            self.maxArcCheck = self.GetValue(self._CURVE_SECTION, self._MAX_ARC_CHECK_CFG['Key'])
            self.fromPad = self.GetValue(self._CURVE_SECTION, self._FROM_PAD_CFG['Key'])
            self.toPad = self.GetValue(self._CURVE_SECTION, self._TO_PAD_CFG['Key'])
        except:
            self.Defaults()
            self.Write()
            self.Load()


class ChamferSettings(BaseSettings):
    """
    Class for chamfer-specific settings.
    """
    _CHAMFER_SECTION = 'chamfer_tab'
    _CHAMFER_LINE_WIDTH = {'Key':'0'}
    _CHAMFER_LINE_UNIT = {'Key':'1', 'Value':{'mm':'0', 'mil':'1', 'in':'2'}}
    _CHAMFER_BOARD_HEIGHT = {'Key':'2'}
    _CHAMFER_HEIGHT_UNIT = {'Key':'3', 'Value':{'mm':'0', 'mil':'1', 'in':'2'}}
    _CHAMFER_ANGLE = {'Key':'4'}
    _CHAMFER_ANGLE_UNIT = {'Key':'5', 'Value':{'deg':'0', 'rad':1}}
    _CHAMFER_AUTOROUTE = {'Key':'6'}

    def __init__(self):
        BaseSettings.__init__(self)
    
    def Defaults(self):
        self.lineWidth = '0.5334'     # 21 mils by default
        self.lineUnit = self._CHAMFER_LINE_UNIT['Value']['mm']
        self.boardHeight = '0.254'    # 10 mils by default
        self.heightUnit = self._CHAMFER_HEIGHT_UNIT['Value']['mm']
        self.chamferAngle = '90'      # 90 degrees by default
        self.angleUnit = self._CHAMFER_ANGLE_UNIT['Value']['deg']
        self.chamferAutoroute = True

        self.Save()
    
    def Save(self):
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_LINE_WIDTH['Key'], self.lineWidth)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_LINE_UNIT['Key'], self.lineUnit)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_BOARD_HEIGHT['Key'], self.boardHeight)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_HEIGHT_UNIT['Key'], self.heightUnit)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_ANGLE['Key'], self.chamferAngle)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_ANGLE_UNIT['Key'], self.angleUnit)
        self.SetValue(self._CHAMFER_SECTION, self._CHAMFER_AUTOROUTE['Key'], self.chamferAutoroute)
        self.Write()
    
    def Load(self):
        try:
            self.Read()

            self.lineWidth = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_LINE_WIDTH['Key'])
            self.lineUnit = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_LINE_UNIT['Key'])
            self.boardHeight = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_BOARD_HEIGHT['Key'])
            self.heightUnit = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_HEIGHT_UNIT['Key'])
            self.chamferAngle = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_ANGLE['Key'])
            self.angleUnit = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_ANGLE_UNIT['Key'])
            self.chamferAutoroute = self.GetValue(self._CHAMFER_SECTION, self._CHAMFER_AUTOROUTE['Key'])
        
        except:
            self.Defaults()
            self.Write()
            self.Load()