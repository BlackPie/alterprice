Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientProfileRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"