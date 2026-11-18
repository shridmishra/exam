"""
Solution Formatter Engine.
Enforces the Zero Wall-of-Text Policy, zero inline continuation,
micro-tags for examples, and structured vertical bulleting.
"""

import re

def clean_num(raw: str) -> str:
    """Standardizes item numbers like '1.', 'a.', etc."""
    if not raw:
        return ""
    if raw == "&bull;":
        return "&bull;"
    return re.sub(r"[\.\)]+$", "", raw) + "."

def format_solution(html: str, math_enhancer=None) -> str:
    """
    Transforms dense solution HTML into clean, un-cardified editorial rows.
    Separates examples to dedicated lines, cleanly wraps numbered headings,
    and isolates list items without wall-of-text fatigue.
    """
    if not html:
        return ""
    
    # 1. Subject-specific LaTeX math enhancements if provided
    if math_enhancer and callable(math_enhancer):
        html = math_enhancer(html)
        
    html = html.replace("•", "&bull;").replace("·", "&bull;")
    html = html.replace("<br>\n<br>", "<br>").replace("<br><br>", "<br>")
    
    split_pattern = r'(?:<br\s*/?>\s*|\n\s*|(?=<div class="sol-diagram-box">|<div class="sol-table-wrap">)|(?<=</div>)\s*(?=(?:<br\s*/?>|\n|<strong>|\d+\.)))(?=(?:<strong>|\d+\.\s*|[a-zA-Z]\)\s*|[a-zA-Z]\.\s*|&bull;\s*|\(\d+\)\s*|\([a-zA-Z]\)\s*|<div class="sol-diagram-box">|<div class="sol-table-wrap">|$))'
    parts = re.split(split_pattern, html)
    formatted = []
    
    for p in parts:
        p = p.strip()
        if not p:
            continue
            
        m_num_outer = re.match(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", p)
        m_num_inner = re.match(r"^<strong>(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", p)
        
        num_str = ""
        if m_num_outer:
            num_str = clean_num(m_num_outer.group(1))
        elif m_num_inner:
            num_str = clean_num(m_num_inner.group(1))
            
        m_title_desc = re.match(r"^(?:(?:\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*)?<strong>(.*?)</strong>:?\s*(.*)$", p, re.DOTALL)
        m_num_only = re.match(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s+(.+)$", p, re.DOTALL)
        
        if m_title_desc:
            raw_title = m_title_desc.group(1).strip()
            raw_desc = m_title_desc.group(2).strip()
            
            title_clean = re.sub(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", "", raw_title).rstrip(":")
            desc_clean = re.sub(r"^(?:<br\s*/?>|\s)+", "", raw_desc)
            
            example_html = ""
            m_ex = re.search(r'(?:<br\s*/?>|\s)*<em>Example:?</em>\s*(.*?)(?=(?:<br\s*/?>\s*<strong>|<br\s*/?>\s*&bull;|$))', desc_clean, flags=re.IGNORECASE | re.DOTALL)
            if m_ex:
                desc_clean = desc_clean[:m_ex.start()].strip()
                example_text = m_ex.group(1).strip()
                example_html = f'<div class="sol-item-example"><span class="example-label">Example:</span> {example_text}</div>'
            else:
                desc_clean = re.sub(r'<em>Example:?</em>', '<span class="example-label">Example:</span>', desc_clean, flags=re.IGNORECASE)

            if not desc_clean and not example_html:
                if num_str and num_str != "&bull;" and not title_clean.startswith(num_str):
                    heading_text = f"{num_str} {title_clean}:"
                else:
                    heading_text = f"{title_clean}:"
                formatted.append(f'<div class="sol-heading">{heading_text}</div>')
            elif not num_str and len(title_clean) > 30:
                formatted.append(f'<div class="sol-heading">{title_clean}:</div><div class="sol-body-text">{desc_clean}{example_html}</div>')
            elif not num_str and raw_desc.startswith("<br>"):
                formatted.append(f'<div class="sol-heading">{title_clean}:</div><div class="sol-body-text">{desc_clean}{example_html}</div>')
            else:
                num_html = f'<span class="sol-item-num">{num_str}</span>' if num_str else ""
                formatted.append(f"""<div class="sol-item-row">
    {num_html}
    <div class="sol-item-content">
        <span class="sol-item-title">{title_clean}:</span> 
        <span class="sol-item-text">{desc_clean}</span>
        {example_html}
    </div>
</div>""")
        elif m_num_only and m_num_only.group(2).strip():
            num = clean_num(m_num_only.group(1))
            desc_clean = re.sub(r"^(?:<br\s*/?>|\s)+", "", m_num_only.group(2).strip())
            
            example_html = ""
            m_ex = re.search(r'(?:<br\s*/?>|\s)*<em>Example:?</em>\s*(.*?)(?=(?:<br\s*/?>\s*<strong>|<br\s*/?>\s*&bull;|$))', desc_clean, flags=re.IGNORECASE | re.DOTALL)
            if m_ex:
                desc_clean = desc_clean[:m_ex.start()].strip()
                example_text = m_ex.group(1).strip()
                example_html = f'<div class="sol-item-example"><span class="example-label">Example:</span> {example_text}</div>'
            else:
                desc_clean = re.sub(r'<em>Example:?</em>', '<span class="example-label">Example:</span>', desc_clean, flags=re.IGNORECASE)

            formatted.append(f"""<div class="sol-item-row">
    <span class="sol-item-num">{num}</span>
    <div class="sol-item-content">
        <span class="sol-item-text">{desc_clean}</span>
        {example_html}
    </div>
</div>""")
        else:
            if p.startswith('<div class="sol-diagram-box">') or p.startswith('<div class="sol-table-wrap">'):
                formatted.append(p)
            else:
                p_clean = re.sub(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", r'<span class="sol-item-num">\1</span> ', p)
                formatted.append(f'<div class="sol-step">{p_clean}</div>')
            
    return "".join(formatted)
