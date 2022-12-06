import logging,os,time
class Logging():
    def make_log_dir(self,dirname='logs'): #创建日志存放目录，并返回目录的路径
        now_dir=os.path.dirname(os.path.dirname(__file__))
        # father_path=os.path.split(now_dir)[0]
        path=os.path.join(now_dir,dirname)
        path=os.path.normpath(path) #os.path.normpath()方法规范路径输出格式
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_log_filename(self): #创建文件文件名格式，便于区分每天的日志
        filename="{}.log".format(time.strftime("%Y-%m-%d",time.localtime()))
        filename=os.path.join(self.make_log_dir(),filename)
        filename=os.path.normpath(filename)
        return filename

    def log(self,level='DEBUG'): #生成日志的主方法，传入对哪些级别以上的日志进行处理
        logger=logging.getLogger()
        logger.setLevel(level)
        if not logger.handlers:
            sh=logging.StreamHandler()
            fh=logging.FileHandler(filename=self.get_log_filename(),mode='a',encoding="utf-8")
            fmt=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-line:%(lineno)d-message:%(message)s")
            sh.setFormatter(fmt=fmt)
            fh.setFormatter(fmt=fmt)
            logger.addHandler(fh)
            logger.addHandler(sh)
        return logger

logger=Logging().log()

if __name__=='__main__':
    logger.debug("debug-111111")
    logger.info("info-2222222")
    logger.error("error-333333")
    logger.warning("warning-4444444")
    logger.critical("critical-555555")
