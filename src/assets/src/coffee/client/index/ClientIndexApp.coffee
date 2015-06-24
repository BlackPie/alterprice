BaseApp = require 'base/BaseApp'
ClientIndexController = require './ClientIndexController'
ClientIndexRouter = require './ClientIndexRouter'


module.exports = class ClientIndexApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientIndexController
	routerClass: ClientIndexRouter
	urlRoot: "/"