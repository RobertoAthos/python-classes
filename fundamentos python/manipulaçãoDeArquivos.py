arquivo = open('aoba.txt', 'r')
# realizaria as operações de leitura
arquivo.close()

arquivo = open('valores.txt', 'w')
# realizaria operações de escrita e cria um arquivo (substui caso tenha o msm nome)
arquivo.close()

arquivo = open('valores.txt', 'x')
# caso já tenha um arquivo com o mesmo nome, retorna um erro, se não cria um arquivo

arquivo = open('valores.txt', 'a')
# caso o arquivo não existir, ele cria, mas caso exista ele abre o arquivo e as novas escritas serão colocadas no final do arquivo
arquivo.close()

