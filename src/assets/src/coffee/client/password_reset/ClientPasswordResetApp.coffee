BaseApp = require 'base/BaseApp'
ClientPasswordResetController = require './ClientPasswordResetController'
ClientPasswordResetRouter = require './ClientPasswordResetRouter'


module.exports = class ClientPasswordResetApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientPasswordResetController
	routerClass: ClientPasswordResetRouter
	urlRoot: "/"