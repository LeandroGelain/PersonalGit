from TrelloApi.GeraRelatório import GeraRelatorio as GR
from TrelloApi.TrelloConfig import Trello as tcfg
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import time
import json
import threading
import os

class app(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.gerarRelatorio = GR()
		self.tconfig = tcfg()
		self.key = self.tconfig.key
		self.token = self.tconfig.token
		
		self.master = master
		self.pack()
		self._nameBoard = None
		self._nome = None
		self.main()

	def main(self):    
		''' 
		Função main para a interface grafica e os metodos
		'''
		self.tabControl = ttk.Notebook(root)
		self.tab1 = ttk.Frame(self.tabControl)
		self.gridTitle = ttk.Label(self.tabControl, text='Gerador de Relatórios Agro Academy Trello')
		self.gridTitle.grid(column=3, row=0, padx=10)
		'''
  		Grid de inputs
		'''
		self.desc_intro = ttk.Label(self.tabControl, text='   Não fechar o programa enquanto está sendo executado.').grid(column=3, row=3, pady=30)
		self.desc_obs = ttk.Label(self.tabControl,   text='Caso Seja cancelado o programa antes de terminar a execução', foreground='red').grid(column=3, row=4)
		self.desc_obs2 = ttk.Label(self.tabControl , text='Delete o aquivo gerado e reinicie a execução para evitar repetições', foreground='red').grid(column=3, row=5)
		# criar funçao para abrir o excel e escrever na possição correta
		self.btnCreate = ttk.Button(self.tabControl, text='Gerar Relatório',command=lambda: threading.Thread(target=self.Relatorio).start())
		self.btnCreate.grid(column=3, row=6, pady=70)
			
		self.progressbar = ttk.Progressbar(self.tabControl,orient=HORIZONTAL, length=200, mode='indeterminate')
		self.progressbar.place(x=80,y=300)
		self.progressbar.start(interval=50)
		
		self.tabControl.pack(expand=2, fill='both')
	# Chamando funçoes de outros arquivos

	def Relatorio(self):
		print('iniciando geração de relatório')
		self.relatorio = self.gerarRelatorio.function_main()
		print(self.relatorio)
		return self.relatorio

root = tk.Tk()

root.title('Agro academy Relatorios')
root.geometry('355x400')
app = app(master=root)
app.master.resizable(0,0)
app.mainloop()