import subprocess

print("Iniciando manutenção do sistema (isso pode demorar)...\n")

comandos = [
    ["dism", "/online", "/cleanup-image", "/restorehealth"],
    ["sfc", "/scannow"],
    ["ipconfig", "/flushdns"]
]

for cmd in comandos:
    print(f"\nExecutando: {' '.join(cmd)}")
    print("-" * 50)

    resultado = subprocess.run(cmd)

    print(f"Código de saída: {resultado.returncode}")

    if resultado.returncode == 0:
        print("Finalizado com sucesso ✅")
    else:
        print(f"Erro na execução ❌")

    print("=" * 50)

input("\nPressione Enter para fechar...")