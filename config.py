class Config:
    SECRET_KEY  = 'fasfdfafasfadfaskibidisigmapogmichambasmegmaboyfornitehittlerasdadasdavvasadasbdasdadgsdfga'
    DEBUG       = True

class DevelomentConfig(Config):
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'fashly'

config = {
    'development': DevelomentConfig
}