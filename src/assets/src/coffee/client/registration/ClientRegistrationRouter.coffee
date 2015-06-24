Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientRegistrationRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"