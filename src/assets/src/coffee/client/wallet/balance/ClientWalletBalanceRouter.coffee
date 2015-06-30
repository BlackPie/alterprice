Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientWalletBalanceRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"