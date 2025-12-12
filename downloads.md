---
layout: default
title: Script Downloads
permalink: /downloads/
---

# Downloads

All scripts used in this portfolio are available for download below. There are also small descriptions and viewable code block without downloading available [Here]({{ site.baseurl }}/#algorithms-with-code)

---

<ul>
{% for file in site.static_files %}
  {% if file.path contains '/scripts/' %}
    <li>
      <a href="{{ file.path | relative_url }}" download>
        {{ file.name }}
      </a>
    </li>
  {% endif %}
{% endfor %}
</ul>

---