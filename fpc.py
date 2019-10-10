#!/usr/bin/python3

########################################################
# This is main file which we use to create basic folder
# structure for flask.

# While creatind any folder structure we consider few things
#  1> New_project
#  2> model add
#  3> controller add
#  4> template add

# This all file are added in base folder

# There is one more folder plugin in which we
# take care for flask plugin but not now

#######################################################################################################

import os
import sys
import logging
import argparse
import subprocess as sp
import base.new_project as np



base_dir = os.path.dirname(os.path.realpath(__file__))

#######################################################################################################
# Helper function for working
def set_logging_level(logger, level):
    logging_level = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'error': logging.ERROR
    }

    logger.setLevel(logging_level[level[0]])

#######################################################################################################

def read_args(argv=None):
    logging.debug("Parsing Argument")
    main_parser = argparse.ArgumentParser(prog="fpc", usage="Use to create boilder plate code for flask", add_help=False)

    main_parser.add_argument("-l", "--logginglevel",
                        help="Logging level provide while running proces",
                        default=["error"],
                        choices=['error', 'debug', 'info'])

    sub_parser = main_parser.add_subparsers(dest='action',help="Provide mode or actions you want to perform")

        
    new_parser = sub_parser.add_parser('new', aliases=['n'])
    new_parser.add_argument('name',
                            help="New project name you want to create")
    new_parser.add_argument('-s', '--structure',
                            help="This flag used to decide folder structure <layer, component>",
                            choices=['layer', 'component', 'rest'],
                            default='component')
    new_parser.add_argument('-g', '--git', help="Enable git in project")
    new_parser.add_argument('-v', '--venv', help="Enable virtual Environment in project")
    

    genrate_parser=sub_parser.add_parser('genrate', aliases=['g'])
    genrate_parser.add_argument('component',
                                help="Which componet you want to add",
                                choices=['blueprint'])
    genrate_parser.add_argument('name')

    return main_parser.parse_args(argv)
###########################################################################################################


def genrate_action(component, name):
    sp.call("%s/base/genrate_component.py %s %s"%(base_dir,args.component, args.name), shell=True)

def create_new_project(args):
    np.main(args)

def main(args):
    logging.debug(args)
    
    # action = args.action
    # component= args.component
    # name = args.name
    
    if args.action == "genrate" or args.action == 'g':
        component = args.component
        name = args.name

        genrate_action(component, name)
    elif args.action == "new" or args.action == 'n':
        
        create_new_project(args)
            

if __name__ == "__main__":
    args = read_args(sys.argv[1:])
    print(args)
    logger = logging.getLogger(__name__)
    #set_logging_level(logger, args.logginglevel)
    main(args)