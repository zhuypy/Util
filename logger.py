import sys
import os
class Logger():
    '''
        log tool class
        suport user-defined log file path and log levels and types
    '''

    def __init__(self):
        self.log_path = LOG_PATH
        self.log_file = os.path.join(self.log_path,'AutoTest'+str(getCurrentTime())+'.log')

    def setLogFileLocation(self,file):
        '''
        modify log storage location
        :param file: log file
        :return: None
        '''
        self.log_file = file

    def writeTextFile(self,msg,kind=None,level=None,file=None,pureMode=False):
        '''
        write in log file
        :param msg: log message
        :param kind: information type such as info or error or debug
        :param level: error level
        :param file: log file
        :param pureMode: pure mode means that message written to a log file has no prefix such as kind
        :return:
        '''
        if not pureMode:
            kind =  '['+kind+']' if kind else ' '
            level = '['+level+']' if  level else ' '
            frame_list = str(sys._getframe(2)).split(',')
            py_location = '['+frame_list[1][7:-1]+']'
            py_line = '['+frame_list[2][1:]+']'
            msg = kind +level+py_location+py_line+str(msg)
        msg = msg.replace(r'\\','\\').replace('//','/') + '\r\n'
        print(msg) # pycharm debugging
        if not file:
            with open(self.log_file,'a+',encoding='utf-8') as fb:
                fb.write(msg)

        else:
            with open(file,'a+',encoding='utf-8') as fb:
                fb.write(msg)

    def info(self,msg,level='common'):
        '''
         ordinary logs
        :param msg: log message
        :param level: error level
        :return:
        '''
        self.writeTextFile(msg,kind='INFO',level=level)

    def error(self,msg,level='common'):
        '''
        error log
        :param msg: log message
        :param level: error level  cosmetic,Minor,major,critical
        :return:
        '''
        self.writeTextFile(msg, kind='ERROR', level=level)

    def debug(self,msg,level='common'):
        '''
        debug log
        :param msg:log message
        :param level:error level
        :return:
        '''
        self.writeTextFile(msg, kind='Debug', level=level)

    def mark(self,msg):
        '''
        mark execution phase
        :param msg:tag content
        :return:None
        '''
        if msg == self.OK or msg == self.NG:
            self.writeTextFile(str(msg),pureMode=True)
        else:
            self.writeTextFile('====================================%s========================================='%(msg),pureMode=True)


    OK = '''
                    @@@@@@@       @@@        @@@
                  @@@      @@@    @@@      @@@
                 @@@        @@@   @@@    @@@
                @@@          @@@  @@@ @@@
                @@@          @@@  @@@@@
                @@@          @@@  @@@ @@@
                 @@@        @@@   @@@    @@@
                  @@@      @@@    @@@      @@@
                    @@@@@@@@      @@@        @@@
        '''


    NG ='''
                @@@@@@@@@         @@@         @@   @@
                @@               @@ @@             @@
                @@              @@   @@       @@   @@
                @@             @@     @@      @@   @@   
                @@@@@@@@@     @@@@@@@@@@@     @@   @@
                @@           @@         @@    @@   @@
                @@          @@           @@   @@   @@
                @@         @@             @@  @@   @@
                @@        @@               @@ @@   @@@@@@@@@@@@
        '''


logger = Logger()

