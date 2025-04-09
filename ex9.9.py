def idades_reversiveis():
    for idade_filho in range(0, 100):
        for diferenca in range(10, 70):
            count = 0
            for ano in range(0, 100):
                idade_f = idade_filho + ano
                idade_m = idade_f + diferenca
                if idade_m > 120 or idade_f > 99:
                    break

                # inverter idade do filho
                if str(idade_f).zfill(2)[::-1] == str(idade_m).zfill(2):
                    count += 1

            if count == 8:
                print(f" Idade atual do filho: {idade_filho}")
                print(f" Diferença de idade (mãe - filho): {diferenca}")
                print(f" Idade atual da mãe: {idade_filho + diferenca}")
                return

idades_reversiveis()
