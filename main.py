from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
## Mude o Range para a quantidade de capitulos que quer baixar + 1 <capitulo inicial - capitulo final + 1>
for numero in range(1, 5):
    numero_pagina = 1
    caminho_pasta_capitulo = f"capitulo-{numero}"
    if not os.path.exists(caminho_pasta_capitulo):
        os.makedirs(caminho_pasta_capitulo)
        print(f"Pasta para o capítulo {numero} criada com sucesso!")
    else:
        print(f"A pasta para o capítulo {numero} já existe.")
    while True:
        ## URL para a api de algum scan
        url_pagina = f"https://exemplo.com/uploads/manga-images/c/anime/capitulo-{numero}/{numero_pagina}.png"
        
        driver.get(url_pagina)
        time.sleep(1)
        print("pagina carregada")
        if "404" in driver.page_source:
            print("Final do capitulo")
            break
        else:
            driver.save_screenshot(f"capitulo-{numero}/{numero_pagina}.png")
            time.sleep(1)
            print(f"pagina salva {numero_pagina}")
            numero_pagina += 1
driver.quit()


