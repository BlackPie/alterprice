Number = require 'base/utils/Number'

template = (locals) =>
    if locals.is_category
        return "<td class=\"category\">#{locals.category}</td><td class=\"category\"></td>"
    else
        if locals.viewURL
            name = "<a href=\"#{locals.viewURL}\" target=\"_blank\">#{locals.product.name}</a>"
        else
            name = locals.product.name

        return "
            <td>#{name}</td>
            <td class=\"text-center\">#{locals.click_price}</td>"


module.exports = template
