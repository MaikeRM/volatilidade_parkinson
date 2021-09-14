# volatilidade_parkinson

Volatilidade Parkinson

Um questionamento que muito Jr. assim como eu já deve ter feito ao mensurar a volatilidade histórica: se analisarmos apenas o fechamento dos preços, perdemos dados da movimentação intradiária do papel, ou seja, se o preço de fechamento do ativo em D-1 foi 10 dinheiros, e o fechamento de hoje é 10 dinheiros a variação da vol é mínima dependendo do modelo que estiver utilizando.

A próxima questão é: existe na literatura alguma forma de considerar a volatilidade intradiária? Sim, obviamente existe e há muito tempo.

Michael Parkinson em 1980, tem como objetivo estimar a volatilidade de uma série temporal a partir dos preços de High e Low nos fornecendo a seguinte equação:
<a><img src="https://media-exp1.licdn.com/dms/image/C4D12AQE_c0-HBVyo8A/article-inline_image-shrink_1000_1488/0/1630432150303?e=1637193600&v=beta&t=hucELPLSvgsf18X0NiYYvXaebCQtwlDaAWGFJiUSUxk"/></a>

Novidade para alguns, assunto batido para outros, mas a intenção é sempre alcançar os desavisados. Caso você ainda utilize a vol histórica fica a dica de implementação.

<a><img src="https://media-exp1.licdn.com/dms/image/C4D12AQH43Ha7cPAFSQ/article-inline_image-shrink_1500_2232/0/1630432465174?e=1637193600&v=beta&t=Ra8AUoVi9m71cRFueGf4BTzeWhyR8huCMt7ZrGdvjY4"  width="80%"/></a>


Segue o código completo no github: https://github.com/MaikeRM/volatilidade_parkinson.git

Referências

[1] E. Sinclair, Volatility Trading, John Wiley & Sons, 2008
