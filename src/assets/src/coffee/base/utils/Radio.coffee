$ = require 'jquery'


module.exports = class Radio

    constructor: (el) ->
        @el = $(el)
        @inputs = @el.find('input[type="radio"]')
        @labels = @el.find('label.radio')
        _ = @

        @sync()

        @inputs.on 'change', (e) =>
            _.sync()


    sync: =>
        @labels.removeClass('selected')
        @inputs.filter(':checked').closest('label').addClass('selected')
