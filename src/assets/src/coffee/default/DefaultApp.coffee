BaseApp = require 'base/BaseApp'
DefaultController = require './DefaultController'
DefaultRouter = require './DefaultRouter'


module.exports = class DefaultApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: DefaultController
	routerClass: DefaultRouter
	urlRoot: "/"