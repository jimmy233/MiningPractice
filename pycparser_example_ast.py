#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:36:55 2018

@author: jimmy233
"""

#-----------------------------------------------------------------
# pycparser: explore_ast.py
#
# This example demonstrates how to "explore" the AST created by
# pycparser to understand its structure. The AST is a n-nary tree
# of nodes, each node having several children, each with a name.
# Just read the code, and let the comments guide you. The lines
# beginning with #~ can be uncommented to print out useful
# information from the AST.
# It helps to have the pycparser/_c_ast.cfg file in front of you.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# License: BSD
#-----------------------------------------------------------------
from __future__ import print_function
import sys
import os
# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast

# This is some C source to parse. Note that pycparser must begin
# at the top level of the C file, i.e. with either declarations
# or function definitions (this is called "external declarations"
# in C grammar lingo)
#
# Also, a C parser must have all the types declared in order to
# build the correct AST. It doesn't matter what they're declared
# to, so I've inserted the dummy typedef in the code to let the
# parser know Hash and Node are types. You don't need to do it
# when parsing real, correct C code.

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text
text = read_file_as_str('train/0ae1/2d61b2d4f64f4d87.txt')

# Create the parser and ask to parse the text. parse() will throw
# a ParseError if there's an error in the code
#
parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

# Uncomment the following line to see the AST in a nice, human
# readable way. show() is the most useful tool in exploring ASTs
# created by pycparser. See the c_ast.py file for the options you
# can pass it.

 
#ast.show(showcoord=True)
print(len(ast.ext))
ast.ext[0].show()
# OK, we've seen that the top node is FileAST. This is always the
# top node of the AST. Its children are "external declarations",
# and are stored in a list called ext[] (see _c_ast.cfg for the
# names and types of Nodes and their children).
# As you see from the printout, our AST has two Typedef children
# and one FuncDef child.
# Let's explore FuncDef more closely. As I've mentioned, the list
# ext[] holds the children of FileAST. Since the function
# definition is the third child, it's ext[2]. Uncomment the
# following line to show it:
#ast.ext[1].show()

# A FuncDef consists of a declaration, a list of parameter
# declarations (for K&R style function definitions), and a body.
# First, let's examine the declaration.
#function_decl = ast.ext[1]
# function_decl, like any other declaration, is a Decl. Its type child
# is a FuncDecl, which has a return type and arguments stored in a
# ParamList node

#function_decl.type.show()
#function_decl.type.args.show()

# The following displays the name and type of each argument:
#for param_decl in function_decl.type.args.params:
    #print('Arg name: %s' % param_decl.name)
    #print('Type:')
    #param_decl.type.show(offset=6)

# The body is of FuncDef is a Compound, which is a placeholder for a block
# surrounded by {} (You should be reading _c_ast.cfg parallel to this
# explanation and seeing these things with your own eyes).
# Let's see the block's declarations:
#if hasattr(ast.ext[2],'body') == True:
#    print("sc")
#function_body = ast.ext[0].body
#function_body.block_items[15].show()
#print(dir(function_body.block_items[15].children()[0][1].children()[0][1].right.name))
s = len(ast.ext)
for i in range(0,s):
    if hasattr(ast.ext[i],'body') == True:
        function_body=ast.ext[i].body
        s1=len(function_body.block_items)
        for j in range(0,s1):
            if hasattr(function_body.block_items[j],'name') == True:
                if(hasattr(function_body.block_items[j].name,'name')) == True:
                        t=function_body.block_items[j].name.name
                        if t=='scanf' or t=='printf':
                            res=t+' '+function_body.block_items[j].children()[1][1].exprs[0].type+' '+function_body.block_items[j].children()[1][1].exprs[0].value
                            print(res)
'''for i in range(0,s):
    if hasattr(ast.ext[i],'body') == True:
        function_body=ast.ext[i].body
        s1=len(function_body.block_items)
        for j in range(0,s1):
            if hasattr(function_body.block_items[j],'children') == True:
                if(hasattr(function_body.block_items[j].children[0][1],'children')) == True:
                    cc=function_body.block_items[15].children()[0][1].children()[0][1]
                    if(hasattr(cc,'left')):
                        print'''
                    
#print(dir(function_body.block_items[6]))
#print(function_body.block_items[6].init.exprs[1].value)
#print(len(function_body.block_items))
# The following displays the declarations and statements in the function
# body
#i = 0
#for decl in function_body.block_items:
#   i=i+1
#    decl.show()

# We can see a single variable declaration, i, declared to be a simple type
# declaration of type 'unsigned int', followed by statements.

# block_items is a list, so the third element is the For statement:

#for_stmt = function_body.block_items[13]
#print(dir(for_stmt.name))

#for_stmt.show()

#print(for_stmt.type.type.names)

# As you can see in _c_ast.cfg, For's children are 'init, cond,
# next' for the respective parts of the 'for' loop specifier,
# and stmt, which is either a single stmt or a Compound if there's
# a block.
#
# Let's dig deeper, to the while statement inside the for loop:

#while_stmt = for_stmt.stmt.block_items[1]
#print(while_stmt)
#while_stmt.show()

# While is simpler, it only has a condition node and a stmt node.
# The condition:

#while_cond = while_stmt.cond
#while_cond.show()

# Note that it's a BinaryOp node - the basic constituent of
# expressions in our AST. BinaryOp is the expression tree, with
# left and right nodes as children. It also has the op attribute,
# which is just the string representation of the operator.

#print(while_cond.op)
#while_cond.left.show()
#while_cond.right.show()


# That's it for the example. I hope you now see how easy it is to explore the
# AST created by pycparser. Although on the surface it is quite complex and has
# a lot of node types, this is the inherent complexity of the C language every
# parser/compiler designer has to cope with.
# Using the tools provided by the c_ast package it's easy to explore the
# structure of AST nodes and write code that processes them.
# Specifically, see the cdecl.py example for a non-trivial demonstration of what
# you can do by recursively going through the AST.