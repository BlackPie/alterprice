$ = require 'jquery'


module.exports = class Checkbox

    constructor: (options) ->
        @el = $(options.el)
        @input = @el.find('input[type="checkbox"]')
        @sync()
        _ = @

        @input.on 'change', (e) =>
            _.sync()


    sync: =>
        if @input.is ':checked'
            @el.addClass 'checked'
        else
            @el.removeClass 'checked'


    @init: (elements) =>
        elements.each (i, el) =>
            new Checkbox {el: el}
