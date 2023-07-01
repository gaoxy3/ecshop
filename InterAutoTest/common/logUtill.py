import logging,datetime

# logger = logging.getLogger("logUtill")
# logger.setLevel(logging.DEBUG)
# #输出到控制台
# fmhandler = logging.StreamHandler()
# formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s ")
# fmhandler.setFormatter(formater)
#
# #输出到文件
# current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# filehandler = logging.FileHandler("../log/"+current_time+".log")
# filehandler.setFormatter(formater)
# logger.addHandler(fmhandler)
# logger.addHandler(filehandler)
#
#
# logger.debug("debug...")
# logger.info("info...")
# logger.warning("warning...")
# logger.error("error...")
# logger.critical("critical...")
class LogUtill():
    def __init__(self,filesrc="log/",loggername=__file__,level=logging.DEBUG):
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            #输出到控制台
            fmhandler = logging.StreamHandler()
            formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s ")
            fmhandler.setFormatter(formater)

            #输出到文件
            current_time = datetime.datetime.now().strftime("%Y-%m-%d")
            filehandler = logging.FileHandler(filesrc+current_time+".log",encoding="utf-8")
            filehandler.setFormatter(formater)
            self.logger.addHandler(fmhandler)
            self.logger.addHandler(filehandler)

if __name__ == '__main__':
   log= LogUtill().logger
   log.error("错误信息。。。")