BaseApp = require 'base/BaseApp'
ClientStatisticsController = require './ClientStatisticsController'
ClientStatisticsRouter = require './ClientStatisticsRouter'


module.exports = class ClientStatisticsApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientStatisticsController
	routerClass: ClientStatisticsRouter
	urlRoot: "/"