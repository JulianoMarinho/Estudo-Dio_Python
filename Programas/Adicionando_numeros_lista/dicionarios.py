#exemplo

pessoa = {
    "nome": "Guilherme", 
    "idade": 28
    }

#usando o construtor dict
pessoa = dict(nome= "Guilherme", 
              idade=28)

#adicionando valores
pessoa["telefone"] = "3333-1234"

#acessando dados do dicionario

pessoa["nome"] #Guilherme

#sobrescrevendo os valores

pessoa["nome"] = "Maria"

#os valores poem ser tanto imutaveis qnto mutaveis,
#a chave precisa ser imutavel

#o dicionario possui uma estrutura parecida com um bd
#ex.:

contatos = {
    "fulano@email.com":{"nome":"Fulano", "telefone":"3333-2221"},
    "ciclano@email.com":{"nome":"ciclano", "telefone":"3333-2222"}
}

#acessando valores:

contatos["fulano@email.com"]["telefone"] #3333-2221

#percorrendo um discionario

#for chave, valor in contatos.items():
    #print(chave,valor)

#metodos dicionario

#clear : limpa todos os valores do dicionario
#copy: copia os valores de um dicionario
#fromkeys atualiza chaves em um dicionario

#ex.:

contatos.fromkeys(["sexo, idade"]) #{"nome": none, "telefone": none}

print(contatos)


seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq,10)

print(dict)


#get
#da para passar um valor padrão para caso o get n encontre o que foi buscado
#ex contatos.get("chave", {})

#items retorna uma lista de tuplas

#keys, retorna só as chaves do dicionario

novo_dicionario = {"a": 100, 1: "teste"}

print(novo_dicionario.keys()) #{ [a], [1]}

#pop remove uma chave do dicionario e retorna o valor removido

#set default

#update atualiza os valores de um dicionario

#values

#in
