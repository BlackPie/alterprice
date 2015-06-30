BaseApp = require 'base/BaseApp'
ClientWalletBalanceController = require './ClientWalletBalanceController'
ClientWalletBalanceRouter = require './ClientWalletBalanceRouter'


module.exports = class ClientWalletBalanceApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientWalletBalanceController
	routerClass: ClientWalletBalanceRouter
	urlRoot: "/"