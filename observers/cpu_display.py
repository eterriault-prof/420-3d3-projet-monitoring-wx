import wx
from observers.observer import Observateur


class AffichageCPU(Observateur):

    def __init__(self, parent: wx.Panel, sizer: wx.BoxSizer):
        box = wx.StaticBox(parent, label="CPU")
        box_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        self._label = wx.StaticText(box, label="0%")
        font = self._label.GetFont()
        font.SetPointSize(24)
        font.MakeBold()
        self._label.SetFont(font)

        self._barre = wx.Gauge(box, range=100, size=(300, 20))

        box_sizer.Add(self._label, 0, wx.ALL | wx.CENTER, 5)
        box_sizer.Add(self._barre, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(box_sizer, 0, wx.ALL | wx.EXPAND, 10)

    def actualiser(self, sujet) -> None:
        valeur = sujet.get_donnees()['cpu']
        self._label.SetLabel(f"{valeur:.1f}%")
        self._barre.SetValue(int(valeur))
        self._label.SetForegroundColour(self._couleur(valeur))
        self._label.Refresh()

    def _couleur(self, valeur: float) -> wx.Colour:
        if valeur < 50:
            return wx.GREEN
        elif valeur < 80:
            return wx.Colour(255, 165, 0)
        return wx.RED
