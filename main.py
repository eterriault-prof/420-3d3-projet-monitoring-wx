import wx
from models.metrics import MetriquesSysteme
from views.dashboard import Dashboard


def main():
    metriques = MetriquesSysteme()
    app = wx.App()
    fenetre = Dashboard(metriques)
    fenetre.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
