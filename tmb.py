#Taxa de metabolismo basal

altura = float(input("Digite sua altura em cm: "))
peso = float(input("Digite seu peso em kg: "))
idade = int(input("Digite sua idade em anos: "))
#Calculo da taxa de metabolismo basal
tmb = float(66 + (13.8 * peso) + (5 * altura) - (6.8 * idade))
print("Sua taxa de metabolismo basal é:", tmb)

#Taxa de metabolismo basal de acordo com a atividade fisica
nenhumaAtividadeFisica = float(1.25 * tmb)
print("Com nenhuma atividade física:", nenhumaAtividadeFisica)

atividadeFisicaModerado = float(1.35 * tmb)
print("Com atividade Fisica Moderada:", atividadeFisicaModerado)

atividadeFisicaIntensa = float(1.45 * tmb)
print("Com Atividade fisica intensa:", atividadeFisicaIntensa)