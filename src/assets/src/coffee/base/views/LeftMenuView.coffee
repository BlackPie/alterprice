$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class LeftMenuView extends Marionette.ItemView
    el: $('#left-column-block')

    template: false

    ui:
        toggleSubCategoryBtn: '.has-submenu > a'

    events:
        "click @ui.toggleSubCategoryBtn":  "onClickToggleSubCategoryBtn"



    initialize: (options) =>
        @channel = options.channel


    onClickToggleSubCategoryBtn: (e) =>
        e.preventDefault()
        el = @$(e.target).closest '.has-submenu'
        if el.hasClass 'open'
            el.find('ul').slideUp 200
            el.removeClass 'open'
        else
            el.find('ul').slideDown 200
            el.addClass 'open'