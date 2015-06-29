Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientWalletRefillRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"