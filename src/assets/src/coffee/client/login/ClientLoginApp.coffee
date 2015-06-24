BaseApp = require 'base/BaseApp'
ClientLoginController = require './ClientLoginController'
ClientLoginRouter = require './ClientLoginRouter'


module.exports = class ClientLoginApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientLoginController
	routerClass: ClientLoginRouter
	urlRoot: "/"