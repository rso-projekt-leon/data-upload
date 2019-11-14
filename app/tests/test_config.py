import os

def test_development_config(test_app):
    test_app.config.from_object('app.config.DevelopmentConfig')
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']


def test_testing_config(test_app):
    test_app.config.from_object('app.config.TestingConfig')
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert test_app.config['TESTING']


def test_production_config(test_app):
    test_app.config.from_object('app.config.ProductionConfig')
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']
