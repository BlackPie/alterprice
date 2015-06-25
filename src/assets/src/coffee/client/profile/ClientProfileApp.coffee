BaseApp = require 'base/BaseApp'
ClientProfileController = require './ClientProfileController'
ClientProfileRouter = require './ClientProfileRouter'


module.exports = class ClientProfileApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientProfileController
	routerClass: ClientProfileRouter
	urlRoot: "/"