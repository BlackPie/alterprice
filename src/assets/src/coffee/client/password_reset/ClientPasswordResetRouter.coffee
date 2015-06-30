Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientPasswordResetRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"