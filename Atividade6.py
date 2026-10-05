<span style="font-size:inherit">import random</span>

<span style="font-size:inherit">numero = random.randint(1, 100)</span>
<span style="font-size:inherit">print("Número sorteado:", numero)</span>

<span style="font-size:inherit">filmes = ["Titanic", "Matrix", "Avatar", "Rei Arthur", "Interestelar"]</span>

<span style="font-size:inherit">filme = random.choice(filmes)</span>
<span style="font-size:inherit">print("Filme escolhido:", filme)</span>

<span style="font-size:inherit">random.shuffle(filmes)</span>
<span style="font-size:inherit">print("Lista embaralhada:", filmes)</span>