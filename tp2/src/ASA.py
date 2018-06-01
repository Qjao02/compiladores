from Token import Token

class AST(object):
    def __init__(self, nome):
         self.nome = nome;
         self.children = []
         self.tipo = None  #tipo do nó. Compound, Assign, ArithOp, etc
         self.value = None

    def __str__(self, level=0):
        ret = "\t"*level+ repr(self) +"\n"
        for child in self.children:
            if (child != None):
                ret += child.__str__(level+1) #level+1
        return ret

    def __repr__(self):
        return self.nome

    def __evaluate__(self):
        for child in self.children:
            if (child != None):
                return child.__evaluate__()

class Compound(AST):
    """Represents a 'BEGIN ... END' block"""
    def __init__(self):
        AST.__init__(self,'Block')
        print('Criando um nó do tipo Block.')
        #self.children = []
    def __repr__(self):
        return self.nome

class Assign(AST):
    def __init__(self, left, op, right):
        AST.__init__(self,'Assign');
        print('Criando um nó do tipo Assign.')

        if(not(left is None)):
            self.children.append(left)

        if(not(right is None)):    
            self.children.append(right)

        self.left = left
        self.token = self.op = op
        self.right = right
    def __repr__(self):
        return self.nome

class If(AST):
    def __init__(self, exp, c_true, c_false):
        AST.__init__(self, 'If')
        print('Criando um nó do tipo If.')
        if(not(exp is None)):
            self.children.append(exp)
        
        if(not(c_true is None)):
            self.children.append(c_true)
        
        if(not(c_false is None)):
            self.children.append(c_false)
        
        self.exp = exp;
        self.c_true = c_true;
        self.c_false = c_false;
    def __repr__(self):
        return self.nome

class While(AST):
    def __init__(self, exp, commands):
        AST.__init__(self,'While')
        print('Criando um nó do tipo While.')
        
        if(not(exp is None)):
            self.children.append(exp)

        if(not (commands is None)):
            self.children.append(commands)

        self.exp = exp;
        self.commands = commands;
    def __repr__(self):
        return self.nome

class Read(AST):
    def __init__(self, id_):
        AST.__init__(self,'Read')
        print('Criando um nó do tipo Read.')
        if(not(id_ is None)):
            self.children.append(id_)
        self.id = id_;
    def __repr__(self):
        return self.nome

class Print(AST):
    def __init__(self, exp):
        AST.__init__(self,'Print')
        print('Criando um nó do tipo Print.')
        
        if(not(exp is None)):
            self.children.append(exp)
        
        self.exp = exp;

    def __repr__(self):
        return self.nome

class Expr(AST):
    def __init__(self, nome, op, left, right):
        AST.__init__(self,nome)
        
        if(not(left is None)):
            self.children.append(left)
        
        if(not(right is None)):
            self.children.append(right)
        
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        #self.left.repr();
        return self.op

class LogicalOp(Expr):
    def __init__(self, op, left, right):
        Expr.__init__(self,'LogicalOp', op, left, right)
        print('Criando um nó do tipo LogicalOp com operador ' + str(op))

class ArithOp(Expr):
    def __init__(self, op, left, right):
        Expr.__init__(self,'ArithOp', op, left, right)
        print('Criando um nó do tipo ArithOp com operador ' + str(op))

class RelOp(Expr):
    def __init__(self, left, op, right):
        Expr.__init__(self,'RelOp', op, left, right)
        print('Criando um nó do tipo RelOp com operador ' + str(op))

class Id(AST):
    """The Var node is constructed out of ID token."""
    def __init__(self, token):
        AST.__init__(self,'Id')
        print('Criando um nó do tipo Id.')
        #self.children.append(token)
        self.token = token
        self.value = token.value

    def __repr__(self):
        return repr(self.token.getLexema())

    def __evaluate__(self):
        return self.value

class Num(AST):
    def __init__(self, token):
        AST.__init__(self,'Num')
        print('Criando um nó do tipo Num.')
        #self.children.append(token)
        self.token = token
        self.value = token.value  #em python, não precisamos nos preocupar com o tipo de value

    def __repr__(self):
        return repr(self.token.getLexema())

    def __evaluate__(self):
        return self.value

def print_tree(current_node, indent="", last='updown'):
    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1
    size_branch = {child: nb_children(child) for child in current_node.children}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(current_node.__repr__()))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.__repr__(), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(current_node.__repr__()))
        print_tree(child, indent=next_indent, last=next_last)
