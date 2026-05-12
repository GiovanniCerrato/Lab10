import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._annoInserito = None
        self._statoSelezionato = None

    def handleCalcola(self, e):
        self._annoInserito = self._view._txtAnno.value
        print(self._annoInserito)
        try:
            self._annoInserito = int(self._annoInserito)
        except ValueError:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore numerico",color="red"))
            self._view.update_page()
            return

        if self._annoInserito < 1816 or self._annoInserito > 2016:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"Inserire un anno valido [1816-2016]",color="orange"))
            self._view.update_page()
            return
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato",color="green"))

        self._model.buildGraph(self._annoInserito)
        nodi = self._model.getAllNodes()
        nodi = list(nodi)
        nodi.sort(key=lambda n:n.StateNme)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumCompConnesse()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi:"))

        for n in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{n} -- {self._model.getNumConfinantiStato(n)}"))
            self._view._ddStati.options.append(ft.dropdown.Option(
                key=n.StateNme,
                data=n,
                on_click = self._leggiStato
            ))
        self._view._ddStati.disabled = False
        self._view._btnRaggiungibili.disabled = False
        self._view.update_page()
        return

    def _leggiStato(self,e):
        self._statoSelezionato = e.control.data
        return print(f"Stato: {self._statoSelezionato} ({self._statoSelezionato.CCode})")


    def handleRaggiungibili(self, e):
        if self._statoSelezionato is None:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"Scegliere uno stato di partenza",color="red"))
            self._view.update_page()
            return
        self._view._txt_result.clean()

        listaRaggiungibili, numRaggiungibili = self._model.getRaggiungibili(self._statoSelezionato)
        self._view._txt_result.controls.append(ft.Text(f"Di seguito tutti i paesi raggiungibili da {self._statoSelezionato} ({numRaggiungibili}):"))

        for r in listaRaggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{r}"))

        self._view.update_page()
        pass

