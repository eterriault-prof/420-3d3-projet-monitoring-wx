import wx
from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
from observers.logger import LoggerFichier
from observers.alerte_cpu import AlerteCPU


class Dashboard(wx.Frame):

    INTERVALLE_MS = 2000

    def __init__(self, metriques: MetriquesSysteme):
        super().__init__(None, title="Monitoring système")
        self._metriques = metriques

        self._panel = wx.Panel(self)
        self._sizer = wx.BoxSizer(wx.VERTICAL)

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_bouton_log()

        self._panel.SetSizer(self._sizer)
        self.Fit()
        self._rafraichir()

    def _creer_observateurs(self) -> None:
        self._alerte = AlerteCPU(self._panel, self._sizer, seuil=80.0)
        self._cpu_display = AffichageCPU(self._panel, self._sizer)
        self._ram_display = AffichageRAM(self._panel, self._sizer)
        self._disk_display = AffichageDisque(self._panel, self._sizer)
        self._logger = LoggerFichier("monitoring.log")

    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self._alerte)
        self._metriques.abonner(self._cpu_display)
        self._metriques.abonner(self._ram_display)
        self._metriques.abonner(self._disk_display)
        self._metriques.abonner(self._logger)

    def _creer_bouton_log(self) -> None:
        self._btn_log = wx.Button(self._panel, label="Désactiver le log")
        self._btn_log.Bind(wx.EVT_BUTTON, lambda e: self._toggle_log())
        self._sizer.Add(self._btn_log, 0, wx.ALL | wx.CENTER, 10)

    def _toggle_log(self) -> None:
        if self._metriques.est_abonne(self._logger):
            self._metriques.desabonner(self._logger)
            self._btn_log.SetLabel("Activer le log")
        else:
            self._metriques.abonner(self._logger)
            self._btn_log.SetLabel("Désactiver le log")

    def _rafraichir(self) -> None:
        self._metriques.actualiser_metriques()
        wx.CallLater(self.INTERVALLE_MS, self._rafraichir)
