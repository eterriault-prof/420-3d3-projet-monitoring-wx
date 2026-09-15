from datetime import datetime
from observers.observer import Observateur


class LoggerFichier(Observateur):

    def __init__(self, chemin_fichier: str = "monitoring.log"):
        self._chemin = chemin_fichier

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = (
            f"{horodatage} | "
            f"CPU: {donnees['cpu']:.1f}% | "
            f"RAM: {donnees['ram']:.1f}% | "
            f"Disque: {donnees['disque']:.1f}%\n"
        )
        with open(self._chemin, 'a') as f:
            f.write(ligne)
