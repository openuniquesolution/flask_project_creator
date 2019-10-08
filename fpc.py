#!/usr/bin/python

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

########################################################

import os
import sys
import logging
import argparse
import subprocess as sp



###############################################################################
# Helper function for working
def set_logging_level(logger, level):
    logging_level = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'error': logging.ERROR
    }

    logger.setLevel(logging_level[level[0]])


def read_args(argv=None):
    logging.debug("Parsing arguments")
    main_parse = argparse.ArgumentParser(prog="fpc", usage="Use to create boilder plate code for flask")
    main_parse.add_argument("action", help="Action you are going to take",
                            nargs="?",
                            choices=['genrate', 'create'])
    main_parse.add_argument("component", help="which component you want to create")
    main_parse.add_argument("name", help="Name of component")
    main_parse.add_argument("-l", "--logginglevel",
                            help="Logging level provide while running proces",
                            default=["error"],
                            nargs=1,
                            choices=['error', 'debug', 'info'])

    return main_parse.parse_args(argv)
###############################################################################


def genrate_action(component, name):
    pass

def create_new_project(name=None):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    sp.call("%s/base/new_project.sh %s"%(base_dir, name), shell=True)

def main(args):
    logging.debug(args)
    
    action = args.action
    component= args.component
    name = args.name
    
    if action == "genrate":
        genrate_action(component, name)
    elif action == "create":
        create_new_project(name)
            

if __name__ == "__main__":
    args = read_args(sys.argv[1:])
    logger = logging.getLogger(__name__)
    set_logging_level(logger, args.logginglevel)
    main(args)