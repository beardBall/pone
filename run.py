import myflaskApp
import config
import os


print(config)
myflaskApp.appStart(config.uat)
print('exiting')

