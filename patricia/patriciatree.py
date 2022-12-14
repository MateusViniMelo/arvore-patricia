class Arvore:

    def __init__(self, raiz):

        """
        Inicia a árvore
        :param str raiz:
        """

        self.raiz = raiz + "$"


    def get_intersect(self, p1, p2):

        """
        Buca o ponto onde duas strings de diferenciam
        :param str p1:
        :param str p2:
        :return int:
        """
        for i in range(len(p1)):

            if len(p2) > i:

                if p1[i] != p2[i]: return i


    def insere(self, palavra):

        """
        Insere uma string na árvore
        :param str palavra:
        :return None:
        """

        # print("Inserindo %s" % palavra)

        if self.check(palavra):

            print("[Erro] Palavra já inserida")

            return

        palavra += '$'

        pai = None

        node = self.raiz

        i = 0

        while 1:

            # Caso nó folha

            if type(node) == str:

                pos = self.get_intersect(palavra, node)

                # Caso nó folha é raiz também

                if pai is None:

                    l = sorted([(ord(palavra[pos]), palavra), (ord(node[pos]),node)])

                    self.raiz = Node(pos, chr(l[0][0]), l[0][1][:pos])

                    self.raiz.filhos = [k[1] for k in l]

                    return


                # Caso padrão

                else:

                    lado = pai.filhos.index(node)

                    l = sorted([(ord(palavra[pos]), palavra), (ord(node[pos]),node)])

                    pai.filhos[lado] = Node(pos, chr(l[0][0]), l[0][1][:pos])

                    pai.filhos[lado].filhos = [k[1] for k in l]

                    return



            else:

                prox = node.get(palavra)

                # Caso prefixo não combina

                if not prox:

                    pos = self.get_intersect(palavra, node.prefixo)

                    l = sorted([(ord(palavra[pos]), palavra), (ord(node.prefixo[pos]),node)])

                    # Caso raiz

                    if pai is None:

                        self.raiz = Node(pos, chr(l[0][0]), palavra[:pos])

                        self.raiz.filhos = [k[1] for k in l]

                        return

                    else:

                        lado = pai.filhos.index(node)

                        pai.filhos[lado] = Node(pos, chr(l[0][0]), palavra[:pos])

                        pai.filhos[lado].filhos = [k[1] for k in l]

                        return

                # Base de iteração

                else:

                    pai = node

                    node = prox


    def check(self, palavra):

        palavra += '$'

        node = self.raiz

        while 1:

            if type(node) == str:

                return node == palavra

            next = node.get(palavra)

            if next:

                node = next

            else:

                return False


    def remove(self, palavra):

        if not self.check(palavra):

            print("[Erro] Palavra não encontrada")
            return

        palavra += '$'

        avo = None
        pai = None
        node = self.raiz

        while 1:

            if type(node) == str:

                if pai is None:

                    print("[Erro] Não é possível remover único item da arvore")

                    return

                else:

                    pai.filhos.remove(node)

                    novo_sucessor = pai.filhos[0]

                    if avo is None:

                        self.raiz = novo_sucessor

                        del pai

                        return

                    else:

                        index = avo.filhos.index(pai)

                        avo.filhos[index] = novo_sucessor

                        del pai

                        return

            else:

                prox = node.get(palavra)

                if pai is None:

                    pai = node

                    node = prox

                else:

                    avo = pai

                    pai = node

                    node = prox

    def derivados(self, prefixo):

        """
        Exibe folhas derivadas de determinado prefixo
        :param str prefixo:
        :return str[]:
        """

        tam = len(prefixo)

        node = self.raiz

        while 1:

            if type(node) == str:

                if node[:tam] == prefixo:

                    return [node[:-1]]

                else:

                    return []

            else:

                if node.prefixo == prefixo or node.prefixo[:tam] == prefixo:

                    return node.derivados()

                next = node.get(prefixo)

                if next:

                    node = next

                else:

                    return []