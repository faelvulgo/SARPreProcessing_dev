from pathlib import Path
import subprocess
from datetime import datetime
from tqdm import tqdm
import sys

"""
Configurations: 
Set the GPT.exe path of ESA Snap and the worflow .XML path
Set the images directory and the output directory
"""

GPT_PATH = r"PATH"

WORKFLOW = r"PATH"

INPUT_DIR = Path(r"PATH")
OUTPUT_DIR = Path(r"PATH")

OUTPUT_DIR.mkdir(exist_ok=True)

# Image lists
arquivos = sorted(INPUT_DIR.glob("*.zip"))

if len(arquivos) == 0:
    print("\nNenhuma imagem .zip encontrada em /input")
    sys.exit()

print(f"\nEncontradas {len(arquivos)} imagens\n")

"""
Processing:
Execute the processing workflow using the ESA Snap GPT and tell the time it took.
"""
falhas = []

for arquivo in tqdm(arquivos, desc="Processando imagens"):

    nome_saida = arquivo.stem + ".tif"
    saida = OUTPUT_DIR / nome_saida

    if saida.exists():
        print(f"\nPulando {arquivo.name} (já processado)")
        continue

    cmd = [
        GPT_PATH,
        WORKFLOW,
        f"-Pinput={arquivo}",
        f"-Poutput={saida}"
    ]

    try:

        inicio = datetime.now()

        resultado = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        fim = datetime.now()

        tempo = fim - inicio

        if resultado.returncode == 0:

            print(f"\nOK: {arquivo.name}")
            print(f"Tempo: {tempo}")

        else:

            print("\nERRO COMPLETO:")
            print(resultado.stderr)

            falhas.append(arquivo.name)

            with open("erros.log", "a", encoding="utf-8") as f:

                f.write("\n")
                f.write("="*60)
                f.write("\n")
                f.write(f"{arquivo.name}\n")
                f.write(resultado.stderr)
                f.write("\n")

    except Exception as e:

        print(f"\nFalha crítica: {arquivo.name}")

        falhas.append(arquivo.name)

        with open("erros.log", "a", encoding="utf-8") as f:

            f.write("\n")
            f.write("="*60)
            f.write("\n")
            f.write(f"{arquivo.name}\n")
            f.write(str(e))
            f.write("\n")

# Summary
print("\n")
print("="*50)

if len(falhas) == 0:

    print("PROCESSAMENTO CONCLUÍDO SEM ERROS")

else:

    print(f"{len(falhas)} arquivos falharam")

    for f in falhas:
        print(f" - {f}")

    print("\nVeja erros.log")

print("="*50)
