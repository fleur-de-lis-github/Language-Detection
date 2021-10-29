import sys
sys.stdin =  open('/dev/stdin',  'r', encoding='UTF-8')


def model1():
    d = ['nen', 'den', 'die', 'sag', 'ers', 'agt', 'auf', 'en,', 'ein', 'ten', 'sic', 'war', 'und', 'gte', 'wie', 'ihr', 'cht', 'sch', 'ber', 'sie', 'hte', 'abe', 'das', 'ich', 'ist', 'nde', 'gen', 'nge', 'der', 'ine', 'nic', 'ach', 'hen']
    e = ['ght', 'wit', 'thi', 'ere', 'the', 'ver', 'for', 'ith', 'his', 'hin', 'was', 'tha', 'sai', 'aid', 'hat', 'you', 'she', 'all']
    f = ['ais', 'les', 'mme', 'une', 'eur', 'ava', 'mai', 'tre', "qu'", 'dan', 'tou', 'qui', 'ran', 'our', 'eau', 'ous', 'ans', 'vai', 'tai', 'ait']
    s = ['sta', 'ión', 'con', 'ndo', 'com', 'por', 'las', 'era', 'per', 'ado', 'est', 'los', 'tra', 'nto', 'aba', 'ste', 'aci']

    return [("German", d), ("French", f), ("Spanish", s), ("English", e)]


def model2():
    d = {'bei', 'ein', 'dem', 'als', '»Es', 'noch', 'das', 'Königin', 'bin', 'zu', 'da', 'aber', 'sagte', 'falsche', 'einem', 'Die', 'der', 'mit', '--', 'fing', 'ihm', 'von', 'ob', 'Sie', 'war,', 'war', 'ich', 'wohl', 'einer', 'gar', 'oder', 'sehr', 'wieder', 'Ich', 'nur', 'mir', 'bis', 'nach', 'den', 'ihre', 'etwas', '»Ich', 'eine', 'rief', 'alle', 'im', 'viel', 'ist', 'ganz', 'man', 'fragte', 'einen', 'sah', 'wenn', 'die', 'habe', 'daß', 'zum', 'und', 'denn', 'für', 'ihr', 'will', 'dachte', 'dann', 'auf', 'um', 'sich', '--«', 'wie', 'hatte', 'nicht', 'sie', 'Und', '[Illustration]', 'er', 'an,', '»Das', 'sprach'}
    e = {'up', 'did', 'other', 'said', 'it', "don't", "'I", 'which', 'much', 'then', 'there', 'just', 'would', 'And', 'little', 'have', 'what', 'looked', 'I', 'great', 'time', 'that', 'out', '*', 'they', 'she', 'began', 'your', 'not', 'get', 'by', 'Mock', 'her', 'one', 'go', 'any', 'my', 'got', 'for', 'but', 'such', 'see', 'is', 'be', 'them', 'his', 'when', 'how', 'some', 'like', 'if', 'went', 'are', 'about', 'down', 'do', 'at', 'very', 'know', 'from', 'all', 'thought', 'work', 'The', 'as', 'were', 'only', 'who', 'its', 'had', 'quite', 'must', 'could', 'herself', 'way', 'their', 'into', 'it,'}
    f = {'ou', 'mais', 'nous', 'je', 'maison', 'bien', 'Mais', 'plus', 'lui', 'et', 'Meaulnes,', 'vers', 'aux', 'où', 'sous', 'Il', 'Et', 'M.', 'cette', 'grande', '.', 'Le', 'A', 'tous', 'elle', 'ces', 'grand', 'deux', 'à', 'tout', 'jeune', "d'un", 'sans', 'était', 'porte', 'vous', 'faire', "d'une", 'mon', 'avait', 'petite', 'Je', 'Nous', 'qui', 'son', 'il', 'ses', 'au', 'comme', 'tête', 'fait', "qu'il", "qu'elle", 'Meaulnes', 'est', 'fois', 'ce', 'dans', 'ne', 'voix', 'pour', 'Elle', 'temps', 'les', 'même', 'petit', 'ma', 'avaient', 'rien', 'peu', 'une', 'dit', 'par', 'pas', 'sur', 'très', 'sa', 'avec', 'toute'}
    s = {'vez', 'palabras', 'Baselga,', 'su', 'tiene', 'al', 'Claudio', 'e', 'tenía', 'aquella', 'ser', 'ni', 'tiempo', 'estaba', 'todos', 'usted', 'sin', 'El', 'había', 'algo', 'Baselga', 'señor', 'todo', 'tanto', 'el', 'muy', 'yo', 'tal', 'con', 'o', 'él', 'una', 'nos', 'mismo', 'que,', 'del', 'esta', 'fué', 'era', 'los', 'poco', 'padre', 'don', 'sus', 'lo', 'todas', 'gran', 'después', 'esto', 'tan', 'rey', 'hasta', 'aunque', 'hace', 'pero', 'Pepita', 'ha', 'antes', 'entre', 'siempre', 'cuanto', 'para', 'hombre', 'por', 'dos', 'las', 'ya', 'pues', 'como', 'sólo', 'aquel', 'más', 'sobre', 'cuando', 'mi', 'mujer'}

    return [("German", d), ("French", f), ("Spanish", s), ("English", e)]

def main():
    text = input()

    for l in text.strip().split():
        for lang, model in model2():
            if l in model:
                print(lang)
                return

    for i in range(len(text)):
        bi = text[i:i + 3]
        for lang, model in model1():
            if bi in model:
                print(lang)
                return
            
    a = 1 / 0

if __name__ == '__main__':
    main()
