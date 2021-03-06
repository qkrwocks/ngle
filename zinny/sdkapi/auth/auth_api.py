# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class auth():

	def __init__(self):
		self.ngle = nGle_util()

	def loginZinnyDevice3(self, send_data):
		sd = send_data

		server = sd['server']

		data = [
			sd['uri'],
			{
				"txNo": sd['txNo']
			},
			{
				"appId": sd['appId'],
				"appSecret": sd['appSecret'],
				"deviceId": sd['deviceId'],
				"serialNo": sd['serialNo'],
				"accessToken": sd['accessToken'],
				"country": sd['country'],
				"lang": sd['lang'],
				"market": sd['market'],
				"appVer": sd['appVer'],
				"sdkVer": sd['sdkVer'],
				"os": sd['os'],
				"osVer": sd['osVer'],
				"telecom": sd['telecom'],
				"deviceModel": sd['deviceModel'],
				"network": sd['network'],
				"loginType": sd['loginType']
			}
		]

		data = self.ngle.websocket_sendData(server, data)
		return data




	

