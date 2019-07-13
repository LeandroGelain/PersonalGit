Comando para transformar py - exe

Liberar path windows:
	path config:
	C:\Python37\Scripts (no caso, python3.7)

Instalar pyinstaller:
	pip install pyinstaller

Py to Exe:
	pyinstaller 'nomearquivo'

Add icone no exe:
	pyinstaller -i ["path icone"]['nomearquivo]

	exemplo: pyinstaller -i "C:\Program File\PythonIcone.ico" executavel.py