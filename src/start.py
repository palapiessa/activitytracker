import logging
import sys

from cliff.command import Command
from ActivityEvent import ActivityEvent
from Timer import Timer
import time

this = sys.modules[__name__]
this.types = ["cycle","sleep","run",""]
this.units = ["km","min"]
this.timeout = 86400 # 1 day

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
        start = time.time()
        this.activity = ActivityEvent(this.types,this.units)
        print("Activity created")
        while (raw_input() == "stop"): #or start > this.timeout):
            #time.sleep(5)
            this.activity.timer.stop()
            # Duration is returned from Timer as (minutes,seconds)
            hours, minutes = divmod(this.activity.timer.duration()[0], 60)
            self.app.stdout.write('hours: '+ hours)
            self.app.stdout.write('minutes: '+ minutes)
            self.app.stdout.write('seconds: '+ this.activity.timer.duration()[1])
            this.timer = None
