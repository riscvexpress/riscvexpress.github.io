function RawInline(el)
  if el.format == 'tex' and el.text:match('\\colorbox') then
    local content = el.text:match('{(.-)}{(.-)}')
    local color, text = content:match('([^{}]+)}{([^{}]+)')
    return pandoc.RawInline('html', '<span style="background-color:' .. color .. ';">' .. text .. '</span>')
  end
end