Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientLoginRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"