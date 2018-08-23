import logging
import sys

from cliff.command import Command
from ActivityEvent import ActivityEvent
from Timer import Timer

this = sys.modules[__name__]
this.types = ["cycle","sleep","run",""]
this.units = ["km","min"]
this.activity = ActivityEvent(this.types,this.units)

class Start(Command):
    "Start an activity. Give activity type as argument. Only one activity can be started per time."
    log = logging.getLogger(__name__)
    
    def get_parser(self, prog_name):
        parser = super(Start, self).get_parser(prog_name)
        parser.add_argument("type",help="type of the activity",choices=this.types)
        return parser
    
    def take_action(self, parsed_args):
        self.log.info('starting activity') 
        self.log.debug('debugging') 
        self.app.stdout.write('start '+ parsed_args.type + '\n')
        if not this.activity.type: 
            this.activity.type = parsed_args.type
        else:
            self.app.stdout.write("Only one activity can be started per time.")
            
