## Jogo Wall Street Bets

Cada agente é um investidor e tem um conjunto de ações 

Eles querem maximizar o valor das suas ações 

Cada agente começa com x dinheiro.

Tipos de ações:

* Se A sobe B sobe(eles sabem*) -->Tipo industrias co-dependetes
* Se A sobe B desce(eles sabem) --> Tipo industrias rivais
* Sobem consistentemente (secreto e random)
* Descem consistentemente (secreto e random)
* Random

*alguns podem saber outros não



**Atuators:**

* Comprar
* Vender 
* Hold (não fazer nada)

**Sensors**:

* valueOfShare
* availableShares

**Environment**

* Inaccessible 
  * Não sabe quais as ações que estão sempre a crescer, etc 
  * Todas as ações que todos têm são publicas (???) Tipo um agente que queira falir os outros
* Non-deterministic
  * Uma ação cujo valor sobe ou desce aleatoriamente. Mas cada ação que tem apenas um output que é se compra vai comprar.
* Static
  * Por rounds
* Discrete
* non-episodic
  * as rounds são depedentes umas das outras

* variação das ações, no fim da rondam vê se quantas ação estão à venda,
  * se estiveram mais do que na ronda anterior --> valor diminui 2% 
  * se estiveram menos do que na ronda anterior --> valor aumenta 2% 
  * 
  * Podem haver evento random, tipo covid! e baixa um certo tipo de ações e aumenta outros. Crashes de mercado. subreddit .....

Pool de ações, quando comprar a pool diminui, quando vendem a pool aumenta.

Compram e vendem a um banco central. 

Por ronda pode haver um limite de nr de ações que se podem comprar ou vender por agente.

A cada ronda os agentes ganham uma percentagem do valor das ações que têm ou uma percentagem do valor do aumento de valor que tiveram

**Goal**:

Cada agente pode ter objectivos diferentes, por exemplo:

* **Maximizar o seu próprio valor**
  * Random
  * Arrisca, aposta todo dinheiro numa ação pouco valiosa e depois esperas que ela valoriza
  * Safe, hold, hold, até perceber algum tendência e só aí compra
  * Arrisca & Safe, investe x% do seu dinheiro, mas nunca todo e vê a tendencia
  * Diversifica, compra vários tipos de ações
  * 
* Falir um certo agente
* Maximizar o valor das ações que detem
* Maximizar o dinheiro que tem
* Fazer crash do mercado

Jogo acaba ao fim de x rondas.

Podem vender/comprar ações para alcancar esse objetivo



