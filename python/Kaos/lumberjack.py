#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import konst
import os
from datetime import datetime

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = konst.pwd

def logger(command, path="%s/k.log" % pwd, *args):
    """ Log the output of another kaos function to the specified file.
        Defaults to '[cwd at the time of kaos import]/k.log' """

    if len(args) >= 1:
        raise kerri.ExcessArguments("logger()", 2)
    else:
        try:
            with open(path, 'a') as log:
                log.write(str(command)+"\n")
                log.close()
        except Exception as error:
            raise kerri.Unknown("logger()", error)

def logit(message, path="%s/kaos.logit" % pwd, *args):
        """ Write A Message To A Log File """

        logtime = datetime.now()
        if len(args) >= 1:
            raise kerri.ExcessArguments("logit()", 2)
        else:
            try:
                with open(path, 'a') as log:
                    log.write("[%s]:\n    %s\n" % (logtime, message))
                    log.close()
                return "Output Written To %s" % path
            except Exception as error:
                raise kerri.ProcessFailure("logit()", error)
