$ = require 'jquery'


module.exports = class Switcher

    constructor: (el) ->
        @el = $(el)
        @checkbox = @el.find('input[type="checkbox"]')
        _ = @

        @el.on 'click', (e) =>
            if _.checkbox.is ':checked'
                _.el.addClass 'on'
            else
                _.el.removeClass 'on'