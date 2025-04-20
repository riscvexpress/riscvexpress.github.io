function RawBlock(el)
  if el.format == "latex" and el.text:match("\\begin{tcolorbox}") then
    local content = el.text
      :match("\\begin{tcolorbox}[^\n]*.-\\begin{verbatim}(.-)\\end{verbatim}.-\\end{tcolorbox}")
      or "(No content found)"

    local html = [[
<div style="background-color:#f9f9f9; border:1px solid #ccc; padding:0.75em; border-radius:5px; font-family:monospace; margin:1em 0;">
<pre style="margin:0;"><code>]] ..
      pandoc.text.escape(content) ..
      [[</code></pre>
</div>]]

    return pandoc.RawBlock("html", html)
  end
end