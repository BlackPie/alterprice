module.exports = class PrettyPrice
    @DECIMAL: 0
    @SEPARATOR: ' '

#    constructor: (options) ->
#        decimal = 0
#        separator = ' '


    @format: (number) =>
        number = parseFloat number
        exp10 = Math.pow 10, PrettyPrice.DECIMAL
        number = Math.round (number * exp10) / exp10
        number = Number(number).toFixed(PrettyPrice.DECIMAL).toString().split '.'
        number = number[0].replace /(\d{1,3}(?=(\d{3})+(?:\.\d|\b)))/g,"\$1" + PrettyPrice.SEPARATOR
        return number
