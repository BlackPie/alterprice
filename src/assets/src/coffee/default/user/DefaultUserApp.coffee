BaseApp = require 'base/BaseApp'
DefaultUserController = require './DefaultUserController'
DefaultUserRouter = require './DefaultUserRouter'


module.exports = class DefaultUserApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: DefaultUserController
	routerClass: DefaultUserRouter
	urlRoot: "/"