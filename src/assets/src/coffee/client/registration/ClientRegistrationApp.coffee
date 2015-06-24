BaseApp = require 'base/BaseApp'
ClientRegistrationController = require './ClientRegistrationController'
ClientRegistrationRouter = require './ClientRegistrationRouter'


module.exports = class ClientRegistrationApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientRegistrationController
	routerClass: ClientRegistrationRouter
	urlRoot: "/"