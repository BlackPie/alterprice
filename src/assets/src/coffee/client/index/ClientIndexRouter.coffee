Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientIndexRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"