import wx
import psutil
from datetime import datetime


class App(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Monitoring système")
        self.SetSize((400, 550))

        panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # --- CPU ---
        cpu_box = wx.StaticBox(panel, label="CPU")
        cpu_sizer = wx.StaticBoxSizer(cpu_box, wx.VERTICAL)
        self.label_cpu = wx.StaticText(cpu_box, label="0%")
        font = self.label_cpu.GetFont()
        font.SetPointSize(24)
        font.MakeBold()
        self.label_cpu.SetFont(font)
        self.barre_cpu = wx.Gauge(cpu_box, range=100, size=(300, 20))
        cpu_sizer.Add(self.label_cpu, 0, wx.ALL | wx.CENTER, 5)
        cpu_sizer.Add(self.barre_cpu, 0, wx.ALL | wx.CENTER, 5)
        self.sizer.Add(cpu_sizer, 0, wx.ALL | wx.EXPAND, 10)

        # --- RAM ---
        ram_box = wx.StaticBox(panel, label="RAM")
        ram_sizer = wx.StaticBoxSizer(ram_box, wx.VERTICAL)
        self.label_ram = wx.StaticText(ram_box, label="0%")
        font2 = self.label_ram.GetFont()
        font2.SetPointSize(24)
        font2.MakeBold()
        self.label_ram.SetFont(font2)
        self.barre_ram = wx.Gauge(ram_box, range=100, size=(300, 20))
        ram_sizer.Add(self.label_ram, 0, wx.ALL | wx.CENTER, 5)
        ram_sizer.Add(self.barre_ram, 0, wx.ALL | wx.CENTER, 5)
        self.sizer.Add(ram_sizer, 0, wx.ALL | wx.EXPAND, 10)

        # --- Disque ---
        disque_box = wx.StaticBox(panel, label="Disque")
        disque_sizer = wx.StaticBoxSizer(disque_box, wx.VERTICAL)
        self.label_disque = wx.StaticText(disque_box, label="0%")
        font3 = self.label_disque.GetFont()
        font3.SetPointSize(24)
        font3.MakeBold()
        self.label_disque.SetFont(font3)
        self.barre_disque = wx.Gauge(disque_box, range=100, size=(300, 20))
        disque_sizer.Add(self.label_disque, 0, wx.ALL | wx.CENTER, 5)
        disque_sizer.Add(self.barre_disque, 0, wx.ALL | wx.CENTER, 5)
        self.sizer.Add(disque_sizer, 0, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(self.sizer)
        self.rafraichir()

    def rafraichir(self):
        # Lire les métriques
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        disque = psutil.disk_usage('/').percent

        # Mettre à jour CPU
        self.label_cpu.SetLabel(f"{cpu:.1f}%")
        self.barre_cpu.SetValue(int(cpu))

        # Mettre à jour RAM
        self.label_ram.SetLabel(f"{ram:.1f}%")
        self.barre_ram.SetValue(int(ram))

        # Mettre à jour Disque
        self.label_disque.SetLabel(f"{disque:.1f}%")
        self.barre_disque.SetValue(int(disque))

        # Écrire dans le fichier log
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = (
            f"{horodatage} | "
            f"CPU: {cpu:.1f}% | "
            f"RAM: {ram:.1f}% | "
            f"Disque: {disque:.1f}%\n"
        )
        with open("monitoring.log", 'a') as f:
            f.write(ligne)

        wx.CallLater(2000, self.rafraichir)


if __name__ == "__main__":
    app = wx.App()
    fenetre = App()
    fenetre.Show()
    app.MainLoop()
