import os
import etcd
from flask import current_app as app

def get_etcd_config(key, fail_env_var):
    try:
        client = etcd.Client(host=app.config['CONFIG_ETCD_HOST_IP'], port=int(app.config['CONFIG_ETCD_HOST_PORT']))
        try:
            return client.read(key).value
        except etcd.EtcdKeyNotFound as e:
            return os.environ.get(fail_env_var)
    except:
        return os.environ.get(fail_env_var)

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = "my_precious"
    ALLOWED_EXTENSIONS = ('csv')
    UPLOAD_FOLDER = '/home'
    VERSION = '1.4'
    SERVICE_NAME = 'data_upload'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    CONFIG_ETCD_HOST_IP = 'etcd'
    CONFIG_ETCD_HOST_PORT = 2379

    @property
    def DATA_STORAGE_URL(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("DATA_STORAGE_URL")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/storage-url').value
        except:
            return os.environ.get("DATA_STORAGE_URL")

    @property
    def DATA_CATALOG_URL(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("DATA_CATALOG_URL")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/catalog-url').value
        except:
            return os.environ.get("DATA_CATALOG_URL")

    @property
    def HEALTH_DEMO_STATUS(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("HEALTH_DEMO_STATUS")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/health-demo-status').value
        except:
            return os.environ.get("HEALTH_DEMO_STATUS")        


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    UPLOAD_FOLDER = '/home/app/app'
    CONFIG_ETCD_HOST_IP = os.environ.get("CONFIG_ETCD_HOST_IP")
    CONFIG_ETCD_HOST_PORT = os.environ.get("CONFIG_ETCD_HOST_PORT") 

    @property
    def DATA_CATALOG_URL(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("DATA_CATALOG_URL")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/catalog-url').value
        except:
            return os.environ.get("DATA_CATALOG_URL")

    @property
    def HEALTH_DEMO_STATUS(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("HEALTH_DEMO_STATUS")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/health-demo-status').value
        except:
            return os.environ.get("HEALTH_DEMO_STATUS")

    @property
    def DATA_STORAGE_URL(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("DATA_STORAGE_URL")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-upload/storage-url').value
        except:
            return os.environ.get("DATA_STORAGE_URL")
