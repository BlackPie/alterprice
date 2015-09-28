Number = require 'base/utils/Number'



template = (locals) =>

    name = (locals) =>
        if locals and locals.product and locals.product.name
            locals.product.name
        else
            undefined

    if locals.is_category
        return "<td class=\"category\">#{locals.category}</td><td class=\"category\"></td>"
    else
        if locals.product_url
            name = "<a href=\"#{locals.product_url}\" target=\"_blank\">#{name(locals)}</a>"
        else
            name = name(locals)

        return "
            <td>#{name}</td>
            <td class=\"text-center\">#{locals.click_price}</td>"


module.exports = template
