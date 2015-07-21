Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientStatisticsRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"