# media.py
def calcular_media(notas):
    """Recebe uma lista de 4 notas e retorna a média."""
    return sum(notas) / len(notas)

def obter_situacao(media):
    """Retorna a situação do aluno com base na média."""
    if media >= 7.0:
        return "Aprovado(a) ✅"
    elif media >= 5.0:
        return "Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"

def main():
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("⚠️ A nota deve estar entre 0 e 10.")
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")

    media = calcular_media(notas)
    situacao = obter_situacao(media)
    print(f"\nMédia: {media:.2f} — Situação: {situacao}")

if __name__ == "__main__":
    main()
