import logging
import sys

from cliff.command import Command
import start

class Stop(Command):
    "Stop current  activity."
    log = logging.getLogger(__name__)
    
    def take_action(self, parsed_args):
        self.log.info('stopping activity') 
        self.log.debug('debugging') 
        
        if not start.activity.timer.startTime==start.activity.timer.stopTime: 
            self.app.stdout.write('stop '+ start.activity.type)
            self.app.stdout.write('Duration ')
            # Duration is returned from Timer as (minutes,seconds)
            hours, minutes = divmod(start.activity.duration()[0], 60)
            self.app.stdout.write('hours: '+ hours)
            self.app.stdout.write('minutes: '+ minutes)
            self.app.stdout.write('seconds: '+ start.activity.duration()[1])
        else:
            self.app.stdout.write("No current  activity.")


