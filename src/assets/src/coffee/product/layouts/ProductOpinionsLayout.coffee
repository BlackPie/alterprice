$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ProductOpinionsLayout extends Marionette.LayoutView
    el: $("#comments-wrapper-view")

    regions:
        opinionsList: ".comments-wrapper"


    #initialize: (options) =>
    #    console.log '-'


    hide: =>
        $(@el).hide()


    show: =>
        $(@el).show()