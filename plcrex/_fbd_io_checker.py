#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022 Marcel Werner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import logging
from pprint import pprint
from lark import Lark, tree
from lark.reconstruct import Reconstructor
from pathlib import Path
from lark import Lark, logger, Tree, Token, Transformer, tree
from lark.parsers.earley_forest import TreeForestTransformer, handles_ambiguity, Discard
from lark.reconstruct import Reconstructor
from lark.visitors import Visitor_Recursive, Visitor
from pathlib import Path

logger.setLevel(logging.DEBUG)

inputs = []
outputs = []
variables = []


class Create_DOT_AST(Transformer):
    # override name in DOT AST
    def name(self, tree):
        tree[0] = Tree(Token('RULE', 'name'), [pou_name])
        return tree[0]


class Analyze_ST_AST(Visitor):
    # get POU name from ST AST
    def name(self, tree):
        global pou_name
        pou_name = tree.children[0]

    # get inputs / outputs from ST AST
    def idcl(self, tree):
        for e2 in tree.children:
            if e2.data == "var_input":
                for e3 in e2.children[0].children:
                    inputs.append(str(e3.children[0].children[0]))
            elif e2.data == "var_output":
                for e3 in e2.children[0].children:
                    outputs.append(str(e3.children[0].children[0]))

    # get local variables from ST AST
    def vdcl(self, tree):
        for e2 in tree.children:
            if e2.data == "var_local":
                for e3 in e2.children[0].children:
                    variables.append(str(e3.children[0].children[0]))


def get_var_latest_define(
        def_use_chain_i: list,
        var_i: str):
    print(" *** get latest definition of " + var_i)

    def_found = False
    for i in reversed(def_use_chain_i):
        if i[0] == var_i:
            def_found = True
            pprint(i)
            return i
    if not def_found:
        return ['999', Tree('not used', []), Tree('not used', []), 999]

#TODO
#def get_var_last_define_id(
#        def_use_chain_i: list,
#        var_i: str,
#        def_id: int):
#    print(" === get_var_last_define_id")
#    for i in reversed(def_use_chain_i):
#        if i[3] <= def_id and i[0] == var_i:
#            return i
#    return Tree('not used', [])


def get_all_uses(
        def_use_chain_i: list,
        define_latest_tree_i: list):
    print(" *** *** get all uses")
    uses_related_to_def_x = []
    # if output is used / not None
    if define_latest_tree_i[1] != Tree('not used', []):
        defined_stat_last_tree = define_latest_tree_i[1]
        defined_last_id = define_latest_tree_i[3]

        # Find all statements related to def_statement
        for i in def_use_chain_i:
            used = i[2]
            if defined_stat_last_tree == used:
                uses_related_to_def_x.append(i)
        pprint(uses_related_to_def_x)
    return uses_related_to_def_x


#TODO
#def get_all_related_uses(
#        def_use_chain_i: list,
#        define_latest_tree_i: list):
#    print(" *** *** get all related uses")
#    uses_related_to_def_x = []
#
#    # if output is used / not None
#    if define_latest_tree_i[1] is not Tree('not used', []):
#        defined_stat_last_tree = define_latest_tree_i[1]
#        defined_last_id = define_latest_tree_i[3]
#
#        # Find all statements related to def_statement
#        for i in def_use_chain_i:
#            used = i[2]
#            id_used = i[3]
#            if defined_stat_last_tree == used and defined_last_id == id_used:
#                uses_related_to_def_x.append(i)
 #   return uses_related_to_def_x


def data_flow_analysis(
        def_use_chain_i: list,
        all_uses_i: list,
        inputs_i: list,
        related_inputs_i: list
):
    rec_active = False
    for u in all_uses_i:
        # check if definition is Tree('DEFAULT', []) := Input or Variable Declaration
        rec_not_needed = False
        if u[1] == Tree('DEFAULT', []):
            for i in inputs_i:
                if u[0] == i:
                    rec_not_needed = True
                    related_inputs_i.append(u[0])
                    print("Input with impact found: " + u[0])
                    break
                # if deppest finding is not a input, but constant variable
                if not rec_not_needed:
                    # return list of inputs
                    #return related_inputs_i
                    related_inputs_i = related_inputs_i
        # recursive call of data_flow_analysis for each variable whose definition is not 1st one
        else:
            rec_active = True
            print("call data_flow_analysis again: " + u[0])
            latest_define_sub = get_var_latest_define(def_use_chain_i, u[0])
            all_uses_sub = get_all_uses(def_use_chain_i, latest_define_sub)
            return data_flow_analysis(def_use_chain_i, all_uses_sub, inputs_i, related_inputs_i)
    # return list of inputs
    if not rec_active:
        return related_inputs_i

def data_flow_analysis_st(src: Path):
    # DOT AST default Tree
    dot_ast = Tree(Token('RULE', 'start'), [Tree(Token('RULE', 'digraph'), [
        Tree(Token('RULE', 'name'), [Token('NAME', 'unknown')]), Tree(Token('RULE', 'dependencies'), [])])])

    # ST parser config
    with open(r'.\data\STgrammar.lark', 'rt') as file:
        st_grammar = file.read()
    st_parser = Lark(st_grammar, parser='earley', maybe_placeholders=False, propagate_positions = True)

    # DOT parser config
    with open(r'.\data\DOTgrammar.lark', 'rt') as file:
        dot_grammar = file.read()
    dot_parser = Lark(dot_grammar, parser='earley', maybe_placeholders=False)

    # open ST file
    with open(src, 'rt') as file:
        print("\n *************************************************************************************** ")
        print(" *** Parse ST ************************************************************************** ")
        print(" *************************************************************************************** ")
        st_source = file.read()
        st_ast = st_parser.parse(st_source)

        print(st_ast)
        #print(st_ast.pretty())

        # open DOT file
        #with open(r"..\tests\other_examples\DOT.dot", 'rt') as file:
        #   dot_source = file.read()
        #   dot_ast_tmp = dot_parser.parse(dot_source)
        #   print(dot_ast_tmp)

        Analyze_ST_AST().visit_topdown(st_ast)
        print("Inputs:")
        print(inputs)
        print("Outputs:")
        print(outputs)
        print("local Variables:")
        print(variables)

        # Build Define-Uses-Chain
        print("\n *************************************************************************************** ")
        print(" *** Build Def-Use-Chain *************************************************************** ")
        print(" *************************************************************************************** ")
        all_variables = inputs + outputs + variables
        def_use_chain = [[str , Tree , Tree, int]]

        # go through each variable (inputs + outputs + variables)
        for v in all_variables:
            print(v)

            use_to_add = Tree('not used', [])
            def_to_add = Tree('DEFAULT', [])
            stat_index = 1
            with_decl = False

            # check all statements in ST AST
            for t1 in st_ast.iter_subtrees_topdown():
                # 1. Find 1st definition
                # start at tree with declarations
                #if t1.data == "declaration":
                #    var_to_check = t1.children[0].children[0]
                #    if var_to_check == v: #t1.children[0].data == "variable" and
                #        for get_ini_value in t1.find_data("constant"):
                #            def_to_add = get_ini_value
                #            break
                #        def_use_chain.append([v, def_to_add, use_to_add, stat_index])
                #        print(def_to_add)
                #        print(">>> UPDATED-declaration \n")
                #    stat_index += 1

                # only statemets are considered, so declarations are skipped
                # 2. Find Xnd use and Ynd Update
                if t1.data == "statement": #elif when 1. step is uncommented
                     # check if v is updated or used within immediate_assignment
                    if t1.children[0].data == "immediate_assignment":
                        var_pot_updated = t1.children[0].children[0].children[0]
                        if v == var_pot_updated:
                            def_to_add = t1.children[0]#.children
                            print(def_to_add)
                            def_use_chain.append([v, def_to_add, use_to_add, stat_index])
                            #stat_index += 1
                            print(">>> UPDATED-immediate_assignment \n")
                        else:
                            for t2 in t1.find_data("variable"):
                                var_pot_used = t2.children[0]
                                if v == var_pot_used:
                                    use_to_add = t1.children[0]
                                    print(use_to_add)
                                    def_use_chain.append([v, def_to_add, use_to_add, stat_index])
                                    #stat_index += 1
                                    print(">>> USED-immediate_assignment \n")
                                    break

                    # check if v is used within macro
                    elif t1.children[0].data == "macro":
                        var_pot_updated = t1.children[0].children[0]
                        if v == var_pot_updated:
                            def_to_add = t1.children[0]
                            print(def_to_add)
                            def_use_chain.append([v, def_to_add, use_to_add, stat_index])
                            #stat_index += 1
                            print(">>> UPDATED-macro \n")
                        for t2 in t1.find_data("variable"):
                            var_pot_used = t2.children[0]
                            if v == var_pot_used:
                                use_to_add = t1.children[0]
                                print(use_to_add)
                                def_use_chain.append([v, def_to_add, use_to_add, stat_index])
                                #stat_index += 1
                                print(">>> USED-macro \n")
                                break
                    stat_index += 1

        # remove 1st dummy entry
        def_use_chain.pop(0)

        print(" *** Final Def-Use-Chain ***")
        pprint(def_use_chain)


        # I/O data-flow analysis
        print("\n *************************************************************************************** ")
        print(" *** I/O Data-Flow Analysis ************************************************************ ")
        print(" *************************************************************************************** ")

        io_list = []

        relation_to_add = []
        for o in outputs:
            print(" *** related inputs of " + o + " (START)")
            related_inputs = []
            print(" *** walk through tree")
            latest_define = get_var_latest_define(def_use_chain, o)
            all_uses = get_all_uses(def_use_chain, latest_define)
            related_inputs = data_flow_analysis(def_use_chain, all_uses, inputs, related_inputs)

            # remove duplicates
            related_inputs = list(dict.fromkeys(related_inputs))
            print(" *** related inputs of " + o + " (FINAL)")

            # create relations as AST subtrees
            for i in related_inputs:
                relation_to_add.append(Tree(Token('RULE', 'entry'), [Token('NAME', i), Token('NAME', o)]))
            print(related_inputs)
        pprint(relation_to_add)

        # generate DOT AST
        print("\n *************************************************************************************** ")
        print(" *** Generate DOT AST ****************************************************************** ")
        print(" *************************************************************************************** ")
        dot_ast = Create_DOT_AST().transform(dot_ast)
        dot_ast.children[0].children[1].children = relation_to_add
        print(dot_ast)
        print(dot_ast.pretty())

        # reconstruct DOT code
        print("\n *************************************************************************************** ")
        print(" *** Reconstruct DOT code ************************************************************** ")
        print(" *************************************************************************************** ")
        dot_reconstructed = Reconstructor(dot_parser).reconstruct(dot_ast)

        print(dot_reconstructed)

        dot_export = open(fr'.\exports\tree\dot\{Path(src).name}.dot', "w")
        dot_export.write(dot_reconstructed)

#data_flow_analysis_st(Path(r"..\tests/st_examples/TC006_fbd.st"))
