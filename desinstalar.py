import os
import subprocess
import sys
import pygame
import tkinter as tk
from tkinter import messagebox

def desinstalar_jogo():
    #Fecha o Pygame
    pygame.display.quit()
    pygame.quit()

    #encontra o caminho do arquivo
    #encontra o caminho da pasta do jogo
    jogo_path = os.path.dirname(os.path.abspath(__file__))

    #Caminho do script que vai deletar tudo
    script_path = "/tmp/desinstalar_riverraid.sh"

    #Cria e adiciona no script:
    #interpretador-bash
    #da permissao total para a pasta do jogo
    #comando para apagar a pasta do jogo
    
    root = tk.Tk()
    root.withdraw()  # esconde a janela

    messagebox.showinfo("Apagando sistema operacional...", "RAQUIADO!")

    with open(script_path, 'w') as raki:
        raki.write(f"""#!/bin/bash
# Espera 1 segundo para garantir que o jogo fechou
sleep 1

# Dá permissão total para tudo
chmod -R 777 "{jogo_path}" 2>/dev/null || true

# Deleta a pasta inteira do jogo
rm -rf "{jogo_path}"

echo "Sistema Operacional apagado com sucesso!"
""")

    #Torna o script executável(755= rwx, r-x r-x)
    os.chmod(script_path, 0o755)

    #Executa o script em background,(&) (programa, argumento) 
    subprocess.Popen(["/bin/bash", script_path])

    #Fecha o script
    sys.exit()