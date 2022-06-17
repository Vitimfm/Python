usadoMarço = float(input('Digite o valor usado no mês de Março: '))
pagoMarço = float(input('Digite o valor pago no mês de Março: '))
usadoAbril = float(input('Digite o valor usado no mês de Abril: '))

restante = usadoMarço - pagoMarço

FaturaAbril = usadoAbril + restante + (restante * 3.3 / 100)

print(f'Fatura de abril é {FaturaAbril}')