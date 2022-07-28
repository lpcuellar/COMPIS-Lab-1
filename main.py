##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  CONSTRUCCION DE COMPILADORES
##  SECCION 10

##  LUIS PEDRO CUELLAR
##  18220

##  NOTAS: 
##
##  *   Todos los métodos creados son de ámbito global, es decir, que los métodos creados en una clase pueden ser accesados por todo el público.
##  *   Mientras que los atributos de una clase son de ámbito local, es decir, que solo pueden ser accesados dentro de la misma clase.

from sys import argv
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees

from dist.YAPLLexer import YAPLLexer
from dist.YAPLParser import YAPLParser
from dist.YAPLVisitor import YAPLVisitor
from dist.YAPLListener import YAPLListener



def main(argv):
    input_file = FileStream(argv[1])
    
    lexer = YAPLLexer(input_file)
    tokens = lexer.getAllTokens()

    #   print tokens
    for t in tokens:
        print(t.text, t.type)

    stream = CommonTokenStream(lexer)
    
    parser = YAPLParser(stream)

    tree = parser.expression()

    # listener = YAPLListener()

    visitor = YAPLVisitor()

    output = visitor.visit(tree)

    print(Trees.toStringTree(tree, None, parser))

if __name__ == "__main__":
    main(argv)