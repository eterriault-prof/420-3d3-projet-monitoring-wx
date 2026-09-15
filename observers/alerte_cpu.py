import wx
from observers.observer import Observateur


class AlerteCPU(Observateur):

    def __init__(self, parent: wx.Panel, sizer: wx.BoxSizer, seuil: float = 80.0):
        self._seuil = seuil
        self._label = wx.StaticText(parent, label="")
        font = self._label.GetFont()
        font.SetPointSize(14)
        font.MakeBold()
        self._label.SetFont(font)
        self._label.SetForegroundColour(wx.RED)
        sizer.Add(self._label, 0, wx.ALL | wx.CENTER, 5)

    def actualiser(self, sujet) -> None:
        cpu = sujet.get_donnees()['cpu']
        if cpu > self._seuil:
            self._label.SetLabel(f"⚠️ CPU critique : {cpu:.1f}%")
        else:
            self._label.SetLabel("")
        self._label.Refresh()
