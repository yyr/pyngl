# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hlu', [dirname(__file__)])
        except ImportError:
            import _hlu
            return _hlu
        if fp is not None:
            try:
                _mod = imp.load_module('_hlu', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _hlu = swig_import_helper()
    del swig_import_helper
else:
    import _hlu
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def new_intp():
  return _hlu.new_intp()
new_intp = _hlu.new_intp

def copy_intp(*args):
  return _hlu.copy_intp(*args)
copy_intp = _hlu.copy_intp

def delete_intp(*args):
  return _hlu.delete_intp(*args)
delete_intp = _hlu.delete_intp

def intp_assign(*args):
  return _hlu.intp_assign(*args)
intp_assign = _hlu.intp_assign

def intp_value(*args):
  return _hlu.intp_value(*args)
intp_value = _hlu.intp_value

def new_floatArray(*args):
  return _hlu.new_floatArray(*args)
new_floatArray = _hlu.new_floatArray

def delete_floatArray(*args):
  return _hlu.delete_floatArray(*args)
delete_floatArray = _hlu.delete_floatArray

def floatArray_getitem(*args):
  return _hlu.floatArray_getitem(*args)
floatArray_getitem = _hlu.floatArray_getitem

def floatArray_setitem(*args):
  return _hlu.floatArray_setitem(*args)
floatArray_setitem = _hlu.floatArray_setitem
NhlSETRL = _hlu.NhlSETRL
NhlGETRL = _hlu.NhlGETRL
NhlFATAL = _hlu.NhlFATAL
NhlWARNING = _hlu.NhlWARNING
NhlINFO = _hlu.NhlINFO
NhlNOERROR = _hlu.NhlNOERROR
NhlNOLINE = _hlu.NhlNOLINE
NhlLINEONLY = _hlu.NhlLINEONLY
NhlLABELONLY = _hlu.NhlLABELONLY
NhlLINEANDLABEL = _hlu.NhlLINEANDLABEL
NhlPOLYLINE = _hlu.NhlPOLYLINE
NhlPOLYMARKER = _hlu.NhlPOLYMARKER
NhlPOLYGON = _hlu.NhlPOLYGON

def c_cssgrid(*args):
  return _hlu.c_cssgrid(*args)
c_cssgrid = _hlu.c_cssgrid

def _NGGetNCARGEnv(*args):
  return _hlu._NGGetNCARGEnv(*args)
_NGGetNCARGEnv = _hlu._NGGetNCARGEnv

def NhlInitialize():
  return _hlu.NhlInitialize()
NhlInitialize = _hlu.NhlInitialize

def NhlClose():
  return _hlu.NhlClose()
NhlClose = _hlu.NhlClose

def NhlRLClear(*args):
  return _hlu.NhlRLClear(*args)
NhlRLClear = _hlu.NhlRLClear

def NhlSetValues(*args):
  return _hlu.NhlSetValues(*args)
NhlSetValues = _hlu.NhlSetValues

def NhlRLSetString(*args):
  return _hlu.NhlRLSetString(*args)
NhlRLSetString = _hlu.NhlRLSetString

def NhlRLSetFloat(*args):
  return _hlu.NhlRLSetFloat(*args)
NhlRLSetFloat = _hlu.NhlRLSetFloat

def NhlRLSetDouble(*args):
  return _hlu.NhlRLSetDouble(*args)
NhlRLSetDouble = _hlu.NhlRLSetDouble

def NhlRLSetInteger(*args):
  return _hlu.NhlRLSetInteger(*args)
NhlRLSetInteger = _hlu.NhlRLSetInteger

def NhlNDCPolyline(*args):
  return _hlu.NhlNDCPolyline(*args)
NhlNDCPolyline = _hlu.NhlNDCPolyline

def NhlNDCPolymarker(*args):
  return _hlu.NhlNDCPolymarker(*args)
NhlNDCPolymarker = _hlu.NhlNDCPolymarker

def NhlNDCPolygon(*args):
  return _hlu.NhlNDCPolygon(*args)
NhlNDCPolygon = _hlu.NhlNDCPolygon

def NhlDataPolyline(*args):
  return _hlu.NhlDataPolyline(*args)
NhlDataPolyline = _hlu.NhlDataPolyline

def NhlDataPolymarker(*args):
  return _hlu.NhlDataPolymarker(*args)
NhlDataPolymarker = _hlu.NhlDataPolymarker

def NhlDataPolygon(*args):
  return _hlu.NhlDataPolygon(*args)
NhlDataPolygon = _hlu.NhlDataPolygon

def NhlDraw(*args):
  return _hlu.NhlDraw(*args)
NhlDraw = _hlu.NhlDraw

def NhlFreeColor(*args):
  return _hlu.NhlFreeColor(*args)
NhlFreeColor = _hlu.NhlFreeColor

def NhlGetGksCi(*args):
  return _hlu.NhlGetGksCi(*args)
NhlGetGksCi = _hlu.NhlGetGksCi

def NhlGetWorkspaceObjectId():
  return _hlu.NhlGetWorkspaceObjectId()
NhlGetWorkspaceObjectId = _hlu.NhlGetWorkspaceObjectId

def NhlIsAllocatedColor(*args):
  return _hlu.NhlIsAllocatedColor(*args)
NhlIsAllocatedColor = _hlu.NhlIsAllocatedColor

def NhlIsApp(*args):
  return _hlu.NhlIsApp(*args)
NhlIsApp = _hlu.NhlIsApp

def NhlIsDataComm(*args):
  return _hlu.NhlIsDataComm(*args)
NhlIsDataComm = _hlu.NhlIsDataComm

def NhlIsDataItem(*args):
  return _hlu.NhlIsDataItem(*args)
NhlIsDataItem = _hlu.NhlIsDataItem

def NhlIsDataSpec(*args):
  return _hlu.NhlIsDataSpec(*args)
NhlIsDataSpec = _hlu.NhlIsDataSpec

def NhlRLIsSet(*args):
  return _hlu.NhlRLIsSet(*args)
NhlRLIsSet = _hlu.NhlRLIsSet

def NhlRLUnSet(*args):
  return _hlu.NhlRLUnSet(*args)
NhlRLUnSet = _hlu.NhlRLUnSet

def NhlIsTransform(*args):
  return _hlu.NhlIsTransform(*args)
NhlIsTransform = _hlu.NhlIsTransform

def NhlIsView(*args):
  return _hlu.NhlIsView(*args)
NhlIsView = _hlu.NhlIsView

def NhlIsWorkstation(*args):
  return _hlu.NhlIsWorkstation(*args)
NhlIsWorkstation = _hlu.NhlIsWorkstation

def NhlName(*args):
  return _hlu.NhlName(*args)
NhlName = _hlu.NhlName

def NhlNewColor(*args):
  return _hlu.NhlNewColor(*args)
NhlNewColor = _hlu.NhlNewColor

def NhlNewDashPattern(*args):
  return _hlu.NhlNewDashPattern(*args)
NhlNewDashPattern = _hlu.NhlNewDashPattern

def NhlNewMarker(*args):
  return _hlu.NhlNewMarker(*args)
NhlNewMarker = _hlu.NhlNewMarker

def NhlSetColor(*args):
  return _hlu.NhlSetColor(*args)
NhlSetColor = _hlu.NhlSetColor

def NhlUpdateData(*args):
  return _hlu.NhlUpdateData(*args)
NhlUpdateData = _hlu.NhlUpdateData

def NhlUpdateWorkstation(*args):
  return _hlu.NhlUpdateWorkstation(*args)
NhlUpdateWorkstation = _hlu.NhlUpdateWorkstation

def NhlOpen():
  return _hlu.NhlOpen()
NhlOpen = _hlu.NhlOpen

def NhlCreate(*args):
  return _hlu.NhlCreate(*args)
NhlCreate = _hlu.NhlCreate

def NhlRLCreate(*args):
  return _hlu.NhlRLCreate(*args)
NhlRLCreate = _hlu.NhlRLCreate

def NhlFrame(*args):
  return _hlu.NhlFrame(*args)
NhlFrame = _hlu.NhlFrame

def NhlDestroy(*args):
  return _hlu.NhlDestroy(*args)
NhlDestroy = _hlu.NhlDestroy

def NhlRLSetMDIntegerArray(*args):
  return _hlu.NhlRLSetMDIntegerArray(*args)
NhlRLSetMDIntegerArray = _hlu.NhlRLSetMDIntegerArray

def NhlRLSetMDDoubleArray(*args):
  return _hlu.NhlRLSetMDDoubleArray(*args)
NhlRLSetMDDoubleArray = _hlu.NhlRLSetMDDoubleArray

def NhlRLSetMDFloatArray(*args):
  return _hlu.NhlRLSetMDFloatArray(*args)
NhlRLSetMDFloatArray = _hlu.NhlRLSetMDFloatArray

def NhlRLSetFloatArray(*args):
  return _hlu.NhlRLSetFloatArray(*args)
NhlRLSetFloatArray = _hlu.NhlRLSetFloatArray

def NhlRLSetIntegerArray(*args):
  return _hlu.NhlRLSetIntegerArray(*args)
NhlRLSetIntegerArray = _hlu.NhlRLSetIntegerArray

def NhlRLSetStringArray(*args):
  return _hlu.NhlRLSetStringArray(*args)
NhlRLSetStringArray = _hlu.NhlRLSetStringArray

def NhlGetValues(*args):
  return _hlu.NhlGetValues(*args)
NhlGetValues = _hlu.NhlGetValues

def NhlGetFloat(*args):
  return _hlu.NhlGetFloat(*args)
NhlGetFloat = _hlu.NhlGetFloat

def NhlGetFloatArray(*args):
  return _hlu.NhlGetFloatArray(*args)
NhlGetFloatArray = _hlu.NhlGetFloatArray

def NhlGetInteger(*args):
  return _hlu.NhlGetInteger(*args)
NhlGetInteger = _hlu.NhlGetInteger

def NhlGetIntegerArray(*args):
  return _hlu.NhlGetIntegerArray(*args)
NhlGetIntegerArray = _hlu.NhlGetIntegerArray

def NhlGetDouble(*args):
  return _hlu.NhlGetDouble(*args)
NhlGetDouble = _hlu.NhlGetDouble

def NhlGetDoubleArray(*args):
  return _hlu.NhlGetDoubleArray(*args)
NhlGetDoubleArray = _hlu.NhlGetDoubleArray

def NhlAddOverlay(*args):
  return _hlu.NhlAddOverlay(*args)
NhlAddOverlay = _hlu.NhlAddOverlay

def NhlClearWorkstation(*args):
  return _hlu.NhlClearWorkstation(*args)
NhlClearWorkstation = _hlu.NhlClearWorkstation

def NhlRemoveAnnotation(*args):
  return _hlu.NhlRemoveAnnotation(*args)
NhlRemoveAnnotation = _hlu.NhlRemoveAnnotation

def NhlAddAnnotation(*args):
  return _hlu.NhlAddAnnotation(*args)
NhlAddAnnotation = _hlu.NhlAddAnnotation

def NhlAppGetDefaultParentId():
  return _hlu.NhlAppGetDefaultParentId()
NhlAppGetDefaultParentId = _hlu.NhlAppGetDefaultParentId

def NhlGetParentWorkstation(*args):
  return _hlu.NhlGetParentWorkstation(*args)
NhlGetParentWorkstation = _hlu.NhlGetParentWorkstation

def NhlClassName(*args):
  return _hlu.NhlClassName(*args)
NhlClassName = _hlu.NhlClassName

def NhlGetString(*args):
  return _hlu.NhlGetString(*args)
NhlGetString = _hlu.NhlGetString

def NhlAddData(*args):
  return _hlu.NhlAddData(*args)
NhlAddData = _hlu.NhlAddData

def NhlRemoveData(*args):
  return _hlu.NhlRemoveData(*args)
NhlRemoveData = _hlu.NhlRemoveData

def NhlRemoveOverlay(*args):
  return _hlu.NhlRemoveOverlay(*args)
NhlRemoveOverlay = _hlu.NhlRemoveOverlay

def NhlGetStringArray(*args):
  return _hlu.NhlGetStringArray(*args)
NhlGetStringArray = _hlu.NhlGetStringArray

def NhlRLDestroy(*args):
  return _hlu.NhlRLDestroy(*args)
NhlRLDestroy = _hlu.NhlRLDestroy

def NhlGetNamedColorIndex(*args):
  return _hlu.NhlGetNamedColorIndex(*args)
NhlGetNamedColorIndex = _hlu.NhlGetNamedColorIndex

def NhlChangeWorkstation(*args):
  return _hlu.NhlChangeWorkstation(*args)
NhlChangeWorkstation = _hlu.NhlChangeWorkstation

def NhlPNDCToData(*args):
  return _hlu.NhlPNDCToData(*args)
NhlPNDCToData = _hlu.NhlPNDCToData

def NhlPDataToNDC(*args):
  return _hlu.NhlPDataToNDC(*args)
NhlPDataToNDC = _hlu.NhlPDataToNDC

def NhlGetMDFloatArray(*args):
  return _hlu.NhlGetMDFloatArray(*args)
NhlGetMDFloatArray = _hlu.NhlGetMDFloatArray

def NhlGetMDDoubleArray(*args):
  return _hlu.NhlGetMDDoubleArray(*args)
NhlGetMDDoubleArray = _hlu.NhlGetMDDoubleArray

def NhlGetMDIntegerArray(*args):
  return _hlu.NhlGetMDIntegerArray(*args)
NhlGetMDIntegerArray = _hlu.NhlGetMDIntegerArray

def NhlPAppClass():
  return _hlu.NhlPAppClass()
NhlPAppClass = _hlu.NhlPAppClass

def NhlPNcgmWorkstationClass():
  return _hlu.NhlPNcgmWorkstationClass()
NhlPNcgmWorkstationClass = _hlu.NhlPNcgmWorkstationClass

def NhlPXWorkstationClass():
  return _hlu.NhlPXWorkstationClass()
NhlPXWorkstationClass = _hlu.NhlPXWorkstationClass

def NhlPPSWorkstationClass():
  return _hlu.NhlPPSWorkstationClass()
NhlPPSWorkstationClass = _hlu.NhlPPSWorkstationClass

def NhlPPDFWorkstationClass():
  return _hlu.NhlPPDFWorkstationClass()
NhlPPDFWorkstationClass = _hlu.NhlPPDFWorkstationClass

def NhlPLogLinPlotClass():
  return _hlu.NhlPLogLinPlotClass()
NhlPLogLinPlotClass = _hlu.NhlPLogLinPlotClass

def NhlPGraphicStyleClass():
  return _hlu.NhlPGraphicStyleClass()
NhlPGraphicStyleClass = _hlu.NhlPGraphicStyleClass

def NhlPScalarFieldClass():
  return _hlu.NhlPScalarFieldClass()
NhlPScalarFieldClass = _hlu.NhlPScalarFieldClass

def NhlPContourPlotClass():
  return _hlu.NhlPContourPlotClass()
NhlPContourPlotClass = _hlu.NhlPContourPlotClass

def NhlPtextItemClass():
  return _hlu.NhlPtextItemClass()
NhlPtextItemClass = _hlu.NhlPtextItemClass

def NhlPscalarFieldClass():
  return _hlu.NhlPscalarFieldClass()
NhlPscalarFieldClass = _hlu.NhlPscalarFieldClass

def NhlPmapPlotClass():
  return _hlu.NhlPmapPlotClass()
NhlPmapPlotClass = _hlu.NhlPmapPlotClass

def NhlPcoordArraysClass():
  return _hlu.NhlPcoordArraysClass()
NhlPcoordArraysClass = _hlu.NhlPcoordArraysClass

def NhlPxyPlotClass():
  return _hlu.NhlPxyPlotClass()
NhlPxyPlotClass = _hlu.NhlPxyPlotClass

def NhlPtickMarkClass():
  return _hlu.NhlPtickMarkClass()
NhlPtickMarkClass = _hlu.NhlPtickMarkClass

def NhlPtitleClass():
  return _hlu.NhlPtitleClass()
NhlPtitleClass = _hlu.NhlPtitleClass

def NhlPlabelBarClass():
  return _hlu.NhlPlabelBarClass()
NhlPlabelBarClass = _hlu.NhlPlabelBarClass

def NhlPlegendClass():
  return _hlu.NhlPlegendClass()
NhlPlegendClass = _hlu.NhlPlegendClass

def NhlPvectorFieldClass():
  return _hlu.NhlPvectorFieldClass()
NhlPvectorFieldClass = _hlu.NhlPvectorFieldClass

def NhlPvectorPlotClass():
  return _hlu.NhlPvectorPlotClass()
NhlPvectorPlotClass = _hlu.NhlPvectorPlotClass

def NhlPstreamlinePlotClass():
  return _hlu.NhlPstreamlinePlotClass()
NhlPstreamlinePlotClass = _hlu.NhlPstreamlinePlotClass

def NGGetNCARGEnv(*args):
  return _hlu.NGGetNCARGEnv(*args)
NGGetNCARGEnv = _hlu.NGGetNCARGEnv

def set_PCMP04(*args):
  return _hlu.set_PCMP04(*args)
set_PCMP04 = _hlu.set_PCMP04

def gendat(*args):
  return _hlu.gendat(*args)
gendat = _hlu.gendat

def gactivate_ws(*args):
  return _hlu.gactivate_ws(*args)
gactivate_ws = _hlu.gactivate_ws

def gdeactivate_ws(*args):
  return _hlu.gdeactivate_ws(*args)
gdeactivate_ws = _hlu.gdeactivate_ws

def bndary():
  return _hlu.bndary()
bndary = _hlu.bndary

def c_plotif(*args):
  return _hlu.c_plotif(*args)
c_plotif = _hlu.c_plotif

def c_cpseti(*args):
  return _hlu.c_cpseti(*args)
c_cpseti = _hlu.c_cpseti

def c_cpsetr(*args):
  return _hlu.c_cpsetr(*args)
c_cpsetr = _hlu.c_cpsetr

def c_pcseti(*args):
  return _hlu.c_pcseti(*args)
c_pcseti = _hlu.c_pcseti

def c_pcsetr(*args):
  return _hlu.c_pcsetr(*args)
c_pcsetr = _hlu.c_pcsetr

def c_set(*args):
  return _hlu.c_set(*args)
c_set = _hlu.c_set

def c_cprect(*args):
  return _hlu.c_cprect(*args)
c_cprect = _hlu.c_cprect

def c_cpcldr(*args):
  return _hlu.c_cpcldr(*args)
c_cpcldr = _hlu.c_cpcldr

def c_plchhq(*args):
  return _hlu.c_plchhq(*args)
c_plchhq = _hlu.c_plchhq

def open_wks_wrap(*args):
  return _hlu.open_wks_wrap(*args)
open_wks_wrap = _hlu.open_wks_wrap

def labelbar_ndc_wrap(*args):
  return _hlu.labelbar_ndc_wrap(*args)
labelbar_ndc_wrap = _hlu.labelbar_ndc_wrap

def legend_ndc_wrap(*args):
  return _hlu.legend_ndc_wrap(*args)
legend_ndc_wrap = _hlu.legend_ndc_wrap

def blank_plot_wrap(*args):
  return _hlu.blank_plot_wrap(*args)
blank_plot_wrap = _hlu.blank_plot_wrap

def contour_wrap(*args):
  return _hlu.contour_wrap(*args)
contour_wrap = _hlu.contour_wrap

def map_wrap(*args):
  return _hlu.map_wrap(*args)
map_wrap = _hlu.map_wrap

def contour_map_wrap(*args):
  return _hlu.contour_map_wrap(*args)
contour_map_wrap = _hlu.contour_map_wrap

def xy_wrap(*args):
  return _hlu.xy_wrap(*args)
xy_wrap = _hlu.xy_wrap

def y_wrap(*args):
  return _hlu.y_wrap(*args)
y_wrap = _hlu.y_wrap

def vector_wrap(*args):
  return _hlu.vector_wrap(*args)
vector_wrap = _hlu.vector_wrap

def vector_map_wrap(*args):
  return _hlu.vector_map_wrap(*args)
vector_map_wrap = _hlu.vector_map_wrap

def vector_scalar_wrap(*args):
  return _hlu.vector_scalar_wrap(*args)
vector_scalar_wrap = _hlu.vector_scalar_wrap

def vector_scalar_map_wrap(*args):
  return _hlu.vector_scalar_map_wrap(*args)
vector_scalar_map_wrap = _hlu.vector_scalar_map_wrap

def streamline_wrap(*args):
  return _hlu.streamline_wrap(*args)
streamline_wrap = _hlu.streamline_wrap

def streamline_map_wrap(*args):
  return _hlu.streamline_map_wrap(*args)
streamline_map_wrap = _hlu.streamline_map_wrap

def streamline_scalar_wrap(*args):
  return _hlu.streamline_scalar_wrap(*args)
streamline_scalar_wrap = _hlu.streamline_scalar_wrap

def streamline_scalar_map_wrap(*args):
  return _hlu.streamline_scalar_map_wrap(*args)
streamline_scalar_map_wrap = _hlu.streamline_scalar_map_wrap

def text_ndc_wrap(*args):
  return _hlu.text_ndc_wrap(*args)
text_ndc_wrap = _hlu.text_ndc_wrap

def text_wrap(*args):
  return _hlu.text_wrap(*args)
text_wrap = _hlu.text_wrap

def add_text_wrap(*args):
  return _hlu.add_text_wrap(*args)
add_text_wrap = _hlu.add_text_wrap

def maximize_plots(*args):
  return _hlu.maximize_plots(*args)
maximize_plots = _hlu.maximize_plots

def poly_wrap(*args):
  return _hlu.poly_wrap(*args)
poly_wrap = _hlu.poly_wrap

def add_poly_wrap(*args):
  return _hlu.add_poly_wrap(*args)
add_poly_wrap = _hlu.add_poly_wrap

def panel_wrap(*args):
  return _hlu.panel_wrap(*args)
panel_wrap = _hlu.panel_wrap

def mapgci(*args):
  return _hlu.mapgci(*args)
mapgci = _hlu.mapgci

def dcapethermo(*args):
  return _hlu.dcapethermo(*args)
dcapethermo = _hlu.dcapethermo

def draw_colormap_wrap(*args):
  return _hlu.draw_colormap_wrap(*args)
draw_colormap_wrap = _hlu.draw_colormap_wrap

def natgridc(*args):
  return _hlu.natgridc(*args)
natgridc = _hlu.natgridc

def ftcurvc(*args):
  return _hlu.ftcurvc(*args)
ftcurvc = _hlu.ftcurvc

def ftcurvpc(*args):
  return _hlu.ftcurvpc(*args)
ftcurvpc = _hlu.ftcurvpc

def ftcurvpic(*args):
  return _hlu.ftcurvpic(*args)
ftcurvpic = _hlu.ftcurvpic

def c_rgbhls(*args):
  return _hlu.c_rgbhls(*args)
c_rgbhls = _hlu.c_rgbhls

def c_hlsrgb(*args):
  return _hlu.c_hlsrgb(*args)
c_hlsrgb = _hlu.c_hlsrgb

def c_rgbhsv(*args):
  return _hlu.c_rgbhsv(*args)
c_rgbhsv = _hlu.c_rgbhsv

def c_hsvrgb(*args):
  return _hlu.c_hsvrgb(*args)
c_hsvrgb = _hlu.c_hsvrgb

def c_rgbyiq(*args):
  return _hlu.c_rgbyiq(*args)
c_rgbyiq = _hlu.c_rgbyiq

def c_yiqrgb(*args):
  return _hlu.c_yiqrgb(*args)
c_yiqrgb = _hlu.c_yiqrgb

def getbb(*args):
  return _hlu.getbb(*args)
getbb = _hlu.getbb

def c_wmbarbp(*args):
  return _hlu.c_wmbarbp(*args)
c_wmbarbp = _hlu.c_wmbarbp

def c_wmsetip(*args):
  return _hlu.c_wmsetip(*args)
c_wmsetip = _hlu.c_wmsetip

def c_wmsetrp(*args):
  return _hlu.c_wmsetrp(*args)
c_wmsetrp = _hlu.c_wmsetrp

def c_wmsetcp(*args):
  return _hlu.c_wmsetcp(*args)
c_wmsetcp = _hlu.c_wmsetcp

def c_wmstnmp(*args):
  return _hlu.c_wmstnmp(*args)
c_wmstnmp = _hlu.c_wmstnmp

def c_wmgetip(*args):
  return _hlu.c_wmgetip(*args)
c_wmgetip = _hlu.c_wmgetip

def c_wmgetrp(*args):
  return _hlu.c_wmgetrp(*args)
c_wmgetrp = _hlu.c_wmgetrp

def c_wmgetcp(*args):
  return _hlu.c_wmgetcp(*args)
c_wmgetcp = _hlu.c_wmgetcp

def c_nnseti(*args):
  return _hlu.c_nnseti(*args)
c_nnseti = _hlu.c_nnseti

def c_nnsetrd(*args):
  return _hlu.c_nnsetrd(*args)
c_nnsetrd = _hlu.c_nnsetrd

def c_nnsetc(*args):
  return _hlu.c_nnsetc(*args)
c_nnsetc = _hlu.c_nnsetc

def c_nngeti(*args):
  return _hlu.c_nngeti(*args)
c_nngeti = _hlu.c_nngeti

def c_nngetrd(*args):
  return _hlu.c_nngetrd(*args)
c_nngetrd = _hlu.c_nngetrd

def c_nngetcp(*args):
  return _hlu.c_nngetcp(*args)
c_nngetcp = _hlu.c_nngetcp

def c_dgcdist(*args):
  return _hlu.c_dgcdist(*args)
c_dgcdist = _hlu.c_dgcdist

def c_dcapethermo(*args):
  return _hlu.c_dcapethermo(*args)
c_dcapethermo = _hlu.c_dcapethermo

def c_dptlclskewt(*args):
  return _hlu.c_dptlclskewt(*args)
c_dptlclskewt = _hlu.c_dptlclskewt

def c_dtmrskewt(*args):
  return _hlu.c_dtmrskewt(*args)
c_dtmrskewt = _hlu.c_dtmrskewt

def c_dtdaskewt(*args):
  return _hlu.c_dtdaskewt(*args)
c_dtdaskewt = _hlu.c_dtdaskewt

def c_dsatlftskewt(*args):
  return _hlu.c_dsatlftskewt(*args)
c_dsatlftskewt = _hlu.c_dsatlftskewt

def c_dshowalskewt(*args):
  return _hlu.c_dshowalskewt(*args)
c_dshowalskewt = _hlu.c_dshowalskewt

def c_dpwskewt(*args):
  return _hlu.c_dpwskewt(*args)
c_dpwskewt = _hlu.c_dpwskewt

def pvoid():
  return _hlu.pvoid()
pvoid = _hlu.pvoid

def set_nglRes_i(*args):
  return _hlu.set_nglRes_i(*args)
set_nglRes_i = _hlu.set_nglRes_i

def get_nglRes_i(*args):
  return _hlu.get_nglRes_i(*args)
get_nglRes_i = _hlu.get_nglRes_i

def set_nglRes_f(*args):
  return _hlu.set_nglRes_f(*args)
set_nglRes_f = _hlu.set_nglRes_f

def get_nglRes_f(*args):
  return _hlu.get_nglRes_f(*args)
get_nglRes_f = _hlu.get_nglRes_f

def set_nglRes_c(*args):
  return _hlu.set_nglRes_c(*args)
set_nglRes_c = _hlu.set_nglRes_c

def get_nglRes_c(*args):
  return _hlu.get_nglRes_c(*args)
get_nglRes_c = _hlu.get_nglRes_c

def set_nglRes_s(*args):
  return _hlu.set_nglRes_s(*args)
set_nglRes_s = _hlu.set_nglRes_s

def get_nglRes_s(*args):
  return _hlu.get_nglRes_s(*args)
get_nglRes_s = _hlu.get_nglRes_s

def NglGaus_p(*args):
  return _hlu.NglGaus_p(*args)
NglGaus_p = _hlu.NglGaus_p
# This file is compatible with both classic and new-style classes.


