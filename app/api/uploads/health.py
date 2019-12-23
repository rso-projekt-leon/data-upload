from app.config import get_etcd_config

def demo_healthcheck():
    health_status = get_etcd_config('/data-upload/health-demo-status', 'HEALTH_DEMO_STATUS')
    if health_status == 'True':
        health_status = True
        message = "data-upload ok"
    else: 
        health_status = False
        message = "data-upload error"
    print('Health check', health_status)
    return health_status, message

def isready_healthcheck():
    return True, 'data-upload is ready'